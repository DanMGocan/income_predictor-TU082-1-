import random
from model_train import unique_values as unique_values
from split_data import test_data as test_data
from data_to_html import html_result
from data import meta_data
from datetime import datetime

current_time = datetime.now().strftime("%d/%m, at %H:%M:%S")
current_day = datetime.today()


test_results = []

def test_model(probabilities, test_data):
    correct = 0
    wrong = 0
    for element in test_data:

        length_of_data = len(element.keys()) - 1
        true_probability = 0
        false_probability = 0

        for key, value in element.items():
            true_probability += probabilities[key][value]["Averages"]["TRUE probability"]
            false_probability += probabilities[key][value]["Averages"]["FALSE probability"]
        
        random_factor = random.randint(0, 100)

        element["True prob"] = round(true_probability  / length_of_data)
        element["False prob"] = round(false_probability / length_of_data)
        
        if random_factor <= element["True prob"]:
            element["TEST Outcome"] = True
        else:
            element["TEST Outcome"] = False
        
        if element["outcome"] == element["TEST Outcome"]:
            correct += 1
        else:
            wrong += 1


        test_results.append(element)
        #print(true_probability / length_of_data, false_probability / length_of_data)

    percentage = correct / (correct + wrong)
    return test_results, correct, wrong, percentage


# final = html_result(result[1], result[2])

# f'''
# # There were {result[1]} correct results and {result[2]} wrong results.
# # The final success rate is {round((result[1] / (result[1] + result[2]) * 100), 2)}.
# '''

# with open('data/test_results.py','w') as data:
#     data.write(str(result))

# with open('data/results.html','w') as data:
#     data.write(final)


#result = test_model(unique_values, test_data)

i = 0
while i < 10:
    try: 
        print(test_model(unique_values, test_data))
    except KeyError:
        print("lol")
    i += 1
    

