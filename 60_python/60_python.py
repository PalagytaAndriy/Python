from abc import ABC,abstractmethod

class IBuilder(ABC):

    @staticmethod
    @abstractmethod
    def build_wall():
        """build wall"""

    @staticmethod
    @abstractmethod
    def build_door():
        """build door"""

    @staticmethod
    @abstractmethod
    def build_window():
        """build window"""

    @staticmethod
    @abstractmethod
    def build_roof():
        """build roof"""

    @staticmethod
    @abstractmethod
    def build_garage():
        """build garage"""

    @staticmethod
    @abstractmethod
    def build_pool():
        """build pool"""

    @staticmethod
    @abstractmethod
    def get_result():
        """return final product"""

class Product:

    def __init__(self):
        self.parts = []

    def add(self,part):
        self.parts.append(part)


class Builder(IBuilder):

    def __init__(self):
        self.product = Product()

    def build_wall(self):
        self.product.add('wall')
        return self

    def build_door(self):
        self.product.add('door')
        return self

    def build_window(self):
        self.product.add('window')
        return self


    def build_roof(self):
        self.product.add('roof')
        return self

    def build_garage(self):
        self.product.add('garage')
        return self

    def build_pool(self):
        self.product.add('pool')
        return self

    def get_result(self):
        return self.product


class Boss:

    def __init__(self):
        self._builder = None

    @property
    def builder(self):
        return  self._builder

    @builder.setter
    def builder(self, builder:Builder):
        self._builder = builder

    @staticmethod
    def construct_house_dream():
        return  Builder().build_roof().build_roof().build_roof().build_roof()\
            .build_window().build_window().build_door().get_result()


    def construct_min_equipment(self):
        return self.builder.\
            build_wall().\
            build_wall().\
            build_wall().\
            build_wall().\
            build_door()

boss = Boss()
builder = Builder()
boss.builder = builder
boss.construct_min_equipment()
print(f'min construct_min_equipment: {", ".join([i for i in boss.builder.product.parts])}')

product1 = Boss.construct_house_dream()
product2= Builder().build_roof().build_roof().build_roof().build_roof()\
    .build_door().build_pool().build_garage().get_result()
print(f'the house consists of {", ".join([i for i in product1.parts])}')
print(f'the house consists of {", ".join([i for i in product2.parts])}')