
# Задание
# Вывести на экран фигуры, заполненные звездочками. 
# Диалог с пользователем реализовать при помощи меню.




# mat = [[' '] * 7 for _ in range(7)]
# n = input('Введите букву от а до к\n')
# match n:
#    case 'а':
#        for i in range(7):
#            for j in range(7):
#                if (i < j and i < 7 - 1 - j) or (i < j and i > 7 - 1 - j):
#                    mat[i][j] = '*'
#    case 'б':
#        for i in range(7):
#            for j in range(7):
#                if (i > j and i < 7 - 1 - j) or (i > j and i > 7 - 1 - j):
#                    mat[i][j] = '*'
#    case 'в':
#        for i in range(7):
#            for j in range(7):
#                if i < j and i < 7 - 1 - j:
#                    mat[i][j] = '*'
#    case 'г':
#        for i in range(7):
#            for j in range(7):
#                if i > j and i > 7 - 1 - j:
#                    mat[i][j] = '*'
#    case 'д':
#        for i in range(7):
#             for j in range(7):
#                 if (i > j and i > 7 - 1 - j) or (i < j and i < 7 - 1 - j):
#                     mat[i][j] = '*'
#    case 'е':
#        for i in range(7):
#             for j in range(7):
#                 if (i > j and i < 7 - 1 - j) or (i < j and i > 7 - 1 - j):
#                     mat[i][j] = '*'
#    case 'ж':
#        for i in range(7):
#             for j in range(7):
#                 if i > j and i < 7 - 1 - j:
#                     mat[i][j] = '*'
#    case 'з':
#        for i in range(7):
#             for j in range(7):
#                 if i < j and i > 7 - 1 - j:
#                     mat[i][j] = '*'
#    case 'и':
#        for i in range(7):
#             for j in range(7):
#                 if (i < j and i < 7 - 1 - j) or (i > j and i < 7 - 1 - j):
#                     mat[i][j] = '*'
#    case 'к':
#        for i in range(7):
#             for j in range(7):
#                 if (i > j and i > 7 - 1 - j) or (i < j and i > 7 - 1 - j):
#                     mat[i][j] = '*'
#    case _:
#        raise ValueError('по русскому написано, от а до к')
# for i in mat:    print(*i)
