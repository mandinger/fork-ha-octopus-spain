"""Constants for Octopus Energy Spain."""
from typing import Final

DOMAIN = "octopus_spain_fork"
CONF_EMAIL = "email"
CONF_PASSWORD = "password"
CONF_APIKEY = "apikey"
CONF_AUTH_TYPE: Final = "auth_type"
UPDATE_INTERVAL = 2
CONSUMPTION_IMPORT_DELAY_DAYS = 0
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
