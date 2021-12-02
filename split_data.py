from raw_data import all_data
from datetime import datetime

current_time = datetime.now().strftime("%d/%m, at %H:%M:%S")
current_day = datetime.today()

def split_data(initial_data, training_percentage):
    train_data = initial_data[ : int((len(initial_data)+1)*(training_percentage / 100))] 
    test_data = initial_data[int((len(initial_data)+1)*(training_percentage / 100)):] 
    return train_data, test_data

divided_data = split_data(all_data["all_data"], 80)

train_data = divided_data[0]
test_data = divided_data[1]

meta_data = {
    "all_data_length": all_data["initial_data_len"],
    "valid_data_length": len(all_data["all_data"]),
    "deleted_entries": all_data["deleted_entries"],
    "train_data_length": len(train_data),
    "Test data length": len(test_data),
    "Created on": current_time,
    "Amount of Categories": all_data["amount_of_categories"],
    "amount_of_values": all_data["amount_of_values"]
}

with open('data/train_data.py','w') as data:
    data.write(str(train_data))

with open('data/test_data.py','w') as data:
    data.write(str(test_data))

with open('data/meta_data.py','w') as data:
    data.write(str(meta_data))