import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing
import matplotlib.pyplot as plt

df=fetch_california_housing()
df
dataset=pd.DataFrame(df.data)
dataset.columns=df.feature_names
dataset.head()
# IndependentVariable features and dependent features
x=dataset
y=df.target
y
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    x, y, test_size=0.30, random_state=42)
X_train
from sklearn.preprocessing import StandardScaler
Scaler=StandardScaler()
X_train= Scaler.fit_transform(X_train)
X_test=Scaler.transform(X_test)
from sklearn.linear_model import LinearRegression
# cross validition
from sklearn.model_selection import cross_val_score
reg=LinearRegression()
reg.fit(X_test,y_test)
mse=cross_val_score(reg, X_train,y_train, cv=10, scoring='neg_mean_squared_error')
msenp.mean(mse)
reg_pre =reg.predict(X_test)
reg_pre
import seaborn as sns
sns.displot(reg_pre-y_test,kind='kde')
from sklearn.metrics import r2_score
sc=r2_score(reg_pre,y_test,multioutput='variance_weighted')
sc
