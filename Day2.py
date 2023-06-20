name = "Toi ten la Bach Xuan Thien"
a =258
print(name)
print(len(name)) #Độ dài chuỗi
print(int('10')) #Chuyển thành số
print(float(10)) #Chuyển thành float
print(type(str(1000023479847)))
userName = input('Enter userName: ') #Nhập dữ liệu từ bàn phím
print(list(userName))
print(dict([('a',1),('b',2)])) #Tạo một từ điển với cặp từ khóa - giá trị được xác định
print(min(4,1,2)) #Trả về phần từ min
print(max(4,10,33)) #Trả về phần từ max
print(sum([5,10])) #Trả về tổng các phần tử
print(sorted([4,232,43,4])) #Trả về danh sách sắp xếp các phần tử 
# open()
# file()
# help()
# dir()

#multiple declare 
first_name, last_name,a, b = 'Bach','Thien', 10 ,5 
print(first_name,last_name,a,b)
#int to float, float to int, int to str, str to int or float , str to list
a_int = 10
a_float = 10.0
a_string = '10'
print(float(a_int))
print(int(a_float))
print(str(a_int))
print(int(a_string))
print(float(a_string))
print(list(a_string))

#Exercise Day2
#level 1
first_name  = 'Xuan'
last_name = 'Thien'
full_name = 'Bach Xuan Thien'
country = 'VietNam'
age = 18
year = 2004
is_married = False
is_true = True
is_light_on = True
a, b,c, light_on = 10 , 5, '12', True
#level 2 
x = input('Input value: ')
print(type(x))
print(len(first_name))
a = len(first_name) > len(last_name)
print(a)
num_one =5 
num_two = 4
sum = num_one +num_two
subtract = num_one - num_two
multiply  = num_one * num_two
divide = num_one / num_two

print(sum, subtract,multiply,divide)
print(num_one % num_two)