import json
import pickle
import os

USER_FILE_DIRECTORY = 'text'

class Fraction:
    c = 0
    count = 0
    def __init__(self,numerator,denominator):
        self.numerator = numerator
        self.denominator = denominator
        Fraction.count +=1
        self.__class__.c += 1

    @classmethod
    def get_created_instances_count1(cls):
        return cls.c

    @staticmethod
    def get_created_instances_count2():
        return  Fraction.count

    def loading_toJSON(self):
        try:
            if os.path.isfile(f'{USER_FILE_DIRECTORY}.json') and os.access(f'{USER_FILE_DIRECTORY}.json', os.R_OK):
                res = self.unloading_toJSON()
                if str(self.get_created_instances_count2()) in res.keys():
                    print('this fraction exists, dosen\'t load in json')
                    return
                else:
                    res.update({self.get_created_instances_count2():
                                    {'numerator': self.numerator,
                                     'denominator': self.denominator}})
                    with open(f'{USER_FILE_DIRECTORY}.json', 'w') as write_file:
                        json.dump(res, write_file, indent=4, ensure_ascii=False)

            else:
                with open(f'{USER_FILE_DIRECTORY}.json', 'w') as write_file:
                    value = {self.get_created_instances_count2():
                                 {'numerator': self.numerator,
                                  'denominator': self.denominator}}
                    json.dump(value, write_file, indent=4, ensure_ascii=False)
        except  Exception as e:
            print(f'Error: {str(e)}')

    @staticmethod
    def unloading_toJSON():
        try:
            with open(f'{USER_FILE_DIRECTORY}.json', "r") as read_file:
                return json.load(read_file)
        except  Exception as e:
            print(f'Error: {str(e)}')
            return {}

    def loading_toPickle(self):
        try:
            if os.path.isfile(f'{USER_FILE_DIRECTORY}.txt') and os.access(f'{USER_FILE_DIRECTORY}.txt', os.R_OK):
                res = self.unloading_toPickle()
                if self.get_created_instances_count2() in res.keys():
                    print('this fraction exists, dosen\'t load in pickle')
                    return
                else:
                    res.update({self.get_created_instances_count2():
                                    {'numerator': self.numerator,
                                     'denominator': self.denominator}})
                    with open(f'{USER_FILE_DIRECTORY}.txt', 'wb') as write_file:
                        pickle.dump(res, write_file)

            else:
                with open(f'{USER_FILE_DIRECTORY}.txt', 'wb') as write_file:
                    value = {self.get_created_instances_count2():
                                 {'numerator': self.numerator,
                                  'denominator': self.denominator}}
                    pickle.dump(value, write_file)
        except  Exception as e:
            print(f'Error: {str(e)}')

    @staticmethod
    def unloading_toPickle():
        try:
            with open(f'{USER_FILE_DIRECTORY}.txt', "rb") as read_file:
                return pickle.load(read_file)
        except  Exception as e:
            print(f'Error: {str(e)}')
            return {}


f1 = Fraction(1,4)
f1.loading_toJSON()
f1.loading_toPickle()

f2 = Fraction(3,5)
f2.loading_toJSON()
f2.loading_toPickle()

f3 = Fraction(3,4)
f3.loading_toJSON()
f3.loading_toPickle()

print(Fraction.unloading_toJSON())
print(Fraction.unloading_toPickle())