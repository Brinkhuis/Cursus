'''
Met dit script wordt een csv-bestand gegenereerd met als doel om
het inlezen van csv-files met pandas te oefenen in Python.
'''

# imports
import pandas as pd
import numpy as np
import datetime
 
# setup
file_name = '../data/leesmij.csv'
records = 50 # number of records
na_vals = int(records / 10) # number of na values
 
# set seed
np.random.seed(777)
 
# generate dataframe
df = pd.DataFrame({'id': range(1, records+1),
                   'leeftijd': np.random.choice(range(18, 100), records, replace=True),
                   'geslacht': np.random.choice(['M', 'V'], records, replace=True),
                   'groep': np.random.choice([i for i in 'ABC'], records, replace=True)})
 
# add na values
for _ in range(na_vals):
    df.iloc[np.random.choice(range(records)), -2] = np.random.choice(['??', '-'], 1, replace=True)
    df.iloc[np.random.choice(range(records)), -1] = np.random.choice(['', ' ', '  '], 1, replace=True)
 
# save to csv
df.to_csv(file_name, sep='/', index=False)
 
# add opening line to file
line = 'Dit bestand is gegenereerd t.b.v. de cursus Data Science with Python'
with open(file_name, 'r+') as f:
    file_data = f.read()
    f.seek(0, 0)
    f.write(line.rstrip('\r\n') + '\n' + file_data)
 
# add closing lines to file
line = 'Dit bestand is gegenereerd op {}\n============== END OF FILE ============='.format(str(datetime.date.today().strftime('%d-%m-%Y')))
with open(file_name, 'a') as f:
    f.write(line.rstrip('\r\n'))
