# Задание 1
# Пользователь вводит с клавиатуры два числа. 
# Нужно посчитать отдельно сумму четных, нечетных и чисел, кратных 9 в указанном диапазоне,
# а также среднеариф- метическое каждой группы.



# number1 = int (input ('Введіть число №1: '))
# number2 = int (input ('Введіть число №2: '))
# sum1 = 0
# sum2=0
# mult=0
# for i in range(number1,number2+1):
#     if  i%2==0 :
#         sum1+=i
#     else:
#         sum2+=i
#     if i%9==0:
#         mult+=i
# print(f"Сума парних {sum1}")
# print(f"Сума не парних {sum2} ")
# print(f"Сума чисел кратниї 9 {mult}")



# Задание 2
# Пользователь вводит с клавиатуры длину линии и символ для заполнения линии.
# Нужно отобразить на экране вертикальную линию из введенного символа, указанной длины.
# Например, если было введено 5 и символ %, тогда вывод на экран будет такой:

# length = int(input("Введіть значення: "))
# symbol = input("Введіть символ: ")
# for i in range(length):
#     print(symbol)


# Задание 3
# Пользователь вводит с клавиатуры числа. Если число больше нуля нужно вывести надпись «Number is positive»,
# если меньше нуля «Number is negative», если равно нулю «Number is equal
# to zero». Когда пользователь вводит число 7 программа прекращает 
# свою работу и выводит на экран надпись «Good bye!»

# while True:
#     i= int(input("Ввести число : "))
#     if i > 0 :
#         print("Number is positive")
#     elif i < 0:
#         print("Number is negative")
#     else:
#         print("Number is equalto zero")
#     if i == 7:
#         print("Good bye!")
#         break

        



# Задание 4
# Пользователь вводит с клавиатуры числа. Програм- ма должна подсчитывать сумму, 
# максимум и минимум, введенных чисел. Когда пользователь вводит число 7 программа 
# прекращает свою работу и выводит на экран надпись «Good bye!»





# i = int(input("Введіть число: "))
# a = 0
# mi,ma = i, i
# while True:
#    a+=i
#    if i > mi:
#        mi = i
#    if i < ma:
#        ma = i
#    i = int(input("Введіть число: "))
#    if i ==7:
#        print("Good bye!")
#        break
# print("Сумма равна:",a)
# print("Максимум:",mi)
# print("Минимум:",ma)



