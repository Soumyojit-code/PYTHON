#series using Dectionary
import pandas as pd
Fruth_Protein={"Apple":0.5,"Blackberries":2,"Grapes":0.6,"Kiwi":0.8,
               "Watermelon":0.9  }
#print(pd.Series(Fruth_Protein))
s1=pd.Series(Fruth_Protein)
s1=pd.Series(Fruth_Protein,name="Protein")
s1.index.name="Fruth"
print(s1)
s1[s1>1]
print(s1[(s1>0.1) | (s1<2)])
print()
s1[(s1>=0.5)&(s1<0.8)]
#modyfying
s1["Apple"]=2.0
print(s1)


