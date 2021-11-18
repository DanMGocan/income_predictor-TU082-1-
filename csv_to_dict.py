import csv
import random

csvPath = "data/data_set.csv"

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
            
            new_dict = {
                "age": row["Age"],
                "workclass": row["Workclass"],
                "education_number": row["Education-number"],
                "marital_status": row["Marital-status"],
                "occupation": row["Occupation"],
                "relationship": row["Relationship"],
                "race": row["Race"],
                "gender": row["Gender"],
                "capital_gain": row["Capital-gain"],
                "capital_loss": row["Capital-loss"],
                "hours_per_week": row["Hours-per-week"],
                "outcome": outcome
            }

            all_data.append(new_dict)

    random.shuffle(all_data)

    return_object = {
        "all_data": all_data,
        "deleted_entries": deleted_entries,
        "initial_data_len": initial_data_len
    }

    return return_object

# Function that will split the first xx% elements of the set in a training set and 
# a model testing set 
def split_data(initial_data, training_percentage):
    train_data = initial_data[:int((len(initial_data)+1)*(training_percentage / 100))] 
    test_data = initial_data[int((len(initial_data)+1)*(training_percentage / 100)):] 
    return train_data, test_data

all_data = convert_data(csvPath)
train_data = split_data(all_data["all_data"], 50)[0]
test_data = split_data(all_data["all_data"], 50)[1]

meta_data = {
    "all_data_length": all_data["initial_data_len"],
    "valid_data_length": len(all_data["all_data"]),
    "deleted_entries": all_data["deleted_entries"],
    "train_data_length": len(train_data),
    "test_data": len(test_data)
}

with open('data/train_data.py','w') as data:
    data.write(str(train_data))

with open('data/test_data.py','w') as data:
    data.write(str(test_data))

with open('data/meta_data.py','w') as data:
    data.write(str(meta_data))




