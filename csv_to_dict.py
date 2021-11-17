
import csv
import random

csvPath = "data/data_set.csv"
dict_path = "data/data_set.py"

def convert_data(initial_path):
    all_data = []
    over_50 = 0
    under_50 = 0
    with open(initial_path) as csvFile:
        csvReader = csv.DictReader(csvFile)
        for row in csvReader:
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
                "outcome": row["Outcome"]
            }
            if new_dict["outcome"] == " > 50 K":
                over_50 += 1
            else:
                under_50 += 1

            all_data.append(new_dict)
    
    with open('dict_data.py','a') as data:
        data.write(str(all_data))



    random.shuffle(all_data)
    print(over_50)
    print(under_50)
    print(len(all_data))
    return all_data


def split_data(initial_data, training_percentage):
    train_data = initial_data[:int((len(initial_data)+1)*(training_percentage / 100))] 
    test_data = initial_data[int((len(initial_data)+1)*(training_percentage / 100)):] 
    return train_data, test_data

all_data = convert_data(csvPath)
train_data = split_data(all_data, 80)[0]
test_data = split_data(all_data, 80)[1]

for i in range(0, 4):
    print(train_data[i])
    print(test_data[i])





