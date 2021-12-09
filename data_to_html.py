
from split_data import meta_data, test_data, train_data
from model_test import result
import random

def meta_data_to_html_table(data):
    string = f'''
    <section class="col-4 my-4 py-4">
    <h4 class="p-0 m-0">Table with the available meta data</h4>
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
    '''

    string2 = ""
    
    for key, value in data.items():
            if key not in ["all_data_length", "valid_data_length", "deleted_entries", "train_data_length", "test_data_length", "created_on", "amount_of_categories"]:
                for parent_key, child_value in value.items():
                    for parent_key_2, child_value_2 in child_value.items():
                        string2 += f'''
                        <tr>
                            <th scope="row">{parent_key_2}</th>
                            <td>{child_value_2}</td>
                        </tr>
                        '''

    return string + "</table></section>"

def test_results_to_html_table(data):
    string = f'''

    '''

def dict_to_html_table(data, sample_size, data_type):
    random_value = random.randint(0, len(data))
    entry_counter = 1
    string = f'''
    <section>
        <h4 class="p-0 m-0">Table with {sample_size} data entries, from {data_type} pool</h4>
        <small><strong>Only a small set of data has been written to the HTML file. All data is available in the source code available on GitHub, at <a href="https://www.google.com" target="_blank">https://github.com/DanMGocan/income_predictor-TU082-1-</strong></a></small>
            
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

training_data_table = dict_to_html_table(train_data, 25, "training data")
meta_data_table = meta_data_to_html_table(meta_data)

def html(correct, wrong):
    percentage = correct / (correct + wrong)
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
            <body class="mx-auto col-10">

                {meta_data_table}
                <br>
                {training_data_table}

                <!-- Optional JavaScript; choose one of the two! -->

                <!-- Option 1: Bootstrap Bundle with Popper -->
                <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>

                <!-- Option 2: Separate Popper and Bootstrap JS -->
                <!--
                <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.10.2/dist/umd/popper.min.js" integrity="sha384-7+zCNj/IqJ95wo16oMtfsKbZ9ccEh31eOz1HGyDuCQ6wgnyJNSYdrPa03rtR1zdB" crossorigin="anonymous"></script>
                <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.min.js" integrity="sha384-QJHtvGhmr9XOIpI6YVutG+2QOK9T+ZnN4kzFN1RtK3zEFEIsxhlmWl5/YESvpZ13" crossorigin="anonymous"></script>
                -->
            </body>
        </html>
    '''

html_result = html(result[1], result[2])

#  <h1>Classifier success rate:</h1>
#                 <p>Correct results: {correct}</p>
#                 <p>Wrong results: {wrong}</p>
#                 <p>Success percentage: {round(percentage * 100, 2)}</p>
#                 <p>Test ran on: {meta_data["Created on"]}</p>
