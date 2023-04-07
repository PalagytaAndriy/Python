from abc import ABC, abstractmethod

class CarFactory(ABC):
    @abstractmethod
    def get_body_type(self):
        pass


    @abstractmethod
    def get_hardware(self):
        pass


class Body(ABC):
    @abstractmethod
    def assembly_engine(self):
        pass

    @abstractmethod
    def body_type(self):
        pass



class Hardware(ABC):
    @abstractmethod
    def put_console(self):
        pass

    @abstractmethod
    def assemdly_seats(self):
        pass


class RegularBody(Body):

    def body_type(self):
        print('Hetchbac')

    def assembly_engine(self):
        print('1.2 Motor')


class SportBody(Body):

    def body_type(self):
        print('Sedan')

    def assembly_engine(self):
        print('2.0 Motor')


class StandardHardware(Hardware):

    def put_console(self):
        print('Small Screen with digital speedometer')

    def assemdly_seats(self):
        print('Normal fabric')

class luxuryHardware(Hardware):

    def put_console(self):
        print('Big Screen with digital speedometer')

    def assemdly_seats(self):
        print('Leather fabric')




class FamilyCar(CarFactory):
    def get_hardware(self):
        return StandardHardware()

    def get_body_type(self):
        return RegularBody()


class OutdoorCar(CarFactory):
    def get_hardware(self):
        return StandardHardware()

    def get_body_type(self):
        return SportBody()


class BachelorCar(CarFactory):
    def get_hardware(self):
        return luxuryHardware()

    def get_body_type(self):
        return RegularBody()



class WealthyCar(CarFactory):
    def get_hardware(self):
        return luxuryHardware()

    def get_body_type(self):
        return SportBody()





def prepare_order(customer):
    factories = {
        'Family': FamilyCar(),
        'Outdoor': OutdoorCar(),
        'Bachelor': BachelorCar(),
        'Wealthy': WealthyCar()
    }

    car = factories[customer]
    body = car.get_body_type()
    hard = car.get_hardware()

    body.assembly_engine()
    body.body_type()
    hard.put_console()
    hard.assemdly_seats()

prepare_order('Family')

