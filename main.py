from csv_to_dict import data, data_list


unique_dict = {}

print(type(data_list[0]))
print(type(data_list))

good = 0
bad = 0

for count, value in enumerate(data_list):
    if value["Outcome"] == " <= 50 K":
        bad += 1
    else:
        good += 1

print(bad, good)