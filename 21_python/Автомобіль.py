class Avto:
    def __init__(self, model, rik_vupysky, marka, color, price):
        self.__model = model
        self.__rik_vupysky = rik_vupysky
        self.__marka = marka
        self.__color = color
        self.__price = price

    def info(self):
        return f"{self.__model}, {self.__rik_vupysky}, {self.__marka}, {self.__color}, {self.__price}"


    def __str__(self):
        return f"{self.__model}, {self.__rik_vupysky}, {self.__marka}, {self.__color}, {self.__price}"


    def get_model(self):
        return self.__model

    def set_model(self, model):
        if isinstance(model, str) and 2 < len(model) < 15:
            self.__model = model
        else:
            raise ValueError(f"{model} is wrong model...")


h1 = Avto("BMW", "1990", "e39", "red", "10 000")
h2 = Avto("Honda", "2000", "acord", "green", "12 500")
h3 = Avto("Volvo", "2022", "c90", "red", "25 000")



print(h1.info())
print(h1.get_model())
h1.set_model('Daf')
print(h1)
