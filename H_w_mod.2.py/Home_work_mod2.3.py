# ; Задание 1
# ; Пользователь вводит с клавиатуры число в диапа- зоне от 1 до 100. Если число кратно 3 (делится на 3 без остатка) 
# ; нужно вывести слово Fizz. Если число кратно 5 нужно вывести слово Buzz. Если число кратно 3 и 5 нужно вывести Fizz Buzz. Если число не кратно не 3 и 5 нужно вывести само число.
# ; Если пользователь ввел значение не в диапазоне от 1 до 100 требуется вывести сообщение об ошибке.



# number = int (input ('Введіть число'))
# if 1 <= number <= 100:
#     if number%3 ==0 and number%5 ==0 :
#         print ('Fizz Buzz')
#     elif  number % 3 ==0:
#         print("Fizz") 
#     elif  number%5 ==0:
#         print("Buzz")
#     elif number %3 != 0 and number% 5 !=0:
#         print(number)
# else:
#     print("Ошибка, введите число в диапазоне [1; 100]")
 








# ; Задание 2
# ; Написать программу, которая по выбору пользова- теля возводит введенное им число
# в степень от нулевой до седьмой включительно.

# number = int(input ("Введіть число: "))
# for i in range(1,8):
#     a=number**i
#     print(a)


# pow=int(input ( ))
# k=int(input ( ))
# i=1
# while i**pow<=k:
#     print (i**pow)





# ; Задание 3
# ; Написать программу подсчета стоимости разговора для 
# разных мобильных операторов. Пользователь вводит стоимость 
# разговора и выбирает с какого на какой опе- ратор он звонит. Вывести стоимость на экран.

# number = int(input())
# action = input("\n1.Bilain \n2.Kyivstar \n3.Vodafon \n4. MTS \nВибери з якого оператора телефонують: ")

# if action == "1":
#     print("Bilain")
# elif action == "2":
#     print("Kyivsatr")
# elif action == "3":
#     print("Vodafon")
# elif action == "4":
#     print("MTS")
# action = input("\n1.Bilain \n2.Kyivstar \n3.Vodafon \n4. MTS \nВибери на  який оператора телефонують: ")

# if action == "1":
#     print(number)
# elif action == "2":
#     print(number)
# elif action == "3":
#     print(number)
# elif action == "4":
#     print(number)



# operator_cost1 = 1.25
# operator_cost2 = 1.75
# operator_cost3 = 1.50

# number_of_minutes = int(input("Ввести кількість хвилин: "))
# action = input("\n1.Bilain \n2.Kyivstar \n3.Vodafon \nВибрати з якого оператора телефонують: ")
# if action == "1":
#     print()
# elif action == "2":
#     print()
# elif action == "3":
#     print()

# action = input("\n1.Bilain \n2.Kyivstar \n3.Vodafon \nВибрати на який оператора телефонують: ")
# if action == "1":
#     print(operator_cost1*number_of_minutes , "грн")
# elif action == "2":
#     print(operator_cost2*number_of_minutes , "грн")
# elif action == "3":
#     print(operator_cost3*number_of_minutes, "грн")
    




# ;  Задание 4
# ; Зарплата менеджера составляет 200$ + процент от про- даж, 
# продажи до 500$ — 3%, от 500 до 1000 — 5%, свыше 1000 — 8%. Пользователь вводит с 
# клавиатуры уровень продаж для трех менеджеров. Определить их зарплату, определить лучшего менеджера, начислить
# ему премию 200$, вывести итоги на экран.


# a = int(input('Введіть продажі 1 менеджера: '))
# b = int(input('Введіть продажі 2 менеджера: '))
# c = int(input('Введіть продажі 3 менеджера: '))
# oklad = 200
# if a>1000:
#    zp1 = oklad+a*0.08
# else:
#    if a <500:
#        zp1 = oklad+a*0.03
#    else:
#        zp1 = oklad+a*0.05
# if b>1000:
#    zp2 = oklad+b*0.08
# else:
#    if b <500:
#        zp2 = oklad+b*0.03
#    else:
#        zp2 = oklad+b*0.05
# if c>1000:
#    zp3 = oklad+c*0.08
# else:
#    if c <500:
#        zp3 = oklad+c*0.03
#    else:
#        zp3 = oklad+c*0.05
# if zp1 > zp2 and zp1 > zp3:
#    print('Лучший по продажам - 1 менеджер!')
#    zp1 += 200
# if zp2 > zp1 and zp2 > zp3:
#    print('Лучший по продажам - 2 менеджер!')
#    zp2 += 200
# if zp3 > zp1 and zp3 > zp2:
#    print('Лучший по продажам - 3 менеджер!')
#    zp3 +=200
# print('Зарплата 1 менеджера ',zp1)
# print('Зарплата 2 менеджера ',zp2)
# print('Зарплата 3 менеджера ',zp3)
