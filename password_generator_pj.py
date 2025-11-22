import random
import string
length = int(input("enter the length of password : "))
pwd = string.ascii_letters + string.punctuation + string.digits
password = ""
for i in range(length):
    password+=random.choice(pwd)

print("your strong password is : ",password)