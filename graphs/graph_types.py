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


if __name__ == '__main__':
  for candy in candy_data:
    print(candy)
    for response in candy_data[candy]:
      graph_idea = response['What type of graph do you think would best represent the flavor of this candy?']
      if graph_idea:
        print('-',graph_idea)