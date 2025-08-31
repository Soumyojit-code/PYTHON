#pandas practice
import pandas as pd
s=pd.Series([10,20,30,40,50])
print(s)
s.dtype
s.values
s.index
s.name='S'
print(s.name)
#indexing
s[0]
s[0:2]
print(s)
s.iloc[3]
print(s)
String=['A','B','C','D','E']
s.index=String
print(s['E'])
