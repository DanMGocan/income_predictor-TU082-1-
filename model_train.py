from csv_to_dict import train_data
import time

    # 'age': 33, 
    # 'workclass': 'Federal-gov',
    # 'education_number': 10,
    # 'marital_status': 'Divorced',
    # 'occupation': 'Other-service',
    # 'relationship': 'Not-in-family',
    # 'race': 'Black',
    # 'gender': 'Male',
    # 'capital_gain': 0,
    # 'capital_loss': 0,
    # 'hours_per_week': 40,
    # 'outcome': False

train_data_length = len(train_data)
tug_of_war = 0.5
print(train_data_length)

def find_unique_values(data):
    counter = 0
    unique_values = {
        "age": {},
        "workclass": {},
        "education_number": {},
        "marital_status": {},
        "occupation": {},
        "relationship": {},
        "race": {},
        "gender": {},
        "capital_gain": {},
        "capital_loss": {},
        "hours_per_week": {},
        "outcome": {}
    }
 
    for element in data:    
        outcome_state = element["outcome"]
        for key, value in element.items():
            unique_values[key][value] = {"True": 0, "False": 0}

            if value in unique_values[key].keys():
                #if outcome_state:
                unique_values[key][value][str(outcome_state)] += 1

            else:
                unique_values[key][value][str(outcome_state)] = 1

                         
        print(f"Model in training. Processing item {counter}.")
        time.sleep(0)
        counter += 1

    return unique_values

def find_min_max(data):
    pass

unique_values = find_unique_values(train_data)

with open('data/unique_data.py','w') as data:
    data.write(str(unique_values))

