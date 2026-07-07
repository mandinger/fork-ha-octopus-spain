"""Local storage of invoice PDFs.

The API returns presigned S3 URLs that expire minutes after they are issued.
Downloading the PDF right after each fetch gives the user a durable copy under
config/www, served by Home Assistant at /local/octopus_spain_fork/... .
"""
from __future__ import annotations

import logging
import os
from pathlib import Path
from typing import Any, Optional

import aiohttp

from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.util import slugify

from .const import LOCAL_URL_PREFIX, PDF_WWW_SUBDIR

_LOGGER = logging.getLogger(__name__)

DOWNLOAD_TIMEOUT = aiohttp.ClientTimeout(total=60)


class InvoicePdfManager:
    """Download and keep track of invoice PDFs under config/www."""

    def __init__(self, hass: HomeAssistant) -> None:
        self._hass = hass
        self._base_dir = Path(hass.config.path("www", PDF_WWW_SUBDIR))

    def _paths(self, account: str, invoice_id: str) -> tuple[Path, str]:
        account_slug = slugify(account)
        filename = f"invoice_{slugify(str(invoice_id))}.pdf"
        path = self._base_dir / account_slug / filename
        url = f"{LOCAL_URL_PREFIX}/{account_slug}/{filename}"
        return path, url

    async def async_ensure_downloaded(
        self,
        account: str,
        invoice: dict[str, Any],
        *,
        force: bool = False,
    ) -> Optional[dict[str, Any]]:
        """Make sure the invoice PDF exists locally; download it if needed.

        Returns a dict with local_path/local_url on success, or None when the
        invoice has no id/URL or the download failed (the next coordinator
        cycle retries because the file is still missing).
        """
        invoice_id = invoice.get("id")
        pdf_url = invoice.get("pdf")
        if not invoice_id or not pdf_url:
            return None

        path, url = self._paths(account, invoice_id)
        exists = await self._hass.async_add_executor_job(path.is_file)
        if exists and not force:
            return {"local_path": str(path), "local_url": url}

        try:
            session = async_get_clientsession(self._hass)
            async with session.get(pdf_url, timeout=DOWNLOAD_TIMEOUT) as resp:
                resp.raise_for_status()
                data = await resp.read()
            await self._hass.async_add_executor_job(_write_atomic, path, data)
        except (aiohttp.ClientError, OSError, TimeoutError) as err:
            _LOGGER.warning(
                "Failed to download invoice PDF for account %s (invoice %s): %s",
                account,
                invoice_id,
                err,
            )
            return None

        _LOGGER.debug(
            "Stored invoice PDF for account %s at %s (%d bytes)",
            account,
            path,
            len(data),
        )
        await self._hass.async_add_executor_job(
            self._cleanup_old_invoices, account, path.name
        )
        return {"local_path": str(path), "local_url": url}

    def _cleanup_old_invoices(self, account: str, keep_filename: str) -> None:
        """Remove superseded invoice PDFs for an account (best effort)."""
        account_dir = self._base_dir / slugify(account)
        try:
            for candidate in account_dir.glob("invoice_*.pdf"):
                if candidate.name != keep_filename:
                    candidate.unlink()
                    _LOGGER.debug("Removed superseded invoice PDF %s", candidate)
        except OSError:
            _LOGGER.debug(
                "Could not clean up old invoice PDFs for %s", account, exc_info=True
            )

    def ensure_base_dir(self) -> None:
        """Create the www subdirectory (blocking; call via executor).

        Home Assistant only serves /local/ when config/www existed at startup,
        so creating it early guarantees the URL works after the next restart
        at the latest.
        """
        self._base_dir.mkdir(parents=True, exist_ok=True)


def _write_atomic(path: Path, data: bytes) -> None:
    """Write file contents atomically (blocking; call via executor)."""
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = path.with_name(path.name + ".tmp")
    tmp_path.write_bytes(data)
    os.replace(tmp_path, path)
