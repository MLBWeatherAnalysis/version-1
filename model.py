import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("data_file2.csv")

df.columns
df_model = ['OPS', 'temp','precip','wind_spd']

# dummy data
df_dummy_data = pd.get_dummies(df_model)

# # train test split
from sklearn.model_selection import train_test_split
X = df_dummy_data.drop('OPS', axis=1)
y = df_dummy_data.OPS.values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

''' multiple linear regression '''
# import statsmodels.api as sm

# X_sm = X = sm.add_constant(X)
# model = sm.OLS(y,X_sm)
# model.fit().summary()

# from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score

# lm = LinearRegression()
# lm.fit(X_train, y_train)

# np.mean(cross_val_score(lm,X_train,y_train, scoring = 'neg_mean_absolute_error'), cv=3)

# ''' lasso regression '''
# from sklearn.linear_model import  Lasso
# lm_l = Lasso()
# np.mean(cross_val_score(lm,X_train,y_train, scoring = 'neg_mean_absolute_error'), cv=3)

# alpha = []
# error = []

# for i in range(1,100):
#     alpha.append(i/10)
#     lml = Lasso(alpha=(i/10))
#     error.append(np.mean(cross_val_score(lml,X_train,y_train, scoring = 'neg_mean_absolute_error', cv=3)))

# plt.plot(alpha, error)

# err = tuple(zip(alpha, error))
# df_err = pd.DataFrame(err, columns = ['alpha', 'error'])
# df_err[df_err.error == max(df_err.error)]

''' random forest '''
from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor()

print(np.mean(cross_val_score(rf,X_train,y_train, scoring = 'neg_mean_absolute_error', cv =3)))
# returns -.82
# 26 ish min but have no idea what's going on above or really just at all
