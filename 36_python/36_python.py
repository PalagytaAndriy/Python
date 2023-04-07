import random

def show(func):
    def inner(arr,name):
        func(arr,name)
        for i in range(0, len(arr)):
            print(f'{i + 1}', end='\t')
            for i2 in range(0, len(arr[i])):
                print(f'{arr[i][i2]}', end='\t')
            print()
    return  inner

@show
def sort_first_elem(arr,call):
    print(f'Array sorted {call}')
    arr.sort(key=lambda x: x[0])

@show
def sort_second_elem(arr,call):
    print(f'Array sorted {call}')
    arr.sort(key=lambda x: x[1])

@show
def normal(arr,call):
    print(f'Array {call}')


indef_code = [random.randint(1000,9999) for i in range(0,10)]
tel = ['+380' + str(random.randint(550000000,999999999)) for i in range(0,10)]

books = ['Думай как математик','Формула. Универсальные законы успеха','Формула. Универсальные законы успеха',
         'Рациональность: от ИИ до зомби','Сделай это завтра','Гениально! Инструменты решения креативных задач',
         'Как прожить хорошую жизнь','Атомные привычки','Вы, наверное, шутите, мистер Фейнман?','Размышления']
release_year = [1998,2002,2008,2005,2010,1986,1977,2014,2019,2010]

mixed = [[i,j] for i,j in zip(indef_code,tel)]
lists = [[i,j] for i,j in zip(books,release_year)]

print('Enter the exercise\n'
      '1.Phone number\n'
      '2.Books')

exercise = int(input('Choose: '))

if exercise == 1:
    print('please make a choose\n'
          '1.Sort by identification codes\n'
          '2.Sort by phone numbers\n'
          '3.Display a list of users with codes and phones\n'
          '4.Exit')
elif exercise == 2:
    print('please make a choose\n'
          '1.Sort by books titles\n'
          '2.Sort by books release\n'
          '3.Display a list of users with books titles and books release\n'
          '4.Exit')

choose = int(input('Choose: '))


while choose != 4:
    if choose == 1:
        if exercise == 1:
            sort_first_elem(mixed, 'identification')
        elif exercise == 2:
            sort_first_elem(lists, 'books titles')
        choose = int(input('Choose: '))
    elif choose == 2:
        if exercise == 1:
            sort_second_elem(mixed, 'identification')
        elif exercise == 2:
            sort_second_elem(lists, 'books release')
        choose = int(input('Choose: '))
    elif choose == 3:
        if exercise == 1:
            normal(mixed, 'normal')
        elif exercise == 2:
            normal(lists, 'normal')
        choose = int(input('Choose: '))
else:
    print('Exit')