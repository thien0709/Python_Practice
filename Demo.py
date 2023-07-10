import pandas as pd 
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
df = pd.read_csv('./datamau.csv');

future = ['Diện tích','Số phòng ngủ','Số phòng tắm']
X = df[future]
y = df['Giá nhà']

model = DecisionTreeRegressor(random_state=1 )
model.fit(X,y)

data = [[300,7,15]]
y_pred  = model.predict(X)
y_predict = model.predict(data)
print(y_pred)
print(y_predict)
print(y)
print(mean_absolute_error(y,y_pred))
