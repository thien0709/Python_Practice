import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
# Đọc dữ liệu từ file CSV
melbourne_file_path = './melb_data.csv'
a = pd.read_csv(melbourne_file_path)
data = a.dropna()
# Chọn các đặc trưng (features) và nhãn (labels)
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
X = data[melbourne_features]
y = data['Price']

# Khởi tạo mô hình DecisionTreeRegressor
model = DecisionTreeRegressor(random_state=1)

# Fit mô hình vào dữ liệu
model.fit(X, y)

# Dự đoán giá nhà cho các mẫu huấn luyện
predictions = model.predict(X)
print(predictions)

#Tính sai số tuyệt đối trung bình của mô hình
print(mean_absolute_error(y,predictions))

# Tính sai số trên dữ liệu kiểm tra bn  e4s    
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)
model.fit(train_X,train_y)
val_predictions = model.predict(val_X)
print(mean_absolute_error(val_y,val_predictions))
