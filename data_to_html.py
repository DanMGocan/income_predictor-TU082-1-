from split_data import meta_data
from model_test import result

def html(correct, wrong):
    percentage = correct / (correct + wrong)
    return f'''
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

    </body>
    </html>
    '''

html_result = html(result[1], result[2])