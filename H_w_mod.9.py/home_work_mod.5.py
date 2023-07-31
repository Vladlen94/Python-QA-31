

# Задание 1
# Напишите функцию, которая отображает на экран форматированный текст, 
# указанный ниже:
# “Don't compare yourself with anyone in this world... 
# if you do so, you are insulting yourself.”
# Bill Gates

# def print_quote():
#     quote = "\t\t\t“Don’t compare yourself with anyone in this world…\n" \
#             "\t\t\tif you do so, you are insulting yourself.”\n" \
#             "\t\t\t\t\t\t\t\t\t\t\t\t\t\tBill Gates"
#     print(quote)


# Задание 2
# Напишите функцию, которая принимает два числа в
# качестве параметра и отображает
# все четные числа между ними.


# def evet_2(a,b):
#     if b > a:
#         for i in range(a, b + 1):
#             if i % 2 == 0:
#                 print(i, end=" ")
#     elif a > b:
#         for i in range(b, a + 1):
#             if i % 2 == 0:
#                 print(i, end=" ")




# def print_numbers(start, end):
#     for num in range(start, end + 1):
#         if num % 2 == 0:
#             print(num)



# Задание 3
# Напишите функцию, которая отображает пустой или заполненный квадрат из некоторого символа. 
# Функция принимает в качестве параметров: длину стороны ква- драта, символ и переменную логического типа:
# ■ если она равна True, квадрат заполненный; ■ если False, квадрат пустой.

# def square(sym,n,fill=True):
#     line=n*sym
#     if fill:
#         for _ in range(n):
#             print(line)
#     else:
#         print(line)
#         for _ in range(n-2):
#             print(sym+" "*(n-2)+sym)
#         print(line)    
        
        
# square("*",8,False)
    

# Напишите функцию, которая возвращает минимальное из пяти чисел. Числа передаются в качестве параметров.

# def min_of_five(a, b, c, d, e):
#    min_num = a
#    if b < min_num:
#        min_num = b
#    if c < min_num:
#        min_num = c
#    if d < min_num:
#        min_num = d
#    if e < min_num:
#        min_num = e
#    return min_num



# Задание 5
# Напишите функцию, которая возвращает произве- дение чисел в указанном диапазоне.
# Границы диапазона передаются в качестве параметров.
# Если границы диапа- зона перепутаны (например, 5 — верхняя граница, 25 — нижняя граница), 
# их нужно поменять местами.


# def prod_of_range(start, end):
#    prod = 1
#    for i in range(start, end+1):
#        prod *= i
#    return prod



# Задание 6
# Напишите функцию, которая считает количество цифр в числе. 
# Число передаётся в качестве параметра. 
# Из функции нужно вернуть полученное количество цифр.
# Например, если передали 3456, количество цифр будет 4.


# def count_digits(num):
#    count = 0
#    while num != 0:
#        count += 1
#        num //= 10
#    return count


# Задание 7
# Напишите функцию, которая проверяет является ли число палиндромом.
# Число передаётся в качестве пара- метра. 
# Если число палиндром нужно вернуть из функции true, иначе false.
# «Палиндром» — это число, у которого первая часть цифр равна второй перевернутой части цифр. 
# Например, 123321 — палиндром (первая часть 123, вторая 321, которая после переворота становится 123),
# 546645 — палиндром, а 421987 — не палиндром.


# def is_palindrome(num):
#    num_str = str(num)
#    return num_str == num_str[::-1]
