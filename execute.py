from execution.data_to_html import html

html_result = html()[0]
t5 = html()[1]

def execute(html_string):
    new_string = html_string.replace("<PLACEHOLDER_FOR_TOTAL_EXEC_TIME>", f'''
    <tr>
        <th scope="col">Total execution time:</th>
        <td>{round(t5, 3)} seconds</td>
    </tr>
    ''')
    
    with open('index.html','w') as data:
        data.write(new_string)

    

execute(html_result)
