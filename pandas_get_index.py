import pandas as pd
df = pd.DataFrame({'BoolCol': [1, 2, 3, 3, 4],'attr': [22, 33, 22, 44, 66]},
       index=[10,20,30,40,50])
print(df)
a = df[(df.BoolCol==3)&(df.attr==22)].index.tolist()
print(a)
