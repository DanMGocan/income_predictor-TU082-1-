## Project made by Dan Gocan, for TU082 program, under the Technical University of Dublin, for Programming and Algorithms class. 

### To execute locally, download and run execute.py

### Description
The program takes a set of data (http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data) and builds a classifier using a simplified random forrest algorithm. The code is split in two folders, Data and Execution. All static
files are in the Data folder, being rewritten everytime the program is executed. The Execution folder holds all the
Python code that cleans, converts and processes the data. The results are written to an HTML page, that can be opened in any browser, or through GitHub pages (https://danmgocan.github.io/income_predictor-TU082-1-/). Results are recursively written as tables, using native Python code and the Bootstrap library for HTML. This part was not optimized as it is not core to the assignment. 

### Data flow
The initial set of data is stored locally as a .csv file. In order for the code to function, there are no network dependencies and the code can be executed on any machine with Python installed. 

1. In **/execution/raw_data.py**, the data is cleaned up and formatted. Numeric values are converted to bracket values, so instead of having 77 values for "Age", we now have only 7, which I think it allows a better analysis of the data available. The same process was applied to "Capital gains", "Capital loss" and "Hours worked per week". Once the conversion is complete, a new dictionary is created for every data entry and all information is stored in a list of dictionaries. **Everytime this module is invoked, the returned list is randomized, so the program will output different results each time.**

2. In **/execution/split_data.py**, we split the list of dictionaries in two lists - one to train the classifier, the other one to test it. The default value is 80% - 20% but this can be easily editable by changing the second argument when calling `split_data` function. The module returns two lists, one with training data, the other one with test data and both lists are also written to .py documents, in /data/ folder. The meta_data variable is calculated in this module too

##### Sample from train_data.py #####
```
{
    'age': '25-34 years old',
    'workclass': 'Private',
    'education_number': 14,
    'marital_status': 'Married-civ-spouse',
    'occupation': 'Tech-support',
    'relationship': 'Husband',
    'race': 'White',
    'gender': 'Male',
    'capital_gain': 'Capital gain 0',
    'capital_loss': 'Capital loss 0',
    'hours_per_week': 'Hours per week under 24.75',
    'outcome': False
}
```

##### Sample from meta_data.py #####
```
{
    'age': {
            '65 and over': 975,
            '55-54 years old': 2849,
            '25-34 years old': 8040,
            '18-24 years old': 4541,
            'Under 18': 328,
            '35-44 years old': 7807,
            '45-54 years old': 5621
        },
        'workclass': {
            'Local-gov': 2067,
            'Private': 22285,
            'Self-emp-not-inc': 2499,
            'Federal-gov': 943,
            'State-gov': 1279,
            'Self-emp-inc': 1074,
            'Without-pay': 14
        },
        'education_number': {
            9: 9840,
            12: 1008,
            4: 557,
            10: 6678,
            6: 820,
            13: 5044,
            8: 377,
            14: 1626,
            16: 375,
            3: 288,
            5: 455,
            11: 1307,
            7: 1048,
            2: 151,
            1: 45,
            15: 542
        },
        'marital_status': {
            'Widowed': 827,
            'Divorced': 4214,
            'Never-married': 9726,
            'Married-civ-spouse': 14064,
            'Separated': 939,
            'Married-spouse-absent': 370,
            'Married-AF-spouse': 21
        }
}
```

3. In **/execution/model_train.py** we create a new empty dictionaries of dictionaries to accommodate the average success rate for every attribute of every category. This is exported as the `unique_values` dictionary and also written to the /data/ folder. 

##### Sample from cart_values.py #####
```
{
    'workclass': {
        'Private': {
            'True': 3913,
            'False': 13934,
            'Averages': {
                'true_probability': 21.93,
                'false_probability': 78.07
            }
        },
        'Local-gov': {
            'True': 486,
            'False': 1162,
            'Averages': {
                'true_probability': 29.49,
                'false_probability': 70.51
            }
        },
        'Self-emp-not-inc': {
            'True': 563,
            'False': 1420,
            'Averages': {
                'true_probability': 28.39,
                'false_probability': 71.61
            }
        },
        'Federal-gov': {
            'True': 280,
            'False': 469,
            'Averages': {
                'true_probability': 37.38,
                'false_probability': 62.62
            }
        }
}
```

4. In **execution/model_test.py** we compare the average success rate of every data entry (based on the amount of "successful" atributes vs. "unsuccessful" attribute) and if the actual success rate is similar with the predicted value, then we register this comparison as a success for the classifier. We compare every data entry in the test_data list and find the amount of correct vs. wrong prediction. The test results are written to the /data/test_results.py file, as dictionaries. 

##### Sample from test_results.py #####
```
{
    'age': '45-54 years old',
    'workclass': 'Private',
    'education_number': 9,
    'marital_status': 'Married-civ-spouse',
    'occupation': 'Craft-repair',
    'relationship': 'Husband',
    'race': 'Black',
    'gender': 'Male',
    'capital_gain': 'Capital gain 0',
    'capital_loss': 'Capital loss 0',
    'hours_per_week': 'Hours per week under 49.5',
    'outcome': False,
    'true_probability': 28,
    'false_probability': 81,
    'test_outcome': False
}
```

5. In **execution/data_to_html.py** all the gathered information is being written in tables and an `index.html` file is returned. This file has all the results and necessary information


### Notes

By successful or unsuccessful, we measure if the data entry has an income that is higher than 50k per year. 

Using `time` module, I have taken measurements at vital points in the program, to measure its performance in seconds. We observe that the most consuming part in terms of resources is converting and clearing the data. This is due to successive `for` loops. 

Persoal opinion about data interpretation can be found at the end of the index.html document. 