from raw_data import train_data
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

def find_unique_values(data):
    '''To not forget to add DOCSTRING'''
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
 
    # Adding empty dictionaries to each entry
    for element in data:   
        for key, value in element.items():
            unique_values[key][value] = {"True": 0, "False": 0}
            
    # Calculating the occurrence of each entry
    for element in data:    
        outcome_state = str(element["outcome"])

        for key, value in element.items():
            unique_values[key][value][outcome_state] += 1
                         
        print(f"Populating data. Processing item {counter}.")
        time.sleep(0)
        counter += 1

    # For loop to calculate the tug-of-war value for each property
    unique_values_keys = unique_values.keys()
    for element in unique_values_keys:
        for key in unique_values[element].keys():
            amount_true = unique_values[element][key]["True"]
            amount_false = unique_values[element][key]["False"]
            amount_total = amount_true + amount_false
            truth_average = 0
            false_average = 0
            
            if amount_true > amount_false:
                truth_average = (amount_true / amount_total) * 100
                false_average = 100 - truth_average

            elif amount_false > amount_true:
                false_average = (amount_false / amount_total) * 100
                truth_average = 100 - false_average

            else:
                false_average = 50
                truth_average = 50

            unique_values[element][key]["Averages"] = {
                "truth_average": round(truth_average, 2),
                "false_average": round(false_average, 2)
            }

    return unique_values

unique_values = find_unique_values(train_data)

with open('data/unique_data.py','w') as data:
    data.write(str(unique_values))

