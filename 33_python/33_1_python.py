from random import random

import requests

full_name= []
resp = requests.get('https://randomuser.me/api/?results=25')
json = resp.json()['results']

i = 0
while i < len(json):
    r_id = random.randint(10000000,10000000000)
    # json[i]['id']['value'] = i  # normal numeration 0 to 24
    # full = str(json[i]['id']['value']).center(20) + " " + json[i]['name']['title'].center(13) +  " " + json[i]['name']['first'].center(15) + " " + json[i]['name']['last'].center(14)
    full = str(json[i]['id']['value'] if json[i]['id']['value'] is not None and json[i]['id']['value'].isdigit() else r_id).center(20)  + " " + json[i]['name']['title'].center(13) + \
           " " + json[i]['name']['first'].center(15)  + " " + json[i]['name']['last'].center(14)


    if json[i]['id']['value'] is None:
        json[i]['id']['value'] = r_id

    full_name.append(full)
    i += 1

print('ID:'.center(20) + 'Title:'.center(15) +  'First:'.center(15) + 'Last:'.center(15))
for i in full_name:
    print(i)

print()
user_to_find = input('enter id: ')
for j in full_name:
    if j.find(user_to_find) > 0:
        print(f'find user : {j}')
        print(f'street: {json[i.find(user_to_find)]["location"]["street"]["name"]} №{json[i.find(user_to_find)]["location"]["street"]["number"]}\n'
              f'city: {json[i.find(user_to_find)]["location"]["city"]}\n'
              f'state: {json[i.find(user_to_find)]["location"]["state"]}\n'
              f'country: {json[i.find(user_to_find)]["location"]["country"]}\n'
              f'email: {json[i.find(user_to_find)]["email"]}\n'
              f'login: {json[i.find(user_to_find)]["login"]["username"]}\n'
              f'password: {json[i.find(user_to_find)]["login"]["password"]}')