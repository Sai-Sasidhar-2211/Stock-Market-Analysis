# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import glob
    import pandas as pd
    path = 'D:\Company\Project needs\Data'
    files = glob.glob(path + "/*.csv")
    df = (pd.read_csv(file) for file in files)
    df1= pd.concat(df, ignore_index=True)
    df1.rename(columns={'TIMESTAMP':'DATE'},inplace = True)
    df1.set_index('DATE',inplace = True)
    print(df1.head())
    df1.to_csv('Data.csv') #1st question

    c = ["TCS","NIFTYBEES","RELIANCE","NIF100BEES","SBIN","INFY"]
    data = pd.DataFrame()
    for i in range(len(c)):
        data = data.append(df1.loc[(df1.SYMBOL == c[i])])
    print(data)   #2nd question

    column = ["SYMBOL","OPEN","HIGH", "LOW", "CLOSE", "TOTTRDQTY"]
    df2 = df1[column]
    print(df2.head())
    df2.to_csv('Data1.csv')  #3rd question

    a  =[['TCS','INFY'],['TCS','NIFTYBEES'],['TCS','NIF100BEES'],['TCS','RELIANCE'],['RELIANCE','SBIN']]
    for i in range(len(a)):
        print(a[i][0]," - ",a[i][1])
        print(data.loc[(data.SYMBOL == a[i][0])].corrwith(data.loc[(data.SYMBOL == a[i][1])],axis = 1))  #4th question

    df2['2D_Avg']= df2['CLOSE'].rolling(2).mean()
    df2['5D_Avg'] = df2['CLOSE'].rolling(5).mean()
    print(df2.head())  #5th question

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
