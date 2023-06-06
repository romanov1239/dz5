# Напишите программу, которая на вход принимает два числа A и B,
#  и возводит число А в целую степень B с помощью рекурсии.

def power(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    else:
        return a * power(a, b-1)

a = int(input("Введите число A: "))
b = int(input("Введите степень B: "))

print(f"{a} в степени {b} равно {power(a, b)}")