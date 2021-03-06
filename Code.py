
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 14:16:34 2015

@author: pupreti
"""

import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

"""
Model 1: Where the intercept term is clearly needed 
This model is the dataset from the cricket chirps vs temperature
"""
#Creating dataframe of Cricket chirp using pandas as cricket_chirp
chirps ={'x': pd.Series([20, 16, 19.8, 18.4, 17.1, 15.5, 
    14.7, 17.1, 15.4, 16.2, 15, 17.2, 16, 17, 14.4]),
    'y': pd.Series([88.6, 71.6, 93.3, 84.3, 80.6, 
    75.2, 69.7, 82, 69.4, 83.3, 79.6, 82.6, 80.6, 83.5, 76.3])}   
cricket_chirp= pd.DataFrame(chirps)

x=cricket_chirp['x']
y= cricket_chirp['y']

#Regression through origin
model1RTO=sm.OLS(y,x).fit()
model1RTO.summary()

#adding constant 1 on the X dataset and running regression
xconstant = sm.add_constant(x)
model1OLS = sm.OLS(y, xconstant).fit()
model1OLS.summary()

#creating points based on the models to draw the regression line
x_prime = np.linspace(-1, x.max(), 100)[:, np.newaxis]
y_hat = model1RTO.predict(x_prime)
resid_model1RTO = y-model1RTO.predict(x)

plt.scatter(x,y, alpha= 0.5)
plt.plot(x_prime, y_hat, 'r', alpha=0.9)
plt.xlabel("x")
plt.ylabel("y")
plt.title("scatterplot with best fit regression line")


x_prime2= sm.add_constant(x_prime)
y_hat2= model1OLS.predict(x_prime2)
resid_model1OLS = y -model1OLS.predict(xconstant)

plt.scatter(x,y, alpha= 0.5)
plt.plot(x_prime2[:, 1], y_hat2, 'b', alpha=0.9)
plt.xlabel("x")
plt.ylabel("y")
plt.title("scatterplot with best fit line")

plt.scatter(x,y- model1OLS.predict(xconstant))
plt.xlabel("x")
plt.ylabel("residual")
plt.title("residual against x")

sm.qqplot(y- model1OLS.predict(xconstant),fit = True, line ="45")
plt.title("QQ Plot to check for normality of residuals")


plt.scatter(x,y- model1RTO.predict(x))
plt.xlabel("x")
plt.ylabel("residual")
plt.title("residual against x")

sm.qqplot(y- model1RTO.predict(x),fit = True, line ="45")
plt.title("QQ Plot to check for normality of residuals")

plt.scatter(x, resid_model1OLS)
plt.scatter(x, resid_model1RTO)

sum(resid_model1OLS**2)
sum(resid_model1RTO**2)




#Plot QQ to see if the data is normal
plt.scatter(model1RTO.predict(x), resid_model1RTO )


data ={'a': pd.Series([20, 16, 19.8, 18.4, 17.1, 15.5, 
    14.7, 17.1, 15.4, 16.2, 15, 17.2, 16, 17, 14.4,0,1,2,3,4,0,0,
    5,10,13, 7,8,9,10,12,12,4,3,3,6,8]),
    'b': pd.Series([88.6, 71.6, 93.3, 84.3, 80.6, 
    75.2, 69.7, 82, 69.4, 83.3, 79.6, 82.6, 80.6, 83.5, 76.3, 3,4,2, 2 , 2,9,1,
    10,40,60,40,30,45,50,50,60,20,15,18,40,70])} 

data= pd.DataFrame(data)

noint= sm.OLS(data['b'], sm.add_constant(data['a'])).fit()
noint.summary()

plt.scatter(data['a'], data['b'])
plt.plot(data['a'], noint.predict(sm.add_constant(data['a'])), '-' )
plt.xlabel("x")
plt.ylabel("y")
plt.title("scatterplot with best fit line")

whatint= sm.OLS(data['b'], data['a']).fit()
whatint.summary()

plt.scatter(data['a'], data['b'])
plt.plot(data['a'], whatint.predict(data['a']), '-' )
plt.xlabel("x")
plt.ylabel("y")
plt.title("scatterplot with best fit line")

resid2 = data['b']-whatint.predict(data['a'])

plt.plot(data['a'], resid2, '.')

plt.plot(list(range(1, 37)), resid2, '-')
plt.xlabel("time")
plt.ylabel("residual")
plt.title("timeplot of residual")

sm.qqplot(resid2,fit = True, line ="45")
