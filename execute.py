import webbrowser
import time
from raw_data import all_data
from data_to_html import html_result
from model_test import result

def execute():
    t1 = all_data["initial_time"]
    t2 = time.perf_counter()
    time_perf = round( t2 - t1, 2)
    success_rate = round( result[3]*100, 2)

    results = []
    results.append(f"Test has been executed in {time_perf} with a success rate of {success_rate}")

    with open('data/results.html','w') as data:
        data.write(html_result)

    return results

print(execute())