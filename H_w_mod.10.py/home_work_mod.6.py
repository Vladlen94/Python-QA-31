# Задание 1
# Напишите функцию, вычисляющую произведение элементов списка целых.
# Список передаётся в качестве па- раметра. Полученный результат возвращается из функции.

# def multiply(x):
#     proizv = 1
#     for el in x:
#         if el !=0:
#             proizv *=el
#     return proizv

# a = [1,2,3,4]     
# print (multiply(a))   



# Задание 2
# Напишите функцию для нахождения минимума в списке целых.
# Список передаётся в качестве параметра. Полученный результат возвращается из функции.


# def _MinList(lst):
#     if len(lst) > 0:
#         _min = lst[0]
#     for i in range(1,len(lst)):
#         if lst[i] < _min:
#             _min = lst[i]
#     return _min

# a = [1,2,3,4]     
# print (_MinList(a))   


# Задание 3
# Напишите функцию, определяющую количество про- стых чисел в списке целых.
# Список передаётся в качестве параметра. Полученный результат возвращается из функции.


# l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
 
 
# def is_prime(number):
#     if number == 1:
#         return True
#     for divider in range(2, number):
#         if number % divider == 0:
#             return False
#     return True
 
 
# primes_count = 0
# for number in l1:
#     primes_count += is_prime(number)
 
# print(primes_count)

# Задание 4
# Напишите функцию, удаляющую из списка целых некоторое заданное число. 
# Из функции нужно вернуть количество удаленных элементов.


# def delete_starting_evens(lst):
#   for i in lst:
#     if i % 2 == 0:
#       lst.remove(i)
#   return lst
 
# print(delete_starting_evens([4, 8, 10, 11, 12, 15]))


# Задание 5
# Напишите функцию, которая получает два списка в 
# качестве параметра и возвращает список, содержащий элементы обоих списков.


# def search_common_elem(a, b):
#     common = []
#     for i in a:
#         if i in b and i not in common:
#             common.append(i)
#     return common


# first = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# second = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# print(search_common_elem(first, second))


# Задание 6
# Напишите функцию, высчитывающую степень каждого элемента списка целых.
# Значение для степени передаётся в качестве параметра, список тоже передаётся в качестве параметра. 
# Функция возвращает новый список, содержа- щий полученные результаты.


# def exponentiate_list(lst, power):
#     return [x ** power for x in lst]

# my_list = [1, 2, 3, 4, 5]
# exponentiated_list = exponentiate_list(my_list, 2)
# print(exponentiated_list)

