from execution.split_data import train_data # Importing just the train_data list of dictionaries
import time

train_data_length = len(train_data)

# A function that will count what is the probability of any data entry to have an income over 50k (a True value)
# based on the occurrence of certain atributes and how are these influencing their success. 
def find_unique_values(data):
    counter = 0

    # Unique values dictionary will hold the attributes in each category and their success rate
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
             
    # Calculating the occurrence of each entry and increment the True or False values
    # depending if the 
    for element in data:    
        outcome_state = str(element["outcome"])
        for key, value in element.items():
            try:
                unique_values[key][value][outcome_state] += 1 # For example, unique_values["Workclass"]["Private"]["True"] will be incremented by 1, or if False, then unique_values["Workclass"]["Private"]["False"] will be incremented.
                # we are trying to find out how many True (>50k) and False (<50k) values are present for each attribute (age, workclass, gender, etc)
            except KeyError: # If the combination of category and attribute does not have a True / False value yet, it will be added here. 
               unique_values[key][value] = {"True": 0, "False": 0}
                         
        counter += 1

    # For loop to calculate in percentages, how many data entries with a given attribute have an income of over 50k and how many an income under 50k. 
    unique_values_keys = unique_values.keys()
    for element in unique_values_keys:
        for key in unique_values[element].keys():

            amount_of_true = unique_values[element][key]["True"]
            amount_of_false = unique_values[element][key]["False"]
            amount_in_total = amount_of_true + amount_of_false

            truth_average = 0
            false_average = 0
            
            if amount_of_true > amount_of_false:
                truth_average = (amount_of_true / amount_in_total) * 100
                false_average = 100 - truth_average

            elif amount_of_false > amount_of_true:
                false_average = (amount_of_false / amount_in_total) * 100
                truth_average = 100 - false_average

            else:
                false_average = 50
                truth_average = 50

            unique_values[element][key]["Averages"] = {
                "true_probability": round(truth_average, 2),
                "false_probability": round(false_average, 2)
            }

    # The dictionary with all the average amounts and amount of "True" and "False" is returned
    return unique_values

t2 = time.perf_counter() # Creating another time stamp for future performance

# The dictionary is being assigned to unique_values variable
unique_values = find_unique_values(train_data)

# And, just to have it, the data is written to the cart_values.py document 
with open('data/cart_values.py','w') as data:
    data.write(str(unique_values))

