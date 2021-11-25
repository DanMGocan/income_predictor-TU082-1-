import csv
import random
from datetime import datetime
from helper_functions import int_to_category

csvPath = "data/data_set.csv"

current_time = datetime.now().strftime("%d/%m, at %H:%M:%S")
current_day = datetime.today()

# Function to convert the .csv document to a dictionary
def convert_data(initial_path):
    all_data = []
    deleted_entries = 0
    initial_data_len = 0

    with open(initial_path) as csvFile:
        csvReader = csv.DictReader(csvFile)
        for row in csvReader:

            # A counter to find out the initial length of the set
            initial_data_len += 1

            # Replacing the Outcome variable with either True or False (if over 50k or under)
            outcome = False
            if row["Outcome"] == " > 50 K":
                outcome = True

            # Will delete (and count) all entries which are having missing variables (listwise deletion)
            if " ? " in row.values():
                deleted_entries += 1
                continue
            
            # Function that converts [age], [capital_loss], [capital_gain]
            # and [hours_per_week] into categories. 
            int_to_category(row)

            # Creating a new dictionary from each entry in the .csv file, with the following modified:
            ## all integers have the correct data type (int from str)
            ## all white spaces in the str data types have been cleared
            ## capital loss has been added as a negative int
            ## outcome has been added as a boolean 

            new_dict = {
                "age": int(row["Age"]),
                "workclass": row["Workclass"].replace(" ", ""),
                "education_number": int(row["Education-number"]),
                "marital_status": row["Marital-status"].replace(" ", ""),
                "occupation": row["Occupation"].replace(" ", ""),
                "relationship": row["Relationship"].replace(" ", ""),
                "race": row["Race"].replace(" ", ""),
                "gender": row["Gender"].replace(" ", ""),
                "capital_gain": int(row["Capital-gain"]),
                "capital_loss": -(int(row["Capital-loss"])), 
                "hours_per_week": int(row["Hours-per-week"]),
                "outcome": outcome
            }

            all_data.append(new_dict)

    # Shuffling the data set every time the function is called
    random.shuffle(all_data)

    # Counting the amount of values for each key
    amount_of_values = {}
    for element in all_data:
        for key, value in element.items():
            if key in amount_of_values.keys():
                if value in amount_of_values[key].keys():
                    amount_of_values[key][value] += 1
                else:
                    amount_of_values[key][value] = 1
            else:
                amount_of_values[key] = {}

    # Counting the amount of individual categories in the data set
    amount_of_categories = {}
    for element in amount_of_values.keys():
        amount_of_categories[element] = len(amount_of_values[element].values())

    return_object = {
        "all_data": all_data,
        "deleted_entries": deleted_entries,
        "initial_data_len": initial_data_len,
        "amount_of_categories": amount_of_categories,
        "amount_of_values": amount_of_values
    }

    return return_object

# Function that will split the first xx% elements of the set in a training set and 
# a model testing set 
def split_data(initial_data, training_percentage):
    train_data = initial_data[ : int((len(initial_data)+1)*(training_percentage / 100))] 
    test_data = initial_data[int((len(initial_data)+1)*(training_percentage / 100)):] 
    return train_data, test_data

all_data = convert_data(csvPath)
divided_data = split_data(all_data["all_data"], 90)

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




