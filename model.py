import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

data = pd.read_csv('car_price.csv')
print(data)

x = data.iloc[:,:3]
y = data.iloc[:, -1]

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

regressor.fit(x,y)

pickle.dump(regressor, open('model.pkl','wb'))


model = pickle.load(open('model.pkl','rb'))

print(model.predict([[2,6000,9]]))


