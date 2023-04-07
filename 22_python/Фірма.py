
f1 = open('1_1.txt', 'a')

def menu():
	print("\nВаріанти вибора:\n"
	      "1. Добавити працівника \n"
	      "2. Видалити\n"
	      "3. Пошук\n"
	      "4. Заміна\n"
	      "5. Показати працівників\n"
	      "6. Вихід\n")
	return input("Зробіть вибір: ")


def add_item():
	global works
	global kycha
	global nom

	name = input("П І П - ")
	works["П І П - "] = name
	tel = input("Телефон - ")
	works["Телефон - "] = tel
	email = input("email - ")
	works["email - "] = email
	posada = input("Посада - ")
	works["Посада - "] = posada
	kabinet = input("Помер кабінету - ")
	works["Помер кабінету - "] = kabinet
	skype = input("Skype - ")
	works["Skype - "] = skype

	kycha[f'Працівник № {nom}'] = works.copy()
	nom += 1


def add_item_new():
	global nom
	global works
	global kycha
	name = input("Введіть нове імя - ")
	works["П І П - "] = name
	tel = input("Телефон - ")
	works["Телефон - "] = tel
	email = input("email - ")
	works["email - "] = email
	posada = input("Посада - ")
	works["Посада - "] = posada
	kabinet = input("Помер кабінету - ")
	works["Помер кабінету - "] = kabinet
	skype = input("Skype - ")
	works["Skype - "] = skype

	kycha[f'Працівник № {nom}'] = works.copy()
	nom += 1


def main():
	global works
	global kycha

	choose = ""
	name = ""

	while not choose.startswith("6"):
		choose = menu()

		if choose.startswith("1"):
			add_item()
		elif choose.startswith("2"):
			if len(kycha) == 0:
				print("Список працівників - порожній!")
				main()
			name = input("Введіть імя працівника для видалення - ")
			i = 0

			for key, item in kycha.items():
				if name == item["П І П - "]:
					i = 1
			if i == 0:
				print('Невірне імя')
				main()

			if len(kycha) > 0:

				key_delete = ""
				for key, item in kycha.items():
					if name == item["П І П - "]:
						key_delete = key
				kycha.pop(key_delete)
			else:
				print("Список працівників - порожній!")

		elif choose.startswith("3"):
			if len(kycha) == 0:
				print("Список працівників - порожній!")
				main()
			name = input("Введіть імя для пошуку - ")
			i = 0

			for key, item in kycha.items():
				if name == item["П І П - "]:
					i = 1
			if i == 0:
				print('Невірне імя')
				main()

			if len(kycha) > 0:
				key_posh = ""
				for key, item in kycha.items():
					if name == item["П І П - "]:
						key_posh = key
				print(f"Знайдено:\n\t Імя: {name} \t Деталі: {kycha[key_posh]} ")
			else:
				print("Список працівників - порожній!")

		elif choose.startswith("4"):
			if len(kycha) == 0:
				print("Список працівників - порожній!")
				main()
			name = input("Введіть імя для заміни - ")
			i = 0
			for key, item in kycha.items():
				if name == item["П І П - "]:
					i = 1
			if i == 0:
				print('Невірне імя')
				main()

			if len(kycha) > 0:
				key_zamin = ""
				for key, item in kycha.items():
					if name == item["П І П - "]:
						key_zamin = key
				kycha.pop(key_zamin)
				add_item_new()

			else:
				print("Список працівників - порожній!")

		elif choose.startswith("5"):
			if len(kycha) == 0:
				print("Список працівників - порожній!")
				main()
			if len(kycha) > 0:
				for key, item in kycha.items():
						print(key, item)
						print()
			else:
				print("Список працівників  - порожній!")
		elif choose.startswith("6"):
			print('Кінець')
		else:
			print("Error..")

works = {}
kycha = {}

nom = 1
main()
