First step was to convert from .data to .csv
and then to convert everything in JSON objects.

1. Convert data from .csv to a long dictionary
1.1. Clear the data from #3, #4, #14
1.2. Clear the data (listwise deletion)
1.3. Replace certain values with scales or binary values

2. Randomly separate the information in two
categories: learning and test (80% vs. 20%)


Add optional conversion to JSON
Type conversion as well, when writing the dictionary
Percentage of people based on categories

xx% of people of age XX have income > 50k
xx% of white people have income > 50k
etc. etc. etc.

TUG OF WAR Optimization system, maybe? 
- Basically, how much of being something affects your income?
For example, gender. If 0.8 of male gender has an income over 50k, 
then the male = gender variable will have a TUGOWAR pull of 0.8.
If the gender is femaile, then the tugowar pull is 0.2. 

Do not forget to add DOCSTRINT

Must add an incrementor / decrementor when checking for age,
capital gains or losses as the exact values might not be present
inside the trained model