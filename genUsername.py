import pandas as pd

num = int(input("please input the number of username: "))

cat = ['ptest'+'%03d'%i for i in range(0,num+1)]

dataframe = pd.DataFrame({'username':cat,'password':cat})

dataframe.to_csv("test.csv",index=False,sep=',')