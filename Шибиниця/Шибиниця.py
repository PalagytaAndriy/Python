
def sl():
    global w
    if w == 0:
        print('Ви відгадали слово , переходьте до іншого')
    global pol
    global slova
    global slovo
    global bkv
    import random
    slova = ['мама', 'коза', 'папа', 'нога', 'шнур']
    slovo = random.choice(slova)
    pol = []
    for j in range(len(slovo)):
        pol.append("_")
    print("\n" * 20)
    if w == 0:
        print('Ви відгадали слово , переходьте до іншого')



def wh():
    global w
    global live
    global ii
    global pol
    global bkv
    global slovo
    while ii != 0:
        print(pol)
        print(f'Бали - {live}')
        print(f'Життя - {ii}\n')
        print(f'Букви які не підішли - {bkv}')
        b = str(input('Введіть букву - '))
        print("\n" * 20)
        for j in range(4):
            if slovo[j] == b:
                pol[j] = b
        if b not in slovo:
            bkv.append(b)
        ii -= 1
        j = 0
        w = 0
        for j in range(4):
            if pol[j] == '_':
                w += 1
        if w == 0:
            live += 1
            sl()


j = 0
w = 1
live = 0
bal = 0
ii = 15
bkv = []

sl()
wh()

print("\n"*20)
print('Ви закінчили гру')
print('І ви вгадали  = ', live , ' сліва(ів)')


