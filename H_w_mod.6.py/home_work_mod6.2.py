# Задание 1
# Написать рекурсивную функцию нахождения 
# наи- большего общего делителя двух целых чисел.


# def N_o_d(a, b):
#     if b == 0:
#         return a
#     else:
#         return N_o_d(b, a % b)


# result = N_o_d(36, 78)
# print(f"Найбільший загальний дільник: {result}")


# Задание 2
# Написать игру «Быки и коровы». 
# Программа «за- гадывает» четырёхзначное число и играющий должен угадать его.
#  После ввода пользователем числа программа сообщает,
#   сколько цифр числа угадано (быки) и сколько цифр угадано 
#   и стоит на нужном месте (коровы). После отгадывания 
#   числа на экран необходимо вывести коли- чество сделанных 
#   пользователем попыток. В программе необходимо использовать рекурсию.


# import random


# def generate_number():
#     digits = list(range(10))
#     random.shuffle(digits)
#     secret = digits[:4]
#     return secret


# def get_bulls_cows(guess, secret):
#     bulls = 0
#     cows = 0
#     for i in range(4):
#         if guess[i] == secret[i]:
#             bulls += 1
#         elif guess[i] in secret:
#             cows += 1
#     return bulls, cows


# def play_game(secret):
#     attempts = 0
#     while True:
#         guess = input("Введіть чотиризначне число: ")
#         if not guess.isdigit() or len(guess) != 4:
#             print("Будь ласка, введіть чотиризначне число!")
#         else:
#             guess = [int(x) for x in guess]
#             bulls, cows = get_bulls_cows(guess, secret)
#             print(f"{bulls} биків, {cows} корів")
#             attempts += 1
#             if bulls == 4:
#                 print(f"Ви виграли! Кількість спроб: {attempts}")
#                 break


# secret_number = generate_number()
# play_game(secret_number)


# Задание 3
# Дана шахматная доска размером 8×8 
# и шахматный конь. Программа должна запросить 
# у пользователя координаты клетки поля и поставить туда коня. 
# Задача программы найти и вывести путь коня, при котором он обойдет 
# все клетки доски, становясь в каждую клетку только один раз.
#  (Так как процесс отыскания пути для разных началь- ных клеток может затянуться, 
#  то рекомендуется сначала
#  опробовать задачу на поле размером 6×6). 
#  В программе необходимо использовать рекурсию.


# def find_knight_tour(size):
#     board = [[0] * size for _ in range(size)]
#     moves = [(2, 1), (1, 2), (-1, 2), (-2, 1),
#              (-2, -1), (-1, -2), (1, -2), (2, -1)]

#     def is_valid_move(x, y):
#         return 0 <= x < size and 0 <= y < size and board[x][y] == 0

#     def knight_tour(x, y, move_count):
#         board[x][y] = move_count

#         if move_count == size ** 2:
#             return True

#         for dx, dy in moves:
#             next_x = x + dx
#             next_y = y + dy

#             if is_valid_move(next_x, next_y):
#                 if knight_tour(next_x, next_y, move_count + 1):
#                     return True

#         board[x][y] = 0
#         return False

#     for start_x in range(size):
#         for start_y in range(size):
#             if knight_tour(start_x, start_y, 1):
#                 for row in board:
#                     print(row)
#                 return

#     print("Шлях не знайдено!")


# find_knight_tour(6)

# Задание 4
# Написать игру «Пятнашки».






# class FifteenPuzzle:
#     def __init__(self):
#         self.board = [[0] * 4 for _ in range(4)]
#         self.empty_pos = (3, 3)
#         self.moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

#     def initialize_board(self):
#         numbers = list(range(1, 16))
#         random.shuffle(numbers)

#         for i in range(4):
#             for j in range(4):
#                 if i == 3 and j == 3:
#                     self.board[i][j] = 0  # Пуста клітинка позначається 0
#                 else:
#                     self.board[i][j] = numbers.pop()

#     def print_board(self):
#         for row in self.board:
#             print(row)

#     def is_valid_move(self, x, y):
#         return 0 <= x < 4 and 0 <= y < 4

#     def perform_move(self, move):
#         dx, dy = move
#         x, y = self.empty_pos
#         new_x, new_y = x + dx, y + dy

#         if self.is_valid_move(new_x, new_y):
#             self.board[x][y], self.board[new_x][new_y] = self.board[new_x][new_y], self.board[x][y]
#             self.empty_pos = (new_x, new_y)
#             return True
#         else:
#             return False

#     def check_win(self):
#         expected_number = 1

#         for i in range(4):
#             for j in range(4):
#                 if i == 3 and j == 3:
#                     return True
#                 if self.board[i][j] != expected_number:
#                     return False
#                 expected_number += 1

#     def play_game(self):
#         self.initialize_board()

#         while True:
#             print("Поточний стан дошки:")
#             self.print_board()

#             move = input("Введіть хід (left, right, up, down): ")
#             move = move.lower()

#             if move == "left":
#                 move = (0, -1)
#             elif move == "right":
#                 move = (0, 1)
#             elif move == "up":
#                 move = (-1, 0)
#             elif move == "down":
#                 move = (1, 0)
#             else:
#                 print("Недійсний хід! Спробуйте ще раз.")
#                 continue

#             if self.perform_move(move):
#                 if self.check_win():
#                     print("Ви виграли!")
#                     break
#             else:
#                 print("Недійсний хід! Спробуйте ще раз.")


# # Запуск гри
# game = FifteenPuzzle()
# game.play_game()