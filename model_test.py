import time
from model_train import unique_values
from split_data import test_data



def test_model(probabilities, test_data):
    test_results = []
    correct = 0
    wrong = 0
    for element in test_data:

        length_of_data = len(element.keys()) - 1
        true_probability = 0
        false_probability = 0

        for key, value in element.items():
            try:
                true_probability += probabilities[key][value]["Averages"]["TRUE probability"]
                false_probability += probabilities[key][value]["Averages"]["FALSE probability"]
            except KeyError:
                continue
            
        element["True prob"] = round(true_probability  / length_of_data)
        element["False prob"] = round(false_probability / length_of_data)
        
        if element["True prob"] >= element["False prob"]:
            element["TEST Outcome"] = True
        else:
            element["TEST Outcome"] = False
        
        if element["outcome"] == element["TEST Outcome"]:
            correct += 1
        else:
            wrong += 1

        test_results.append(element)

    percentage = correct / (correct + wrong)
    return test_results, correct, wrong, percentage

t3 = time.perf_counter()
result = test_model(unique_values, test_data)
with open('data/test_results.py','w') as data:
    data.write(str(result))

