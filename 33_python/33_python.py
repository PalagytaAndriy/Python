# ls = [0, 7, -5, 1]
# ls1 = ["As","fv","3h","b", "12s", "9l" ]
# ls2 = ["as","Fv","3h","B", "12s", "cl" ]

# print(True if 7 in ls else False)
# print(ls.index(7))
# ls1.sort(key=str.lower)
# ls2.sort()
# print(ls1, '\n', ls2)
# print(ord('A'), ord('a'))

# ls1 = [
# 	[0, 1, 2],
# 	[3, 4, 5],
# 	[6, 7, 8]
# ]
#
# ls2 = [
# 	[0, 1, 2],
# 	[3, 4, 5],
# 	[6, 7, 8]
# ]
#
# ls3 = []
#
# i = 0
# while i < len(ls1):
# 	j = 0
# 	temp = []
# 	while j < len(ls1[i]):
# 		temp.append(ls1[i][j]+ls2[i][j])
# 		j += 1
# 	ls3.append(temp)
# 	i += 1
#
# print(ls3)
# ls1, ls2, ls3 = ls
# print(ls1,ls2,ls3)
# from random import randint

# ls1 = [randint(0, 10) for i in range(0, 10)] # 4,6,8,7,6,5,6,7

# ls2 = [[randint(0, 10) for i in range(0, 10)] for j in range(0,5)] # 4,6,8,7,6,5,6,7
# print(ls2)

# import turtle
# import tkinter # pygame
# import pyqt5
# import json
import random

import requests

response = requests.get("https://randomuser.me/api/?results=25")

users = []

json = response.json()['results']

i = 0
while i < len(json):
	name = json[i]['name']
	original_id = json[i]['id']['value']
	r_id = random.randint(1000, 10000)
	id = str(json[i]['id']['value']).ljust(20) if original_id is not None and original_id.isdigit()  \
		else str(r_id).ljust(20)

	if json[i]["id"]["value"] is None:
		json[i]["id"]["value"] = r_id

	full_name = id + name['title'].ljust(20) + name['first'].ljust(20) + name['last'].ljust(20)
	users.append(full_name)
	i += 1

print("ID".ljust(20) + "Title".ljust(20) + "First".ljust(20) + "Last".ljust(20))
for i in users:
	print(i)

user_to_find = input("Enter id: " )

# Доробити програму - добавити можливість просмотру даних аккаунта по id*
# Користувач вводить id аккаунта та повинен побачити street, city, state, country, email, login, password