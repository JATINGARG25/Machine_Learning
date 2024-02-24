import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error

data = "C:/Users/gargj/Desktop/Machine learning/Machine_Learning/melb_data.csv"
df = pd.read_csv(data)

# print(df.head())
# print(df.describe())
# print(df.columns)
# print(df.shape)
# print(df.info())

y = df.Price

df_features = ["Rooms","Landsize","Bathroom","Bedroom2"]
X = df[df_features]

model = DecisionTreeRegressor(random_state = 1)
model.fit(X,y)

predictions = model.predict(X)
print(model.predict(X.head()))
print(y.head().to_list())

mea
n_absolute_error(y,predictions)

