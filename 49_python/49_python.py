class Car:
    count = 0

    def __init__(self, name_model, year_made, manufacturer,engine_volume, color, price):
        self.name_model = name_model
        self.year_made = year_made
        self.__manufacturer = manufacturer
        self.engine_volume = engine_volume
        self.__color = color
        self.price = price
        Car.count += 1
        self.c = Car.count

    def get__color(self):
        return f'new manufacturer: {self.__color}\n'

    def set__color(self,fcolor):
        if isinstance (fcolor, str):
            self.__color = fcolor
        else:
            raise  ValueError(f'{fcolor} id wrong data...')

    def get__mnufacturer(self):
        return  f'new manufacturer: {self.__manufacturer}\n'

    def set__manufacturer(self,fmanufacturer):
        if isinstance (fmanufacturer, str):
            self.__manufacturer = fmanufacturer
        else:
            raise  ValueError(f'{fmanufacturer} id wrong data...')


    def __str__(self):
        return f'Car {self.c}\nModel: {self.name_model}\nYear made: {self.year_made}\nManufacture: {self.__manufacturer}\n' \
               f'Engibe: {self.engine_volume}\nColor: {self.__color}\nPrice: {self.price}\n'

class Book:
    count = 0

    def __init__(self,name_book,year_made,publisher,genre, author, price):
        self.name_book = name_book
        self.year_made = year_made
        self.__publisher = publisher
        self.genre = genre
        self.author = author
        self.__price = price
        Book.count += 1
        self.c = Book.count

    def get__price(self):
        return  f'new price: {self.__price}\n'

    def set__price(self,fprice):
        if isinstance (int(fprice.strip('$')), int):
            self.__price = fprice
        else:
            raise  ValueError(f'{fprice} id wrong data...')

    def get__publisher(self):
        return  f'new price: {self.__publisher}\n'

    def set__publisher(self,fpublisher):
        if isinstance (fpublisher, str):
            self.__publisher = fpublisher
        else:
            raise  ValueError(f'{fpublisher} id wrong data...')


    def __str__(self):
        return f'Book {self.c}\nName book: {self.name_book}\nYear made: {self.year_made}\nPublisher: {self.__publisher}\nGener: ' \
               f'{self.genre}\nAuthor: {self.author}\nPrice: {self.__price}\n'

class Stadium:
    count = 0

    def __init__(self,stadium_name,opening_date,country,city, capacity):
        self.stadium_name = stadium_name
        self.__opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity
        Stadium.count += 1
        self.c = Stadium.count


    def get__opening_date(self):
        return  f'new opening date: {self.__opening_date}\n'

    def set__opening_date(self,fopening_date):
        if isinstance (fopening_date, str):
            self.__opening_date = fopening_date
        else:
            raise  ValueError(f'{fopening_date} id wrong data...')

    def __str__(self):
        return f'Stadium {self.c}\nStadium Name: {self.stadium_name}\nOpening Date: {self.__opening_date}\nCountry: {self.country}\n' \
               f'City: {self.city}\nCapacity: {self.capacity}\n'


c1 = Car('Chevrolet','1992','GM','1,5','Blue','1500$')
c2 = Car('KIA','1998','KIA','2','Red','2500$')
c3 = Car('Niva','2000','ZAZ','2','Gren','500$')

b1 = Book('Pet Sematary','1983','Doubleday','Horror','Stephen King','100$')
b2 = Book('Chalk Man','2018','Doubleday','Thriller ','S. J. Tudor','50$')


s1 = Stadium('Rungrado 1st of May Stadium','1 May 1989','North Korea','Pyongyang','114 000')
s2 = Stadium('Azadi Stadium','17 October 1971','Iran','Teheran','100 116',)

print(c1)
c1.set__manufacturer('GM')
print(c1.get__mnufacturer())
print(f'Change {c1}')

print(c2)
c2.set__color('Gray')
print(c2.get__color())
print(f'Change {c2}')

print(c3)

print(b1)
b1.set__price('120$')
print(b1.get__price())
print(f'Change {b1}')

print(b2)
b2.set__publisher('Duglas')
print(b2.get__publisher())
print(f'Change {b2}')

print(s1)
s1.set__opening_date('28 May 1989')
print(s1.get__opening_date())
print(f'Change {s1}')


print(s2)