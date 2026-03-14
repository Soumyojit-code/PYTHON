import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = pd.read_csv("placement.csv")

print("Available columns:", data.columns.tolist())

X = data[['cgpa']]
y = data['package']

model = LinearRegression()
model.fit(X, y)

m = model.coef_[0]
c = model.intercept_

print(f"Equation of line: y = {m:.2f}x + {c:.2f}")

plt.figure(figsize=(8,6))
plt.scatter(X, y, color='blue', label='Data points')
plt.plot(X, model.predict(X), color='red', label=f'y={m:.2f}x+{c:.2f}')
plt.xlabel("CGPA")
plt.ylabel("Package")
plt.title("Linear Regression Fit")
plt.legend()
plt.grid(True)
plt.show()
import pandas as pd

# Create DataFrame with the correct column name 'cgpa' instead of 'x'
x_new = pd.DataFrame({'cgpa': [10]})   # Changed column name from 'x' to 'cgpa' to match training data

# Make prediction
y_pred = model.predict(x_new)

print(f"predicted y = {y_pred[0]:.2f}")