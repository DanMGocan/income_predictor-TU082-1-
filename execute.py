import webbrowser
import time
from raw_data import all_data
from data_to_html import html
from model_test import result

html_result = html()

def execute():

    html_result.replace("<PLACEHOLDER_FOR_TOTAL_EXEC_TIME>", '''
    
    
    ''')
    with open('/index.html','w') as data:
        data.write(html_result)

execute()
