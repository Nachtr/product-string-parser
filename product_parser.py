# considering importing RE or BeautifulSoup if I want to expand this idea further
from dataclasses import replace
import json # To make our dictionary look nice

# let's create a list that has some sample product information:
listings = [
    "Apple iPhone 13 (128GB) - $999",
    "Samsung Galaxy S22 Ultra, 256GB - Starting at $1188",
    "Google Pixel 6 Pro - 512GB @ $890",
    "Oneplus 13 (512GB) - $1300",
    "Oppo N3 256GB @ $2000"
]

def parse_product_listings(listings):
    product_listings = {}  # Create the dictionary to store extracted info

    for product in listings:
        if "Starting at" in product:  # Handle "Starting at" separately first
            parts = product.split(" Starting at ")
            product_name = parts[0].rstrip(" -")
            price_str = parts[-1].split()[-1].replace("$", "").strip()

        elif "-" in product:  # If the listing uses hyphen
            parts = product.split(" - ")
            product_name = parts[0].rstrip(" -")
            price_str = parts[-1].split()[-1].replace("$", "").strip()

        elif "," in product:  # If the listing uses a comma
            parts = product.split(", ")
            product_name = parts[0].rstrip(" -")
            price_str = parts[-1].split()[-1].replace("$", "").strip()

        elif "@" in product:  # If the listing uses "@"
            parts = product.split(" @ ")
            product_name = parts[0].rstrip(" -")
            price_str = parts[-1].replace("$", "").strip()

        else:  # Handle any other unrecognized formats
            print(f"Skipping unrecognized format: {product}")
            continue

        try:
            price = float(price_str)  # Convert extracted price to float
            product_listings[product_name] = price  # Store in dictionary
        except ValueError:
            print(f"Error converting price for: {product_name} - Raw Price: {price_str}")
            continue  # Skip faulty price conversions
    return product_listings

parsed_data = parse_product_listings(listings)
print(json.dumps(parsed_data, indent=4))