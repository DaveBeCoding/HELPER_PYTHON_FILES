import pandas

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




