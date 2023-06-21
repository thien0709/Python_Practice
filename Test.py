import pandas as pd
melbourne_file_path = './melb_data.csv'
a = pd.read_csv(melbourne_file_path)
print(a.describe()) #Mô tả số liệu về bảng
print(a.columns) # (Các tiêu đề của bảng) Xem danh sách tất cả các cột trong tập dữ liệu
print(a.dropna) # Loại bỏ các các dòng hoặc cột chứa giá trị NaN
print(a.Address) # Chọn mục tiêu dự đoán (địa chỉ)
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
print(a[melbourne_features].describe()) # Lựa chọn các tính năng (Các cột được nhập vào sau đó được sử dụng để đưa ra dự đoán)
print(a[melbourne_features].head())
# print(a.Price) == print(a['Price'])

