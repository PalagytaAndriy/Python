from abc import ABC, abstractmethod

class AbstractCar(ABC):
    @abstractmethod
    def get_body_type(self):
        pass



class SedanCar(AbstractCar):

    def __init__(self):
        self.body = 'sedan'

    def get_body_type(self):
        return f"Body type: {self.body}"


class HatchbeckCar(AbstractCar):

    def __init__(self):
        self.body = 'hatchbeck'

    def get_body_type(self):
        return f"Body type: {self.body}"


class PicupCar(AbstractCar):

    def __init__(self):
        self.body = 'picup'

    def get_body_type(self):
        return f"Body type: {self.body}"


class CarFactory():
    @staticmethod
    def buil_car(type):
        try:
            if type == 'sedan':
                return SedanCar()
            elif type == 'hatchbeck':
                return HatchbeckCar()
            elif type == 'picup':
                return PicupCar()
            raise AssertionError('Type is not valid')
        except AssertionError as e:
            print(e)


list_type = ['sedan', 'picup', 'sedan', 'hatchbeck', 'jeep']
for t in list_type:
    car = CarFactory.buil_car(t)
    body = car.get_body_type()
    print(body)







