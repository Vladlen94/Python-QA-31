
# Задание 1:
# Пользователь вводит с клавиатуры арифметическое выражение. Например, 23+12.
# Необходимо вывести на экран результат выражения. В нашем примере это 35.
# Арифметическое выражение может состоять только из трёх частей:
# число, операция, число. Возможные операции: +, -,*,/




# a = input( " Введить вираз :")
# if a.find("+") != -1:
#     n=a.find("+")
#     print(a,"=",float(a[:n])+float(a[n+1:len(a)]))
# if a.find("-") != -1:
#     n=a.find("-")
#     print(a,"=",float(a[:n])-float(a[n+1:len(a)]))
# if a.find("*") != -1:
#     n=a.find("*")
#     print(a,"=",float(a[:n])*float(a[n+1:len(a)]))   
# if a.find("/") != -1:
#     n=a.find("/")
#     print(a,"=",float(a[:n])/float(a[n+1:len(a)]))    


# В списке целых, заполненном случайными числами, 
# определить минимальный и максимальный элементы,
# посчитать количество отрицательных элементов, 
# посчи- тать количество положительных элементов, 
# посчитать количество нулей.
# Результаты вывести на экран.


# import random
# a=[-12,12,123,-4,11,-56,-23,-56,-12,32,111,45,65,41,-11,-23,-3]
# s=0
# kp=0
# ko=0
# for i in range (20):
#     a.append(random.randint(-10,20))
#     print("%5d" % (a[i]),end="")
#     s += a[i]
#     if a[i]>0:
#         kp += 1
#     if a[i]<0:
#         ko += 1
# print()
# print ("s =",s)
# print ("kp =",kp)
# print ("ko =",ko)

# Задание 1
# Два списка целых заполняются случайными числами. Необходимо:
# ■ Сформироватьтретийсписок,содержащийэлементы обоих списков;
# ■ Сформироватьтретийсписок,содержащийэлементы обоих списков без повторений;
# ■ Сформироватьтретийсписок,содержащийэлементы общие для двух списков;
# ■ Сформировать третий список, содержащий только уникальные 
# элементы каждого из списков;
# ■ Сформировать третий список, содержащий только минимальное и
# максимальное значение каждого из списков.

# from random import randint
# a = [randint(1,10) for x in range(5)]
# b = [randint(1,10) for x in range(5)]
# print(a, '- первый список')
# print(b, '- второй список\n')
# c1 = a+b
# print(c1) 
# c2 = sorted(set(c1), key=c1.index)
# print(c2) 
# c3 = [a[i] for i in range(len(a)) if a[i] in b]
# print(c3)
# c4 = sorted(list(set(a)) + list(set(b)), key=c1.index)
# print(c4) 
# c5 = [min(c1), max(c1)]
# print(c5) 