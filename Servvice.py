import pandas as pd
import numpy as np

fl = pd.read_csv("C:\\Users\\aditi\\Downloads\\Salaries.csv")


# print(fl.head())

# print(fl.shape)

# print(fl.info)

print(fl.columns)

# print(fl[:].isnull().sum())

# print(fl['BasePay'].isnull().sum())

# print(fl['TotalPay'].mean())

fl1= fl['TotalPay'].max()
print(fl[fl['TotalPay']==fl1][['EmployeeName','TotalPay']])
