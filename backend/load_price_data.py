# Run ONCE to import price paid data into MongoDB
from dotenv import load_dotenv
load_dotenv()

import csv
from app import create_app
from app.extensions import db

FIELDS = ["id","price","date","postcode","property_type",
          "new_build","tenure","paon","saon","street",
          "locality","town","district","county","ppd","status"]

app = create_app()
with app.app_context():
    collection = db().price_paid
    collection.drop()  # fresh load

    batch, total = [], 0
    with open("priced-paid-data-2025.txt", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) < 16:
                continue
            doc = dict(zip(FIELDS, row))
            doc["price"] = int(doc["price"])
            doc["postcode_clean"] = doc["postcode"].replace(" ", "").upper()
            batch.append(doc)
            if len(batch) >= 1000:
                collection.insert_many(batch)
                total += len(batch)
                batch = []
                print(f"Loaded {total}...", end="\r")

    if batch:
        collection.insert_many(batch)
        total += len(batch)

    # Index for fast postcode lookups
    collection.create_index("postcode_clean")
    collection.create_index("postcode")
    print(f"\n✅ Loaded {total} records into MongoDB")