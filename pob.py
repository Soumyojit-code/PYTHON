import numpy as np
import pandas as pd
data= { "Name":['Alic','Bob','Charlie','David','Eve'],"Age":[25,30,np.nan,35,np.nan],"City":['Delhi','Kolkata','MUmbai','Siliguri','Guwahati']}
df=pd.DataFrame(data)
print(data)
total_missing=df.isnull().sum()
print(total_missing)
print(df.isnull().sum())
