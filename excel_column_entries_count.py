import pandas as pd
import numpy as np
x = pd.read_excel(r'C:\Users\admin\Desktop\123.xlsx')

y = x.status.value_counts()
i = ['surveyed by','ownership','building type','vacancy','proposed renovation','building type','flooring type',
    'proper sitting place','playing area','weighing scale','weighing scale type','height stand','height scale type',
    'infantometer','meal supplier','separate kitchen','platform','toilet','tap in toilet','toilet repair','useless items',
     'separate place washing utensils','separate place washing hands','uniform','medical kit','time to bring water','thr on time',
     'usable ro','ro filter repair','preschool toys','color type','roof leakage','electricity','electricity source',
     'electricity bill paid by','dishes washed at','drumstick tree','drumstick leaves used','curry leaves','need to call kids',
     'kids migration','mobile phone','mobile phone type','range','aww residence','aww education']
for z in i:
    y = y.append(pd.Series([z]))
    x[z] = x[x['status']=='Approved'][z].fillna("BLANK")
    y = y.append(x[x['status']=='Approved'][z].value_counts())

y.to_excel('done.xlsx')