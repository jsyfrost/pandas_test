import pandas as pd
import numpy as np

df = pd.DataFrame(np.zeros((8, 4)))  # 新建一个数据框
df.iloc[2:6, 0] = 1  # 将第0列的第3行到第6行的值改为1


def getlistnum(li):  # 这个函数就是要对列表的每个元素进行计数
    li = list(li)
    set1 = set(li)
    dict1 = {}
    for item in set1:
        dict1.update({item: li.count(item)})
    return dict1

print(df[0])
zero_col_count = getlistnum(df[0])  # df[0]指列名为0的列，如果你的列名是字符串就要加引号
three_row_count = getlistnum(df.loc[3])  # df.loc[0]指行名为0的行，同样字符串的话要加引号
print(zero_col_count)

print(df)
print(df.count())