import requests
import csv
import json
from io import StringIO

# Prefer to define constants for the base URL and endpoint
BASE_URL = "https://coderbyte.com"
ENDPOINT = "/api/challenges/logs/user-info-csv"

full_url = BASE_URL + ENDPOINT

# Perform GET request
response = requests.get(full_url)

# Check if request was successful
if response.status_code == 200:
  csvfile = StringIO(response.text)
  reader = csv.reader(csvfile)
  header = next(reader)
  data_rows = list(reader)

  # Sort the data by the SECOND column (email)
  sorted_rows = sorted(data_rows, key=lambda r: r[1])

  # Convert sorted rows to a list of dictionaries
  list_json = [dict(zip(header, r)) for r in sorted_rows]

  # Convert to Json formatted string and print result
  output_json = json.dumps(list_json, indent=2)
  print(output_json)
else:
  print(f"Error: unable to get data. Status code: {response.status_code}")

print(response)