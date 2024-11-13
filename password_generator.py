#password_generator
import random

count= int(input("enter the count of password:"))
length= int(input("enter the length of password:"))
chars = 'abcedfghijklmonpqrstuvwxyzABCDEFGHIKKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()[]-+/`\{};'
   
for pwd in range(count):
  password=''
  for c in range(length):
    password += random.choice(chars)
    print(password)

