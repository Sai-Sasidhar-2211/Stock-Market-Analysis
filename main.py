# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import glob
import pandas as pd
path = r'C:\Users\aditya\Downloads\Stock'
files = glob.glob(path + "/*.csv")

df = (pd.read_csv(file) for file in files)
df1 = pd.concat(df, ignore_index=True)
df1.rename(columns={'TIMESTAMP':'DATE'},inplace = True)
df1.set_index('DATE',inplace = True)
print(df1.head())

shares = ["TCS","NIFTYBEES","RELIANCE","NIF100BEES","SBIN","INFY"]
df2 = pd.DataFrame()
for i in range(len(shares)):
    df2 = df2.append(df1.loc[(df1.SYMBOL == shares[i])])
print(df2)

column = ["SYMBOL","OPEN","HIGH", "LOW", "CLOSE", "TOTTRDQTY"]
df3 = df2[column]
print(df3)
df3.to_csv('Data1.csv')

a  =[['TCS','INFY'],['TCS','NIFTYBEES'],['TCS','NIF100BEES'],['TCS','RELIANCE'],['RELIANCE','SBIN']]
for i in range(len(a)):
    print(a[i][0]," - ",a[i][1])
    print(df3.loc[(df3.SYMBOL == a[i][0])].corrwith(df3.loc[(df3.SYMBOL == a[i][1])],axis = 1))

df3['2D_Avg'] = df3['CLOSE'].rolling(2).mean()
df3['5D_Avg'] = df3['CLOSE'].rolling(5).mean()
print(df3.head())