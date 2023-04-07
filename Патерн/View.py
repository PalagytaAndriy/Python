def index():
    print('MVC - siple exemple test - index')
    print('Press [y] to see data from database, [n] - exit :')

def person(ls):
    print(f'Data from db, we have {len(ls)} persons. '
          f'Here they are: ')
    for item in ls:
        print(item)

def endView():
    print('Goodbye')