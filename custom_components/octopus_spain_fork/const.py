"""Constants for Octopus Energy Spain."""
from typing import Final

DOMAIN = "octopus_spain_fork"
CONF_EMAIL = "email"
CONF_PASSWORD = "password"
CONF_APIKEY = "apikey"
CONF_AUTH_TYPE: Final = "auth_type"
# List of Octopus account numbers the user chose to load entities for. When
# missing or empty, every discovered account is loaded (backward compatible).
CONF_ACCOUNTS: Final = "accounts"
UPDATE_INTERVAL = 2
CONSUMPTION_IMPORT_DELAY_DAYS = 0
# The statistics importer reconstructs a rolling window that normally starts at
# the first of the current month. Distributor readings land 1-3 days late, so on
# the 1st the tail of the previous month is still unpublished; without a
# catch-up the window would move on and those days would never be imported
# again. During the first CONSUMPTION_CATCHUP_DAYS days of a month the window is
# extended back into the previous month so late data still gets picked up.
CONSUMPTION_CATCHUP_DAYS: Final = 7
# How much hourly history to import when the statistic series is empty
# (fresh install). Existing series are never backfilled: inserting rows
# below an existing cumulative-sum series would corrupt the sums.
STATISTICS_BACKFILL_DAYS = 365
STATISTICS_BACKFILL_CHUNK_DAYS = 30
AUTH_OPTIONS: Final = ["username/password", "apikey"]

SERVICE_DOWNLOAD_INVOICE: Final = "download_invoice"
ATTR_ACCOUNT: Final = "account"
# Invoice PDFs are stored under config/www so they get a durable URL that,
# unlike the presigned S3 links from the API, never expires.
PDF_WWW_SUBDIR: Final = DOMAIN
LOCAL_URL_PREFIX: Final = f"/local/{DOMAIN}"
STAT_PREFIX_EXPORT: Final = "energy_export"
