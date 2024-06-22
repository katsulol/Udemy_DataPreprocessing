import numpy as np
import pandas as pd
import matplotlib as plt
from sklearn.impute import SimpleImputer

df = pd.read_csv("Data.csv")

x = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

#print(x, y)

imputer = SimpleImputer(missing_values = np.nan, strategy = "mean")
imputer.fit(x[:, 1:3])
x[:, 1:3] = imputer.transform(x[:, 1:3])
print(x)
