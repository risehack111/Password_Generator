import random

chars = '+-/*!&#?=@<>abcdefghijklnmopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
number = int(input("Количество паролей: "))
lenght = int(input("Длина строки: "))
for x in range(number):
    password = ''
    for i in range(lenght):
        password += random.choice(chars)
    print(password)
    file = open('Password.txt', 'a')
    file.write('\n' + password)
    file.close()