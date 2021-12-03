import csv
import random
from datetime import datetime

csvPath = "data/data_set.csv"

# Function that converts [age] into brackets.
# To convert age to brackets we have used subjective
# values. 
def age_to_bracket(data):
    # Modify for age
    age = int(data["Age"])
    if age < 18:
        return "Under 18"
    elif age >= 18 and age <= 24:
        return "18-24 years old"
    elif age >= 25 and age <= 34:
        return "25-34 years old"
    elif age >= 35 and age <= 44:
        return "35-44 years old"
    elif age >= 45 and age <= 54:
        return "45-54 years old"
    elif age >= 55 and age <= 64:
        return "55-54 years old"
    else:
        return "65 and over"
    
# Function that converts [capital_loss], [capital_gain], [hours_per_week] into brackets.
# For this conversion we have taken the max of each category and,
# through splitting the averages, we have created 9 possible categories
def capital_to_bracket(data, value, type):
    if type == "capital_gain":
        capital = int(data["capital_gain"])
        wording = "Capital gain"
    elif type == "capital_loss":
        capital = int(data["capital_loss"])
        wording = "Capital loss"
    elif type == "hours_per_week":
        capital = int(data["hours_per_week"])
        wording = "Hours per week"

    if capital == 0:
        return f"{wording} 0"
    elif capital <= value / 8: 
        return f"{wording} under {value / 8}"
    elif capital <= value / 4: 
        return f"{wording} under {value / 4}"
    elif capital <= (value / 8 + value / 4):
        return f"{wording} under {((value / 8) + (value / 4))}"
    elif capital <= value / 2:
        return f"{wording} under {value / 2}"
    elif capital <= (value / 2 + value / 4):
        return f"{wording} under {value / 2 + value / 4}"
    elif capital <= (value / 2 + value / 4):
        return f"{wording} under {value / 2 + value / 4}"
    elif capital <= value - value / 8:
        return f"{wording} under {value - value / 8}"
    elif capital <= value:
        return f"{wording} under {value + 1}"
    else:
        return f"Error - capital gain is {capital} and the value is {value}"

# Function to convert the .csv document to a dictionary
def convert_data(initial_path):
    all_data = []

    # In order to have organic brackets for capital gain, loss and hours worked,
    # we are adding all the values to lists, and then finding the max. value of
    # each.
    all_capital_gain = []
    all_capital_loss = []
    all_hours_per_week = []

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

            # Creating a new dictionary from each entry in the .csv file, with the following modified:
            ## all integers have the correct data type (int from str)
            ## all white spaces in the str data types have been cleared
            ## capital loss has been added as a negative int
            ## outcome has been added as a boolean 

            new_dict = {
                "age": age_to_bracket(row),
                "workclass": row["Workclass"].replace(" ", ""),
                "education_number": int(row["Education-number"]),
                "marital_status": row["Marital-status"].replace(" ", ""),
                "occupation": row["Occupation"].replace(" ", ""),
                "relationship": row["Relationship"].replace(" ", ""),
                "race": row["Race"].replace(" ", ""),
                "gender": row["Gender"].replace(" ", ""),
                "capital_gain": int(row["Capital-gain"]),
                "capital_loss": int(row["Capital-loss"]), 
                "hours_per_week": int(row["Hours-per-week"]),
                "outcome": outcome
            }

            # In order to find the minimum and the maximum capital gains / losses
            # we append all the 
            all_capital_gain.append(int(row["Capital-gain"]))
            all_capital_loss.append(int(row["Capital-loss"]))
            all_hours_per_week.append(int(row["Hours-per-week"]))
            all_data.append(new_dict)

        max_capital = max(all_capital_gain)
        min_capital = max(all_capital_loss)
        max_hours = max(all_hours_per_week)

        # Overwriting the values in capital_gain / loss with the position in the brackets
        for element in all_data:
            element["capital_gain"] = capital_to_bracket(element, max_capital, "capital_gain")
            element["capital_loss"] = capital_to_bracket(element, min_capital, "capital_loss")
            element["hours_per_week"] = capital_to_bracket(element, max_hours, "hours_per_week" )

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

all_data = convert_data(csvPath)






