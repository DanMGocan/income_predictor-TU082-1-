# https://medium.com/@hannah15198/convert-csv-to-json-with-python-b8899c722f6d

import csv, json

counter = 0

csvPath = "data/data_set.csv"
jsonPath = "data/data_set.json"

data = {}
data_list = []

with open(csvPath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for rows in csvReader:
        data_list.append(rows)
        #data[counter] = rows
        #counter += 1



#with open(jsonPath, "w") as jsonFile:
#    jsonFile.write(json.dumps(data, indent=4))


