from execution.raw_data import all_data # Imports the clean and formated data
from datetime import datetime # Imports datetime module, as to properly note the time when the program is executed
import time # time module used to measure time wise performance

current_time = datetime.now().strftime("%d/%m, at %H:%M:%S")

# Function that divides the all_data list into a training and test set. The percentage can be
# modified by changing the second argument of the split_data function on line 16
def split_data(initial_data, training_percentage):
    train_data = initial_data[ : int((len(initial_data)+1)*(training_percentage / 100))] 
    test_data = initial_data[int((len(initial_data)+1)*(training_percentage / 100)):] 
    return train_data, test_data

t1 = time.perf_counter() # Counter to measure time performance

# Dividing data as assigning the two lists as a tuple
divided_data = split_data(all_data["all_data"], 80)

# Assigning the two tuples to variables, as lists of dictionaries
train_data = divided_data[0]
test_data = divided_data[1]

# Meta data, collected because it was there and the more information, the better.
meta_data = {
    "all_data_length": all_data["initial_data_len"],
    "valid_data_length": len(all_data["all_data"]),
    "deleted_entries": all_data["deleted_entries"],
    "train_data_length": len(train_data),
    "test_data_length": len(test_data),
    "created_on": current_time,
    "amount_of_categories": all_data["amount_of_categories"],
    "amount_of_values": all_data["amount_of_values"]
}

# Writing all the information to .py documents, stored in /data/ folder. These documents are not used 
# later in the program but written to help us keep track of how our data looks.
with open('data/train_data.py','w') as data:
    data.write(str(train_data))

with open('data/test_data.py','w') as data:
    data.write(str(test_data))

with open('data/meta_data.py','w') as data:
    data.write(str(meta_data))