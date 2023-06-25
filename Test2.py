import pandas as pd
from sklearn.tree import DecisionTreeRegressor

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
