import json
import csv
import os

import json
import csv

def convert_json_to_csv():
    with open("products_output.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    fieldnames = [
        "Product Title",
        "Product Final Price",
        "Product Rating",
        "Seller Name",
        "Main Image URL",
        "Product Description",
    ]

    with open("products_output.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for p in data:
            writer.writerow({
                "Product Title": p.get("title", ""),
                "Product Final Price": p.get("price", ""),
                "Product Rating": p.get("rating", ""),
                "Seller Name": p.get("seller", ""),
                "Main Image URL": p.get("main_image", ""),
                "Product Description": p.get("description", ""),
            })

