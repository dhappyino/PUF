import hashlib
import random
array = []
password = input('使用者輸入密碼:')
print('使用者密碼:', password)
hash_password = hashlib.sha256(password.encode(
    "utf-8")).hexdigest()  # 用sha256對password進行加密
print("十六進位:", hash_password)
number = int(hash_password, 16)
print("十進位:", number)  # 十六轉十
decimalValue = number
binaryString = ""
value = decimalValue
while value != 0:
    binaryString = str(value % 2) + binaryString
    value //= 2
print("二進位: ", binaryString)
array = random.randint(10, 99) for x in range(1024)
print(array)
