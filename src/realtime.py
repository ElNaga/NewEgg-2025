# realtime.py

import json
import time
import tls_client

from config import BASE_HEADERS
from parser import parse_realtime

def fetch_realtime(item_number: str):
    url = (
        "https://www.newegg.com/product/api/ProductRealtime"
        f"?ItemNumber={item_number}&CountryCode=USA"
    )

    session = tls_client.Session(
        client_identifier="chrome_120",
        random_tls_extension_order=True
    )

    try:
        r = session.get(url, headers=BASE_HEADERS)
        time.sleep(1.0)
    except Exception as e:
        print(f"[ERROR] Item {item_number} → {e}")
        return None

    if not r or r.status_code != 200:
        print(f"[ERROR] Failed realtime fetch {item_number}, code={r.status_code}")
        return None

    try:
        data = json.loads(r.text)
        return parse_realtime(data)
    except Exception:
        print(f"[ERROR] JSON fail for {item_number}")
        return None
