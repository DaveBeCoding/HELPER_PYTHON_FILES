import pandas
from sklearn import linear_model

df = pandas.read_csv("data.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)

print(regr.coef_) 

# Weight: 0.00755095, if the Weight increases by 1kg the CO2 emission increases by W
# Volume: 0.00780526, if the engine size (Volume) increases by 1 cm^3, the CO2 emission increases by V


