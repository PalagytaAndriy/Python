import json


class Shoes:

    def __init__(self, shoes=None, color=None, price=None, factory=None, size=None):
        self.shoes = shoes
        self.color = color
        self.price = price
        self.factory = factory
        self.size = size



    def __str__(self):
        return f'Модель: {self.shoes}\n' \
               f'Колір: {self.color}\n' \
               f'Ціна: {self.price}\n' \
               f'Виробник: {self.factory}\n' \
               f'Розмір: {self.size}'

    @staticmethod
    def get_json():
        res = []
        with open('sklad.json', encoding='utf-8') as f:
            data = json.loads(f.read())
            for i in data['Магазін']:
                res.append(Shoes(i['Модель'], i['Колір'], i['Ціна'], i['Виробник'], i['Розмір']))
        return res

    @staticmethod
    def load_json(shoes):
        with open('sklad.json', 'r', encoding='utf-8') as f:
            data = json.loads(f.read())
        new_item = {"Модель": shoes.shoes, "Колір": shoes.color, "Ціна": shoes.price, "Виробник": shoes.factory, "Розмір": shoes.size}
        data['Магазін'].append(new_item)
        with open('sklad.json', 'w') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)