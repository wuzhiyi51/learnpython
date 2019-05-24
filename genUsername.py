# coding=utf-8
import pandas as pd

num = int(input("请输入输入用户名数量（1-200）: "))

if num > 200:
    print('您输入的数量大于200')
else:
    cat = ['ptest'+'%03d'%i for i in range(1,num+1)]

    dataframe = pd.DataFrame({'username':cat,'password':cat})

    dataframe.to_csv("user.csv",index=False,sep=',')

    print('账号密码已生成，请查看user.csv文件')

# li=[]
# for i in range(0,10):
#     li.append(i)
# print(li)