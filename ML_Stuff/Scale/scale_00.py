import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler() #  standardization method z = (x - u) / s

# Where z is the new value, x is the original value, u is the mean and s is the standard deviation

df = pandas.read_csv("data.csv")

X = df[['Weight', 'Volume']]

scaledX = scale.fit_transform(X)

print(scaledX)
