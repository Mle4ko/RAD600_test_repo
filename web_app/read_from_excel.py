#!//usr/bin/python3

from itertools import count
from numpy import size, sort
import pandas as pd
import sys
import os
from contextlib import redirect_stdout
import random

df = pd.read_excel('/home/lsauser/python_projects/Test_40BT.xlsx', sheet_name=None, header=None)

sheet1 = df["Sheet1"]

total_rows = (len(sheet1))
# print(random.randint(0, total_rows-1))
questions = []


while len(questions) < 5:
    q = random.randint(0, total_rows-1)
    if q not in questions:
        questions.append(q)

print(questions)
 
questions = sort(questions)    
print(questions)


for q in questions:
    print(f"{q+1}. {sheet1.loc[q, 1]}")
    print(f"    A: {sheet1.loc[q, 2]}")
    print(f"    B: {sheet1.loc[q, 3]}")
    print(f"    C: {sheet1.loc[q, 4]}")
    print(f"    D: {sheet1.loc[q, 5]}")
    print()
    print()
    

# print(len(sheet1))
        



# for row in range(total_rows):
    
#     print(sheet1.loc[row, 1])

# print(len(sheet1))


# file_loc = "path.xlsx"
# df = pd.read_excel(file_loc, index_col=None, na_values=['NA'], usecols = "A,C:AA")
# print(df)
# print(df.loc[45, 0])

# with pd.option_context('display.max_rows', 55, 'display.max_columns', None):
#     # print(df)
#     with open('/home/lsauser/python_projects/test_output.txt', 'w') as f:
#         with redirect_stdout(f):
#             print(df) 


# df.at[0,'A']