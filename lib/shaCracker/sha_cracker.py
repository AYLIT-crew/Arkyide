import hashlib
import csv
from concurrent.futures import ThreadPoolExecutor

def hash_item(item):
  """Calculates the SHA256 hash of an item."""
  return hashlib.sha256(item.encode()).hexdigest()

def multithreaded_hashing(input_list):
  """Hashes items in the list using multiple threads."""
  with ThreadPoolExecutor() as executor:
    hashed_items = executor.map(hash_item, input_list)
  return list(hashed_items)

def brute_force_sha256(input_list, target_string):
    with ThreadPoolExecutor(max_workers=8) as executor:  # Define how many cores
        hashed_items = executor.map(
            lambda item: (item, hashlib.sha256(item.encode('utf-8')).hexdigest()),
            input_list)
    for item, hashed_item in hashed_items:
        if hashed_item == target_string:
            return item

    return None

passwords = []
with open('combo_list.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        new_row = row[0].split(",")
        new_row = new_row[1]
        passwords.append(new_row)


result = brute_force_sha256(passwords, hashlib.sha256("Tschaly1998".encode()).hexdigest())

if result:
    print(f"Match found: {result}")
else:
    print("No match found.")

