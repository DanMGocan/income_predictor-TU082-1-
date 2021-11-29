from raw_data import all_data

def split_data(initial_data, training_percentage):
    train_data = initial_data[ : int((len(initial_data)+1)*(training_percentage / 100))] 
    test_data = initial_data[int((len(initial_data)+1)*(training_percentage / 100)):] 
    return train_data, test_data

divided_data = split_data(all_data["all_data"], 90)

train_data = divided_data[0]
test_data = divided_data[1]