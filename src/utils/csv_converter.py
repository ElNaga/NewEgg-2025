import json
import csv
import os

def convert_json_to_csv(input_path="products_output.json", output_path="products_output.csv"):
    if not os.path.exists(input_path):
        print(f"[ERROR] JSON file not found → {input_path}")
        return

    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not data:
        print("[ERROR] No data inside JSON!")
        return

    headers = sorted(set().union(*(item.keys() for item in data)))

    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)

    print(f"[OK] CSV saved → {output_path}")
