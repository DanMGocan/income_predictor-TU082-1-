# This module takes all the data available in the document and translates everything into
# an HTML document, formatted with Bootstrap. The html code has not been properly refactored
# and there are parts of it that could have been written better. However, what matters most
# is that is functional, even if not ideal. 

# Time imports, to measure execution time 
from execution.raw_data import t0 # Time before execution
from execution.split_data import meta_data, train_data, t1 # Time before splitting the data
from execution.model_train import unique_values, t2 # Time before training the model
from execution.model_test import result, t3 # Time before testing the model

import random
import time

t4 = time.perf_counter() # Another time stamp to measure time performance

############################################################################
# Functions that convert available data in html tables, by recursively #####
# building strings. Every function creates a new <section> and all these ###
# sections are at the end, merged into one string, that is then returned ###
# and written to index.html by the execute.py document #####################
############################################################################

def meta_data_to_html_table(data):
    return f'''
    <section class="container col-10">
        <h4>Table with the available meta data</h4>
            <table class="table table-sm table-striped ">
                <tr>
                    <th scope="row">Executed on:</th>
                    <td>{data["created_on"]}</td>
                <tr>
                <tr>
                    <th scope="row">Initial amount of data entries:</th>
                    <td>{data["all_data_length"]}</td>
                <tr>
                <tr>
                    <th scope="row">Valid data entries:</th>
                    <td>{data["valid_data_length"]}</td>
                <tr>
                <tr>
                    <th scope="row">Deleted data entries:</th>
                    <td>{data["deleted_entries"]} <small>(Listwise deletion)</small>
                <tr>
                <tr>
                    <th scope="row">Length of training data set:</th>
                    <td>{data["train_data_length"]}</td>
                <tr>
                <tr>
                    <th scope="row">Length of test data set:</th>
                    <td>{data["test_data_length"]}</td>
                <tr>
            </table>
            
            <table class="table table-sm table-striped "
                <tr>
                    <th scope="row">Amount of correct predictions:</th>
                    <td class="text-success">{result[1]}</td>
                </tr>
                <tr>
                    <th scope="row">Amount of wrong predictions:</th>
                    <td class="text-danger">{result[2]}</td>
                </tr>
                <tr>
                    <th scope="row" class="fs-4">Classifier success rate:</th>
                    <td class="text-secondary fs-4">{result[3]}</td>
                </tr>
            </table>
    </section>
    '''

def meta_categories_to_html(data):
    string = f'''
    <section class="container col-10">
        <h4>Tables with the amount of individual values, for each category</h4>
        '''
    str_to_add = ""
    for key, value in data["amount_of_values"].items():
            str_to_add += f'''

                <table class="table table-sm table-striped">
                    <th scope="row" class="mt-4">{key.replace("_", " ").title()}</th>
                    <th scope="row"># of members</th>
                    <th scope="row">Success rate</th>
                    <th scope="row">Failure rate</th>
                    '''
            for parent_key, child_value in value.items():
                    
                    try:
                        true_prob = unique_values[key][parent_key]["Averages"]["true_probability"]
                        false_prob = unique_values[key][parent_key]["Averages"]["false_probability"]
                    except KeyError:
                        continue

                    str_to_add += f'''
                    <tr>
                        <td>{parent_key}</td>
                        <td>{child_value}</td>
                        <td>{true_prob}%</td>
                        <td>{false_prob}%</td>
                    </tr> 
                    '''
 
    string += str_to_add
    return string + "</table></section>"

def time_performance_to_table():
    return f'''
    <section class="container col-10">
    <h4>Table with the execution times</h4>
    <table class="table table-sm table-striped">
        <tr>
            <th scope="col">To initialize, clean and convert data:</th>
            <td>{round(t1 - t0, 3)} seconds</td>
        </tr>
        <tr>
            <th scope="col">To split the data:</th>
            <td>{round(t2 - t1, 3)} seconds</td>
        </tr>
        <tr>
            <th scope="col">To train the model (performing analysis on {meta_data["train_data_length"]}) data entries:</th>
            <td>{round(t3 - t2, 3)} seconds</td>
        </tr>
        <tr>
            <th scope="col">To test the model (performing analysis on {meta_data["test_data_length"]}) data entries:</th>
            <td>{round(t4 - t3, 3)} seconds</td>
        </tr>
        <PLACEHOLDER_FOR_TOTAL_EXEC_TIME>
    </table>
    </section>
    '''

# Please note that this function returns a random sample set of 50 elements ([from_random_value:random_value+50])
def dict_to_html_table(data, sample_size):
    random_value = random.randint(0, len(data))
    entry_counter = 1
    string = f'''
    <section class="container col-12">
        <h4>Table with {sample_size} data entries, from training data pool</h4>
        <small><strong>Only a small set of data has been written to the HTML file. All data is available in the source code available on GitHub, at <a href="https://github.com/DanMGocan/income_predictor-TU082-1-" target="_blank">https://github.com/DanMGocan/income_predictor-TU082-1-</strong></a></small>
            
            <table class="table table-sm table-striped">
                <tr>
                    <th scope="col">Entry #</th>
                    <th scope="col">Age</th>
                    <th scope="col">Workclass</th>
                    <th scope="col">Education Level</th>
                    <th scope="col">Marital Status</th>
                    <th scope="col">Occupation</th>
                    <th scope="col">Relationship</th>
                    <th scope="col">Race</th>
                    <th scope="col">Gender</th>
                    <th scope="col">Capital Gain</th>
                    <th scope="col">Capital Loss</th>
                    <th scope="col">Hours Worked Per Week</th>
                    <th scope="col">Earnings over 50k</th>
                </tr>
    '''
    for element in data[random_value : random_value + sample_size]:
        string += f'''
            <tr>
                <th scope="row">{entry_counter}</td>
                <td >{element["age"]}</td>
                <td >{element["workclass"]}</td>
                <td >{element["education_number"]}</td>
                <td >{element["marital_status"]}</td>
                <td >{element["occupation"]}</td>
                <td>{element["relationship"]}</td>
                <td >{element["race"]}</td>
                <td >{element["gender"]}</td>
                <td >{element["capital_gain"]}</td>
                <td >{element["capital_loss"]}</td>
                <td >{element["hours_per_week"]}</td>
                <td >{element["outcome"]}</td>
            </tr>
            '''
        entry_counter += 1
    return string + "</table></section>"

###########################################################################
###########################################################################


# In order to initialize the amount of data entries presented, change the value for this function from 50
# to your prefered value
training_data_table = dict_to_html_table(train_data, 50)

meta_data_table = meta_data_to_html_table(meta_data)
meta_categories = meta_categories_to_html(meta_data)
time_performance_table = time_performance_to_table()

# The main function that deliver the final string, to execute.py
def html():
    return f'''
    <!doctype html>
        <html lang="en">
            <head>
                <!-- Required meta tags -->
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1">

                <!-- Bootstrap CSS -->
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">

                <title>TU Classifier, results</title>
            </head>
            <body class="mx-auto container">
                <div class="py-4"></div>
                {meta_data_table}
                <br>
                <div class="py-4"></div>
                {time_performance_table}
                <br>
                <div class="py-4"></div>
                {meta_categories}
                <br>
                <div class="py-4"></div>
                {training_data_table}
                <br>
                <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>

            </body>
        </html>
    ''', time.perf_counter() # This function also returns, at the end, the final time stamp. 


