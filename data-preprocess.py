

import csv
import json

candy_rows = {}

with open('Raw_Data/sour-candy-data.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['What Candy Are you sampling?'] not in candy_rows:
            candy_rows[row['What Candy Are you sampling?']] = []
        candy_rows[row['What Candy Are you sampling?']].append(row)


print(json.dumps(candy_rows, indent = 4))

for candy_name in candy_rows:
    with open(f'Processed_Data/{candy_name}.csv', 'w+', newline='') as csvfile:
        fieldnames = list(candy_rows[candy_name][0].keys())
        fieldnames.remove("Your Name")
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in candy_rows[candy_name]:
            del row["Your Name"]
            writer.writerow(row)

