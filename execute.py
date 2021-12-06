import webbrowser
from data_to_html import html_result

with open('data/results.html','w') as data:
    data.write(html_result)
    webbrowser.open_new_tab("data/results.html")

# filename = "data/results.html"
# webbrowser.open_new_tab("results.html")