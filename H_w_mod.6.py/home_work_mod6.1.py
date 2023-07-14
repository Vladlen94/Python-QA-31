# Задание 1
# Напишите функцию, вычисляющую произведение элементов списка целых. 
# Список передаётся в качестве па- раметра. 
# Полученный результат возвращается из функции.




# def sum_list_s(lst):
#     result=0
#     for num in lst:
#         result += num
#     return result
    


# list=[1,2,3,4,5]
# print(sum_list_s(list))


# Задание 2
# Напишите функцию для нахождения минимума в списке целых. 
# Список передаётся в качестве параметра. 
# Полученный результат возвращается из функции.



# def _MinList(lst):
#    if len(lst) > 0:
#        _min = lst[0]
#    for i in range(1,len(lst)):
#        if lst[i] < _min:
#            _min = lst[i]
#    return _min

# list=[12,32,45,68,11]
# print(_MinList(list))


# def min_of_list(lst):
#     min_num = lst[0]
#     for num in lst:
#         if num < min_num:
#             min_num = num
#     return min_num


# list=[12,32,45,68,11]
# print(min_of_list(list))



# Задание 3
# Напишите функцию, определяющую количество 
# про- стых чисел в списке целых. 
# Список передаётся в качестве параметра. 
# Полученный результат возвращается из функции.


# def count_number(num):
#     num_digits = 0
#     temp = num
#     while temp > 0:
#         temp //= 10
#         num_digits += 1
#     return num_digits


# numbers = count_number(113422)
# print(numbers)



# Задание 4
# Напишите функцию, удаляющую из списка целых некоторое заданное число. 
# Из функции нужно вернуть количество удаленных элементов.


# def remove_elements(nums, target):
#     count = 0  
#     for i in range(len(nums) - 1, -1, -1):
#         if nums[i] == target:
#             del nums[i]
#             count += 1

#     return count


# numbers = [1, 2, 3, 4, 5, 4, 4, 6, 4, 7]
# target_number = 4

# deleted_count = remove_elements(numbers, target_number)
# print("Удалено", deleted_count, "элементов")
# print("Итоговый список:", numbers)







# Задание 5
# Напишите функцию, 
# которая получает два списка в 
# качестве параметра и возвращает список, 
# содержащий элементы обоих списков.

 
# def combine_lists(list1, list2):
#     combined_list = list1 + list2
#     return combined_list


# numbers1 = [1, 2, 3]
# numbers2 = [4, 5, 6]

# combined = combine_lists(numbers1, numbers2)
# print("Объединенный список:", combined)



 
#  Задание 6
# Напишите функцию, 
# высчитывающую степень каждого элемента списка целых. 
# Значение для степени передаётся в качестве параметра, 
# список тоже передаётся в качестве параметра. 
# Функция возвращает новый список, содержа- щий полученные результаты.





# def calculate_power(nums, power):
#     powered_list = [num ** power for num in nums]
#     return powered_list


# numbers = [1, 2, 3, 4, 5]
# exponent = 2

# powered = calculate_power(numbers, exponent)
# print("Результат возведения в степень:", powered)