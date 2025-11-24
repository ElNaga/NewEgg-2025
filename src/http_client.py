# http_client.py

import time
from config import SESSION, BASE_HEADERS

def safe_get(url, headers=None):
    try:
        r = SESSION.get(url, headers=headers or BASE_HEADERS)
        time.sleep(1.0)
        return r
    except Exception as e:
        print(f"[WARN] Request error → {e}")
        return None
