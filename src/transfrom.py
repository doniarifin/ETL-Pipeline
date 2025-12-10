def transfrom_data(data_list):
    transformed = []
    print("Starting data transformation...")

    for item in data_list:
        price_str = item["price"].replace("Â£", "£").replace("£", "").strip()
        # convert to IDR
        price_value = float(price_str) * 22203.45

        rating_map = {
            "One": 1,
            "Two": 2,
            "Three": 3,
            "Four": 4,
            "Five": 5
        }
        rating_value = rating_map.get(item["rating"], 0)

        transformed.append({
            "title": item["title"].strip(),
            "rating": rating_value,
            "price": price_value
        })

    print("Transfrom data success")
    return transformed
