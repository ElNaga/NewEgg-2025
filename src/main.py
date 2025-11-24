# main.py

import json
from config import CATEGORIES, MAX_ITEMS
from category_scraper import scrape_category
from utils.csv_converter import convert_json_to_csv


def scrape_newegg():
    all_products = []
    global_count = 0

    for cat_name, cat_id in CATEGORIES.items():
        if global_count >= MAX_ITEMS:
            break

        cat_products, global_count = scrape_category(
            cat_name, cat_id, global_count
        )
        all_products.extend(cat_products)

    print(f"\n[FINISHED] Total collected: {global_count}")

    with open("products_output.json", "w", encoding="utf-8") as f:
        json.dump(all_products, f, indent=2, ensure_ascii=False)

    convert_json_to_csv()


if __name__ == "__main__":
    scrape_newegg()
