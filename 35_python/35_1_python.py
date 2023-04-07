import pygame as pg
import pygame.transform

pg.init()

RES = WEDTH, HEIGHT = 700, 700

sc = pg.display.set_mode(RES)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLEDZOLOT = (238, 232, 170)
HOURSE = (255, 0, 0)
OHRA = (160, 82, 45)

FPS = 60

k =[[1,1]]
size = 50
y = 0

clock = pg.time.Clock()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()

    count = 0

    for x in range(1,9):
        for y in range(1,9):
            if (x + y) % 2 == 0:
                pg.draw.rect(sc, BLEDZOLOT, [size * x, size * y, size, size])
            else:
                pg.draw.rect(sc, OHRA, [size * x, size * y, size, size])

    for x in range(len(k)):
        pg.draw.rect(sc, HOURSE, [size * k[x][0], size * k[x][1], size, size])

    # pygame.transform.rotate(sc, -20)
    pygame.transform.rotate(sc, 90)
    pg.display.update()

    clock.tick(FPS)