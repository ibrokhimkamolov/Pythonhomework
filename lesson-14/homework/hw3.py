import requests
import json
from bs4 import BeautifulSoup

BASE_URL = "https://www.demoblaze.com/"
PRODUCTS_URL = "https://api.demoblaze.com/bycat"
DETAILS_URL = "https://api.demoblaze.com/view"

laptops = []
page = 0

while True:
    payload = {"cat": "notebook", "id": str(page)}
    res = requests.post(PRODUCTS_URL, json=payload)

    data = res.json()
    items = data.get("Items", [])

    if not items:
        break  # No more laptops

    for item in items:
        name = item["title"]
        price = item["price"]
        item_id = item["id"]

        # Get full description from details API
        detail_res = requests.post(DETAILS_URL, json={"id": item_id})
        detail_data = detail_res.json()
        description = BeautifulSoup(detail_data["desc"], "html.parser").text.strip()

        laptops.append({
            "name": name,
            "price": f"${price}",
            "description": description
        })

    page += 1

# Save to JSON file
with open("laptops.json", "w", encoding="utf-8") as f:
    json.dump(laptops, f, indent=2, ensure_ascii=False)

print(f"✅ Scraped {len(laptops)} laptops and saved to laptops.json")
