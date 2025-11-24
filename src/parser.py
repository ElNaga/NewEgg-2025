# parser.py

def parse_realtime(data: dict) -> dict:
    item = data["MainItem"]

    image_name = item["Image"]["Normal"]["ImageName"]
    main_image = f"https://c1.neweggimages.com/ProductImageOriginal/{image_name}"

    description = (
        item["Description"]["LongDescription"]
        or item["Description"]["BulletDescription"]
        or item["Description"]["WebDescription"]
    )

    return {
        "title": item["Description"]["Title"],
        "price": item["FinalPrice"],
        "rating": item["Review"]["RatingOneDecimal"],
        "rating_count": item["Review"]["HumanRating"],
        "seller": item["Seller"]["SellerName"] or "Newegg",
        "main_image": main_image,
        "description": description,
    }
