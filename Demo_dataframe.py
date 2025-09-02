#Data Frame
import pandas as pd
Data={
    "Name":["Ram","Alice","Bob","David","Rohit","Ram"],
    "Age":[25,32,27,26,24,25],
    "Deparment":["HR","IT","Finance","HR","IT","Finance"]
    ,"Salary":[50000,60000,55000,62000,58000,61000]
}
df=pd.DataFrame(Data)
print(df)
df.head(2)
df.tail(2)
#loc and iloc
df.iloc[1:3]
df.loc[1:2,["Age","Deparment"]]
df["Age"]
df.drop("Deparment",axis=1,inplace=True)
#print(df)'''
print(df.shape,"\n")
print('\n',df.describe)
#Broodcasting
df['Salary']=df['Salary']+300
df["Salary"]
#rename columns
df.rename(columns={'Deparment':'Dept'},inplace=True)
#create new columns
df["PRomoted_Salary"]=df["Salary"]*1.1




    
