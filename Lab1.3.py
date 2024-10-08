# Import NumPy and pandas
import numpy as np
import pandas as pd

# Import the LinearRegression function from sklearn.linear_model
from sklearn.linear_model import LinearRegression

# Read in the csv file homes.csv
homes = pd.read_csv('dataset/homes.csv')

# Store relevant columns as variables
y = homes['Price']
y = np.reshape(y.values, (-1,1))
X = homes['Floor']
X = np.reshape(X.values, (-1,1))

# Fit a least squares regression model
linModel = LinearRegression()
linModel.fit(X,y)

# Print the intercept and slope of the regression
print('The intercept of the regression is ', end="")
print('%.3f' % linModel.intercept_)

print('The slope of the regression is ', end="")
print('%.3f' % linModel.coef_)