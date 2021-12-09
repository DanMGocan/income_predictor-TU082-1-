from split_data import train_data
import time

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
             
    # Calculating the occurrence of each entry
    for element in data:    
        outcome_state = str(element["outcome"])
        for key, value in element.items():
            try:
                unique_values[key][value][outcome_state] += 1
            except KeyError:
               unique_values[key][value] = {"True": 0, "False": 0}
                         
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
                "TRUE probability": round(truth_average, 2),
                "FALSE probability": round(false_average, 2)
            }

    return unique_values

t2 = time.perf_counter()
unique_values = find_unique_values(train_data)

with open('data/cart_values.py','w') as data:
    data.write(str(unique_values))

