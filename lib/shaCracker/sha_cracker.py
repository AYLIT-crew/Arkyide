import hashlib
import csv
def brute_force_sha256(input_list, target_string):
    for item in input_list:
        # Compute SHA256 hash of the current item
        hashed_item = hashlib.sha256(item.encode()).hexdigest()
        
        # Compare the hashed item with the target string
        if hashed_item == target_string:
            return item  # Return the original item if the hash matches
    
    return None  # Return None if no match is found



passwords = []
with open('combo_list.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        new_row = row[0].split(",")
        new_row = new_row[1]
        passwords.append(new_row)


#Usage:
input_list = passwords
target_string = "0a34b9336e57472a87fd0fa911c9e6e75ac87249a7d6122f4ef5ecb3d88e04d" 

result = brute_force_sha256(input_list, hashlib.sha256("Tschaly1998".encode()).hexdigest())

if result:
    print(f"Match found: {result}")
else:
    print("No match found.")

