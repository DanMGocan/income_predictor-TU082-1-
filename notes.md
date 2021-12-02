First step was to convert from .data to .csv
and then to convert everything in JSON objects.

1. Convert data from .csv to a long dictionary
1.1. Clear the data from #3, #4, #14
1.2. Clear the data (listwise deletion)
1.3. Replace certain values with scales or binary values
1.3.1. Replace numerical 

2. Randomly separate the information in two
categories: learning and test (80% vs. 20%)

#! VERY IMPORTANT !#
Process data as such to create groups of 10 in terms of
age, capital gains / loss, etc. Create groups based on
splitting averages. Split the averages by equally distributing
values.

Add optional conversion to JSON
Type conversion as well, when writing the dictionary
Percentage of people based on categories

xx% of people of age XX have income > 50k
xx% of white people have income > 50k
etc. etc. etc.

Do not forget to add DOCSTRINT

Must add an incrementor / decrementor when checking for age,
capital gains or losses as the exact values might not be present
inside the trained model

Put together chart of data transition in .ppt, to see how data is moved and modified (???)

Export all information as an .html document

Code that is easily adaptable with minimal modification

Code should return html documents, with all the available information, structured in tables

Maybe add rounding to categories

Add all categories as some test data might have some extra categories that are not present in the initial set