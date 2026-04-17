import csv
import os

DATA_DIRECTORY = "./data"
OUTPUT_FILE_PATH = "./new_data.csv"

with open(OUTPUT_FILE_PATH, "w") as output_file:
    writer = csv.writer(output_file)
    writer.writerow(["sales", "date", "region"])

    for file_name in os.listdir(DATA_DIRECTORY):
        with open(f"{DATA_DIRECTORY}/{file_name}", "r") as input_file:
            reader = csv.DictReader(input_file)
            for row in reader:
                if row["product"] == "pink morsel":
                    price = float(row["price"][1:])
                    sale = price * int(row["quantity"])
                    writer.writerow([sale, row["date"], row["region"]])
