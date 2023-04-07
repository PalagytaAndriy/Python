import random
import pygame as pg

pg.init()

RES = WEDTH, HEIGHT = 600,600 # если доска увеличиваться нужно увеличивать размеры

sc = pg.display.set_mode(RES)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLEDZOLOT = (238, 232, 170)
HOURSE = (255, 0, 0)
OHRA = (160, 82, 45)

FPS = 60

sizes = 75
y = 0

clock = pg.time.Clock()


def q(p,s):
    global  step_hours
    global count_options
    if p[0] <= 0 or p[0] > size or p[1] <= 0 or p[1] > size or p not in point: # Выход за границы поля и предыдущий шаг
        p = back_point
        count_options.remove(step_hours) #удаление плохого варианта
    else:
        print(f'{s}:{p}:{step_hours}')
        count_options = [1, 2, 3, 4, 5, 6, 7, 8]
        point.remove(p)#удаление шага с  поля
        steps.append(p)
        s -= 1
    return p,s

size = 6 # размер поля
point = []# масив координат - шахмантая доска
for i in range(1,size+1):
    for j in range(1,size+1):
        point.append([i,j])

steps = [] # Пройденій путь
step = len(point)-1 # Количество возможных шагов
point_horse = point[random.randint(0,step)] # Случайное первое место коня
count_options = [1,2,3,4,5,6,7,8] # Индексы возможных шагов
steps.append(point_horse)
point.remove(point_horse)
print(point)
print(point_horse)



while step >= 0 and len(count_options):# пока есть свободные шаги и есть выбор

    back_point = point_horse #передыдущий шаг
    step_hours = count_options[random.randint(0,len(count_options)-1)]
    if step_hours == 1:
        point_horse,step = q([point_horse[0] - 2, point_horse[1] + 1],step)
    elif step_hours == 2:
        point_horse,step = q([point_horse[0] - 1, point_horse[1] + 2],step)
    elif step_hours == 3:
        point_horse,step = q([point_horse[0] + 1, point_horse[1] + 2],step)
    elif step_hours == 4:
        point_horse,step = q([point_horse[0] + 2, point_horse[1] + 1],step)
    elif step_hours == 5:
        point_horse,step = q([point_horse[0] - 2, point_horse[1] - 1],step)
    elif step_hours == 6:
        point_horse,step = q([point_horse[0] + 1, point_horse[1] - 2],step)
    elif step_hours == 7:
        point_horse,step = q([point_horse[0] - 1, point_horse[1] + 2],step)
    elif step_hours == 8:
        point_horse,step = q([point_horse[0] - 2, point_horse[1] - 1],step)


print('The end')
print(f'Steps taken: {size*size - step}')
print(f'Passed board cells {steps}')
print(f'Free cells of the board{point}')


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()

    count = 0

    for x in range(1,size+1):
        for y in range(1,size+1):
            if (x + y) % 2 == 0:
                pg.draw.rect(sc, BLEDZOLOT, [sizes * x, sizes * y, sizes, sizes])
            else:
                pg.draw.rect(sc, OHRA, [sizes * x, sizes * y, sizes, sizes])

    for x in range(len(steps)):
        pg.draw.rect(sc, HOURSE, [sizes * steps[x][0], sizes * (size + 1 -steps[x][1]), sizes, sizes])

    pg.display.update()
    clock.tick(FPS)