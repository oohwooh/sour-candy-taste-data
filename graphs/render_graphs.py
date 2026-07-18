import os
import csv
from radar import radar


PROCESSED_DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'Processed_Data')

candy_data = {}

for filename in os.listdir(PROCESSED_DATA_DIR):
    if not filename.endswith('.csv'):
        continue

    candy_name = filename[:-len('.csv')]
    filepath = os.path.join(PROCESSED_DATA_DIR, filename)

    with open(filepath, newline='') as f:
        reader = csv.DictReader(f)
        candy_data[candy_name] = list(reader)

radar(candy_data, "Sour Patch Kids Strips").show()
