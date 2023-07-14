
# Задание 1
# Напишите функцию, которая отображает на экран форматированный текст, указанный ниже:
# “Don't compare yourself with anyone in this world... if you do so, you are insulting yourself.”
# Bill Gates


# def print_quote():
#     quote = "\t\t\t“Don’t compare yourself with anyone in this world…\n" \
#             "\t\t\tif you do so, you are insulting yourself.”\n" \
#             "\t\t\t\t\t\t\t\t\t\t\t\t\t\tBill Gates"
#     print(quote)
# print_quote()


# Задание 2
# Напишите функцию, которая принимает два числа в качестве параметра и
# отображает все четные числа между ними.

# def print_numbers(start, end):
#     for num in range(start, end + 1):
#         if num % 2 == 0:
#             print(num)


# print_numbers(1, 12)

# Задание 3
# Напишите функцию, которая отображает пустой или заполненный квадрат из некоторого символа.
# Функция принимает в качестве параметров: длину стороны ква- драта, символ и переменную логического типа:
# ■ если она равна True, квадрат заполненный; ■ если False, квадрат пустой.

# def draw_square(Length, symbol, filled):
#     if filled:
#         for i in range(Length):
#             print(symbol * Length)
#     else:
#         for i in range(Length):
#             if i == 0 or i == Length - 1:
#                 print(symbol * Length)
#             else:
#                 print(symbol + " " * (Length - 2) + symbol)


# draw_square(5, '*', False)


# Задание 4
# Напишите функцию, которая возвращает минимальное из пяти чисел. Числа передаются в качестве параметров.

# def min_of_five(a, b, c, d, e):
#     min_val = a
#     if b < min_val:
#         min_val = b
#     if c < min_val:
#         min_val = c
#     if d < min_val:
#         min_val = d
#     if e < min_val:
#         min_val = e
#     return min_val


# print(min(12, 123, 412, 1, 42))


# Завдання 5
# Напишіть функцію, яка повертає добуток чисел у зазна-
# ченому діапазоні. Межі діапазону передаються як параметри.
# Якщо межі діапазону переплутані (наприклад, 5 — верхня
# межа, 25 — нижня межа), їх треба поміняти місцями.
# 

# def product_range(start, end):
#     if start > end:
#         start, end = end, start
#     product = 1
#     for i in range(start, end + 1):
#         product *= i
#     return product


# number = product_range(5, 1)
# print(number)

# Завдання 6
# Напишіть функцію, яка підраховує кількість цифр у числі.
# Число передається як параметр. Поверніть з функції отриману
# кількість цифр. Наприклад, якщо передали 3456, кількість
# цифр буде 4.
# 

# def count_number(num):
#     num_digits = 0
#     temp = num
#     while temp > 0:
#         temp //= 10
#         num_digits += 1
#     return num_digits


# numbers = count_number(113422)
# print(numbers)




# Завдання 7
# Напишіть функцію, яка перевіряє число на паліндром.
# Число передається як параметр. Якщо число є паліндромом,
# поверніть з функції true, якщо ні — false.
# «Паліндром» — це число, в якому перша частина цифр
# дорівнює другій перевернутій частини цифр. Наприклад,
# 123321 — паліндром (перша частина 123, друга 321, яка після
# перевороту стає 123), 546645 — паліндром, а 421987 — не
# паліндром.


# def check_palindrome(num):
#     if num < 0:
#         return "Не паліндром"
#     if num == 0:
#         return "Паліндром"
#     num_digits = 0
#     temp = num
#     while temp > 0:
#         temp //= 10
#         num_digits += 1
#     number = 0
#     number2 = 0
#     for i in range(num_digits // 2):
#         number2 = number2 * 10 + num % 10
#         num //= 10
#     if num_digits % 2 == 1:
#         num //= 10
#     number = num
#     if number == number2:
#         return "Паліндром"
#     else:
#         return "Не паліндром"


# print(check_palindrome(123321))

# print(check_palindrome(546645))

# print(check_palindrome(421987))