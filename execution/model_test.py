from execution.model_train import unique_values
from execution.split_data import test_data # Importing the data test set, which hasn't been used to train the classifier and 
                                           # comparing it against the unique_values dictionary values
import time

def test_model(probabilities, test_data):
    test_results = []

    # Declaring two counters to measure the amount of correct and wrong results
    correct = 0
    wrong = 0

    for element in test_data:

        length_of_data = len(element.keys()) - 1
        true_probability = 0
        false_probability = 0

        # Add all the average success rates
        for key, value in element.items():
            try:
                true_probability += probabilities[key][value]["Averages"]["true_probability"]
                false_probability += probabilities[key][value]["Averages"]["false_probability"]
            except KeyError:
                continue
            
        # Divide the total averages by the lenght of the data
        element["true_probability"] = round(true_probability  / length_of_data)
        element["false_probability"] = round(false_probability / length_of_data)
        
        # Count if the true probability is higher than the true probability and assign a 
        # test outcome to it, according to that
        if element["true_probability"] >= element["false_probability"]:
            element["test_outcome"] = True
        else:
            element["test_outcome"] = False
        
        # Count if the assigned test result is equal with the actual value and if so
        # append the correct and wrong variable as needed
        if element["outcome"] == element["test_outcome"]:
            correct += 1
        else:
            wrong += 1

        test_results.append(element)

    percentage = f"{round(correct / (correct + wrong) * 100, 3)}%"
    return test_results, correct, wrong, percentage

t3 = time.perf_counter()

result = test_model(unique_values, test_data)

with open('data/test_results.py','w') as data:
    data.write(str(result[0]))

