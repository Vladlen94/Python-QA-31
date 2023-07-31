# Задание 1
# Реализуйте класс «Автомобиль». Необходимо хранить 
# в полях класса: название модели, год выпуска, производителя,
# объем двигателя, цвет машины, цену. Реализуйте 
# методы класса для ввода данных, вывода данных, 
# реализуйте доступ к отдельным полям через методы класса. 
# К уже реализованному классу «Автомобиль» добавьте 
# конструктор, а также необходимые перегруженные методы


# class Car:
#    def __init__(self, model_name=None, year=None, manufacturer=None, engine_volume=None, color=None, price=None):
#        self.model_name = model_name
#        self.year = year
#        self.manufacturer = manufacturer
#        self.engine_volume = engine_volume
#        self.color = color
#        self.price = price
#    def set_model_name(self, model_name):
#        self.model_name = model_name
#    def set_year(self, year):
#        self.year = year
#    def set_manufacturer(self, manufacturer):
#        self.manufacturer = manufacturer
#    def set_engine_volume(self, engine_volume):
#        self.engine_volume = engine_volume
#    def set_color(self, color):
#        self.color = color
#    def set_price(self, price):
#        self.price = price
#    def get_model_name(self):
#        return self.model_name
#    def get_year(self):
#        return self.year
#    def get_manufacturer(self):
#        return self.manufacturer
#    def get_engine_volume(self):
#        return self.engine_volume
#    def get_color(self):
#        return self.color
#    def get_price(self):
#        return self.price
#    def display_car_info(self):
#        print("Model name:", self.model_name)
#        print("Year:", self.year)
#        print("Manufacturer:", self.manufacturer)
#        print("Engine volume:", self.engine_volume)
#        print("Color:", self.color)
#        print("Price:", self.price)
#    def input_car_info(self):
#        self.set_model_name(input("Enter model name: "))
#        self.set_year(input("Enter year of production: "))
#        self.set_manufacturer(input("Enter manufacturer: "))
#        self.set_engine_volume(input("Enter engine volume: "))
#        self.set_color(input("Enter color: "))
#        self.set_price(input("Enter price: "))




# Задание 2
# Реализуйте класс «Книга». Необходимо хранить в 
# полях класса: название книги, год выпуска, издателя, 
# жанр, автора, цену. Реализуйте методы класса для ввода 
# данных, вывода данных, реализуйте доступ к отдельным 
# полям через методы класса.
# К уже реализованному классу «Книга» добавьте конструктор,
# а также необходимые перегруженные методы.

class Book:
   def __init__(self, book_name=None, year=None, publisher=None, genre=None, author=None, price=None):
       self.book_name = book_name
       self.year = year
       self.publisher = publisher
       self.genre = genre
       self.author = author
       self.price = price
   def set_book_name(self, book_name):
       self.book_name = book_name
   def set_year(self, year):
       self.year = year
   def set_publisher(self, publisher):
       self.publisher = publisher
   def set_genre(self, genre):
       self.genre = genre
   def set_author(self, author):
       self.author = author
   def set_price(self, price):
       self.price = price
   def get_book_name(self):
       return self.book_name
   def get_year(self):
       return self.year
   def get_publisher(self):
       return self.publisher
   def get_genre(self):
       return self.genre
   def get_author(self):
       return self.author
   def get_price(self):
       return self.price
   def display_book_info(self):
       print("Book name:", self.book_name)
       print("Year:", self.year)
       print("Publisher:", self.publisher)
       print("Genre:", self.genre)
       print("Author:", self.author)
       print("Price:", self.price)
   def input_book_info(self):
       self.set_book_name(input("Enter book name: "))
       self.set_year(input("Enter year of publication: "))
       self.set_publisher(input("Enter publisher: "))
       self.set_genre(input("Enter genre: "))
       self.set_author(input("Enter author: "))
       self.set_price(input("Enter price: "))


# Задание 3
# Реализуйте класс «Стадион». Необходимо хранить в 
# полях класса: название стадиона, дату открытия, страну, 
# город, вместимость. Реализуйте методы класса для ввода 
# данных, вывода данных, реализуйте доступ к отдельным 
# полям через методы класса.
# К уже реализованному классу «Стадион» добавьте 
# конструктор, а также необходимые перегруженные методы

# class Stadium:
#    def __init__(self, name='', opening_date='', country='', city='', capacity=0):
#        self.name = name
#        self.opening_date = opening_date
#        self.country = country
#        self.city = city
#        self.capacity = capacity
   
#    def input_data(self):
#        self.name = input("Enter stadium name: ")
#        self.opening_date = input("Enter opening date: ")
#        self.country = input("Enter country: ")
#        self.city = input("Enter city: ")
#        self.capacity = int(input("Enter capacity: "))
   
#    def print_data(self):
#        print(f"Stadium name: {self.name}")
#        print(f"Opening date: {self.opening_date}")
#        print(f"Country: {self.country}")
#        print(f"City: {self.city}")
#        print(f"Capacity: {self.capacity}")
   
#    def get_name(self):
#        return self.name
   
#    def set_name(self, name):
#        self.name = name
   
#    def get_opening_date(self):
#        return self.opening_date
   
#    def set_opening_date(self, opening_date):
#        self.opening_date = opening_date
   
#    def get_country(self):
#        return self.country
   
#    def set_country(self, country):
#        self.country = country
   
#    def get_city(self):
#        return self.city
   
#    def set_city(self, city):
#        self.city = city
   
#    def get_capacity(self):
#        return self.capacity
   
#    def set_capacity(self, capacity):
#        self.capacity = capacity
