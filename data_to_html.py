
from split_data import meta_data, test_data, train_data
from model_test import result

def dict_to_html_table(data):
    entry_counter = 1
    string = '''
        <table class="table mx-4 px-4">
            <tr>
                <th>Entry #</th>
                <th>Age</th>
                <th>Workclass</th>
                <th>Education Level</th>
                <th>Marital Status</th>
                <th>Occupation</th>
                <th>Relationship</th>
                <th>Race</th>
                <th>Gender</th>
                <th>Capital Gain</th>
                <th>Capital Loss</th>
                <th>Hours Worked Per Week</th>
                <th>Earnings over 50k</th>
            </tr>
    '''
    for element in data:
        string = string + f'''
            <tr class="py-0 my-0">
                <td >{entry_counter}</td>
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
    string += '''
        </table>
    '''

    return string

test_data_table = dict_to_html_table(train_data)

def html(correct, wrong, table1):
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
            <body>
                <h1>Classifier success rate:</h1>
                <p>Correct results: {correct}</p>
                <p>Wrong results: {wrong}</p>
                <p>Success percentage: {round(percentage * 100, 2)}</p>
                <p>Test ran on: {meta_data["Created on"]}</p>

                <h4>Table with Test data</h4>
                {table1}

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


    <!doctype html>
    <html lang="en">
    <head>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <link rel="stylesheet" href="/results.css">


        <title>TU Classifier, results</title>
    </head>
    <body>
        <h1>Classifier success rate:</h1>
        <p>Correct results: {correct}</p>
        <p>Wrong results: {wrong}</p>
        <p>Success percentage: {round(percentage * 100, 2)}</p>
        <p>Test ran on: {meta_data["Created on"]}</p>

    <h4>Table with Test data</h4>
    {table1}
    </body>
    </html>
    '''

html_result = html(result[1], result[2], test_data_table)