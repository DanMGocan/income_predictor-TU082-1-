# Importing the string with all the html markup generated
from execution.data_to_html import html

html_result = html()[0]
t5 = html()[1] # Taking the time at the end of data_to_html.py execution

def execute(html_string):
    # A placeholder was created for the final execution time that is now replaced with the actual value
    new_string = html_string.replace("<PLACEHOLDER_FOR_TOTAL_EXEC_TIME>", f'''
    <tr>
        <th scope="col">Total execution time:</th>
        <td>{round(t5, 3)} seconds</td>
    </tr>
    ''')
    
    with open('index.html','w') as data:
        data.write(new_string)

    
# Invoking the final function that will generate the index.html file
execute(html_result)
