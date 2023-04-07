

def menu():
	global angl
	global franc
	print("\nВаріанти вибора:\n"
	      "1. Добавити \n"
	      "2. Видалити \n"
	      "3. Переклад \n"
	      "4. Заміна \n"
	      "5. Вихід \n")
	print(angl)
	print(franc)
	return input("Зробіть вибір: ")

def add_item():
	global angl
	global franc

	name_an = input("слово англійське - ")
	name_fr = input("слово французьке - ")
	franc[name_fr] = name_an
	angl[name_an] = name_fr


def add_item_new():
	global angl
	global franc

	name_an = input("Введіть нове слово англійське - ")
	name_fr = input("Введіть нове слово французьке - ")
	franc[name_fr] = name_an
	angl[name_an] = name_fr


def main():
	global angl
	global franc
	choose = ''

	while not choose.startswith("5"):
		choose = menu()

		if choose.startswith("1"):
			add_item()

		elif choose.startswith("2"):

			key_delete = ""
			key_delete_2 = ""
			if len(angl) > 0:
				name = input("Введіть слово для видалення - ")
				if name in angl:
					for key, item in angl.items():
						if name == key:
							key_delete = key
							key_delete_2 = item
					angl.pop(key_delete)
					franc.pop(key_delete_2)
					menu()
				else:
					print("Невірне слово")
					main()
				if name in franc:
					for key, item in franc.items():
						if name == key:
							key_delete = key
							key_delete_2 = item
					franc.pop(key_delete)
					angl.pop(key_delete_2)
					menu()

				else:
					print("Невірне слово")
			else:
				print("Список слів - порожній!")

		elif choose.startswith("3"):
			if len(angl) > 0:
				name = input("Введіть слово для перекладу - ")
				if name in angl:
					for key, item in angl.items():
						if name == key:
							print(f'Слово на англійському - {key} --------- Слово на французькому - {item}')
							menu()
				if name in franc:
					for key, item in franc.items():
						if name == key:
							print(f'Слово на французькому - {key} --------- Слово на англійському - {item}')
							menu()

				else:
					print("Невірне слово")
					menu()

			else:
				print("Список слів - порожній!")

		elif choose.startswith("4"):
			if len(angl) > 0:
				name = input("Введіть слово яке замінити - ")
				name_1 = input("Введіть слово НА яке замінити - ")
				if name in angl:
					angl[name_1] = angl.pop(name)
					for key, item in franc.items():
						if name == item:
							franc[key] = name_1
							main()
				if name in franc:
					franc[name_1] = franc.pop(name)
					for key, item in angl.items():
						if name == item:
							angl[key] = name_1

				else:
					print("Невірне слово")

				if name in franc:
					if name in angl:
						franc[name_1] = franc.pop(name)
				else:
					print("Невірне слово")
			else:
				print("Список слів - порожній!")

		elif choose.startswith("5"):
			print('Кінець')
			exit()
		else:
			print("Error..")

angl = {}
franc = {}


main()