# config.py

import re
import tls_client

BASE_HEADERS = {
    "accept": "text/html,application/json, text/plain, */*",
    "accept-language": "en-US,en;q=0.9",
    "origin": "https://www.newegg.com",
    "referer": "https://www.newegg.com/",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0 Safari/537.36"
    ),
}

CATEGORIES = {
    "cpu": "100006676",
    "gpu": "100006662",
    "motherboard": "100006654",
    "ram": "100006650",
    "case": "100006644",
    "psu": "100006656",
    "cooling": "100006648",
    "barebone": "100006668",
    "server_components": "101714293",
    "sound_card": "100161254"
}

MAX_ITEMS = 500

ITEM_RE = re.compile(r'"ItemNumber"\s*:\s*"([^"]+)"')

SESSION = tls_client.Session(
    client_identifier="chrome_120",
    random_tls_extension_order=True
)
