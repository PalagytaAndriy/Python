

class Stack:
    def __init__(self):
        self.list = list()

    def add(self, x):
        self.list.append(x)


    def empt(self):
        if len(st.list) != 0:
            print('\nСтек НЕ пустий\n')
        else:
            print('\nСтек пустий\n')

st = Stack()

while True:
    print('1.Розміщення рядка у стеку\n'
          '2.Виштовхування рядка зі стеку\n'
          '3.Підрахувати кількість рядків у стеку\n'
          '4.Перевірити чи повний стек\n'
          '5.Очистити стек\n'
          '6.Отримати значення без виштовхування верхнього рядка зі стеку\n'
          '7.Вивисти стек\n'
          '8.Вихід\n')
    n = input(str('Ваш вибір\n '
                  ' --> '))
    if n == '8':
        exit()

    if n == '1':
        p = input('Введіть те що буде відображено у добаленому рядку стеку\n'
                  ' --> ')
        st.add(p)

    if n == '7':
        if len(st.list) != 0:
            for i in st.list:
                print(i, ' --> ', end=' ')
        else:
            print('\nСтек пустий\n')
    print('\n')

    if n == '3':
        print(f'Кількісь рядків у стеку --> {len(st.list)}\n')

    if n == '2':
        if len(st.list) != 0:
            st.list.pop()
            print('------- Готово --------')
        else:
            print('\nСтек пустий\n')

    if n == '4':
        st.empt()

    if n == '6':
        print(f'останне значення у стеку --> ', *st.list[-1:], '\n')






