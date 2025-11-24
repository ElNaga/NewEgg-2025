# category_scraper.py

from config import ITEM_RE, MAX_ITEMS
from http_client import safe_get
from realtime import fetch_realtime

def collect_item_numbers(category_id: str):
    all_items = set()

    for page in range(1, 999):
        url = f"https://www.newegg.com/p/pl?N={category_id}&PageSize=96&page={page}"
        print(f"[INFO] Fetching page {page}: {url}")

        r = safe_get(url)
        if not r or not getattr(r, "text", None):
            break

        page_items = set(ITEM_RE.findall(r.text))
        if not page_items:
            break

        new_items = page_items - all_items
        if not new_items:
            break

        all_items.update(new_items)

    return sorted(all_items)


def scrape_category(cat_name: str, cat_id: str, global_count: int):
    results = []

    item_numbers = collect_item_numbers(cat_id)
    if not item_numbers:
        return results, global_count

    for item_number in item_numbers:
        if global_count >= MAX_ITEMS:
            break

        info = fetch_realtime(item_number)
        if not info:
            continue

        info["item_number"] = item_number
        info["category"] = cat_name

        results.append(info)
        global_count += 1

        print(f"[OK] Fetched {item_number} → total={global_count}")

    return results, global_count
