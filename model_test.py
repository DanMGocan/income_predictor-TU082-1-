from model_train import unique_values
from raw_data import test_data

initial_over = 0
initial_under = 0

for element in test_data:
    element["Tug-of-War"] = 0
    if element["outcome"] == True:
        initial_over += 1
    elif element["outcome"] == False:
        initial_under += 1

print(initial_over, initial_under)

correct_values = 0
wrong_values = 0

keys_to_test = ["workclass", "education_number", "marital_status", "occupation", "relationship", "gender"]

for element in test_data:
    for key, value in element.items():
        pass