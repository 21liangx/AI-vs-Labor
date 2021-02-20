"""
Created on Thu Dec 1 2020

@author: xiaoyu
"""

import csv
import pandas as pd

with open('database.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

print('Re-formating Dataset')
rank = []
prob = []
soc = []
occu = []
for i in data:
    i_string = str(i)
    a = i_string.find(' ')
    rank.append(i_string[2:a-1])

    i_string = i_string[a+1:]
    a = i_string.find(' ')
    prob.append(i_string[0:a])

    i_string = i_string[a+1:]
    a = i_string.find(' ')
    num = i_string[0:a]
    if num not in ('0','1'):
        soc.append(num)
    else:
        i_string = i_string[a+1:]
        a = i_string.find(' ')
        soc.append(i_string[0:a])

    occu.append(i_string[a+1:-2])

print('Test')
print(rank[0:5])
print(prob[0:5])
print(soc[0:5])
print(occu[0:5])

print('Exporting DataFrame to csv')
df = pd.DataFrame(columns=['RANK','PROBABILITY','SOC_CODE','OCCUPATION'])
df['RANK'] = rank
df['PROBABILITY'] = prob
df['SOC_CODE'] = soc
df['OCCUPATION'] = occu
df.head(10)

df.to_csv(r'C:\Users\xiaoyu\Desktop\Website\DATABASE_FINAL.csv', index = False, header=True)
