import json


class Shoes:

    def __init__(self, type_shoes=None, view_shoes=None, color=None, price=None, manufacturer=None, size=None):
        self.type_shoes = type_shoes
        self.view_shoes = view_shoes
        self.color = color
        self.price = price
        self.manufacturer = manufacturer
        self.size = size



    def __str__(self):
        return f'type shoes: {self.type_shoes}\n' \
               f'view shoes: {self.view_shoes}\n' \
               f'color: {self.color}\n' \
               f'price: {self.price}\n' \
               f'manufacturer: {self.manufacturer}\n' \
               f'size: {self.size}'

    @staticmethod
    def get_json_request():
        res = []
        with open('request.json', encoding='utf-8') as f:
            data = json.loads(f.read())
            for i in data['stock']:
                res.append(Shoes(i['type shoes'],
                                 i['view shoes'],
                                 i['color'],
                                 i['price'],
                                 i['manufacturer'],
                                 i['size']))
        return res

    @staticmethod
    def load_json_request(shoes):
        with open('request.json','r', encoding='utf-8') as f:
            data = json.loads(f.read())
        new_item = {"type shoes": shoes.type_shoes, "view shoes": shoes.view_shoes,
                    "color": shoes.color, "price": shoes.price, "manufacturer": shoes.manufacturer,
                    "size": shoes.size}
        data['stock'].append(new_item)
        with open('request.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4,ensure_ascii=False)
