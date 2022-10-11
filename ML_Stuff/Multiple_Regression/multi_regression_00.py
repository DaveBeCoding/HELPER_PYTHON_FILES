import pandas
from sklearn import linear_model # Linear regression object -> has a method call "fit()"
#Fit: takes the independent and dependent values as parameters and fills the regression object with data
# that describes the relationship 

# predict the CO2 emission of a car based on the size of the engine
# with multiple regression we can throw in more variables, 
# ...like the weight of the car <- makes the prediction more accurate

df = pandas.read_csv("data.csv") 

# 

# make a list of the independent values and call this variable X
X = df[['Weight', 'Volume']]

# Put the dependent values in a variable called y
y = df['CO2']

# NOTE: common to name the list of independent values with a upper case X, 
# .... and the list of dependent values with a lower case y

# 
regr = linear_model.LinearRegression()
regr.fit(X, y)

#Predict the CO2 emission of a car where the weight is 2300(kg), and the volume is 1300(cm3)
predictedCO2 = regr.predict([[2300, 1300]])



