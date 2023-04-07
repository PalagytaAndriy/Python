import os.path
import random
from threading import *
import math
user_path = 'test.txt'
if not os.path.exists(user_path):
    print("File not found!")
    exit(0)
def fill():
    with open(user_path, 'w') as f:
        f.write(' '.join([str(random.randint(0, 10)) for _ in range(10)]))
        print("fill  finished")
def find():
    res = []
    with open(user_path, 'r') as f:
        data = f.readlines()
        for i in data:
            num = list(map(int, list(i.replace(' ', ''))))
            for n in num:
                if n % 2 and n % 3 or n == 2 or n == 3 or n == 1:
                    res.append(n)
    with open('find', 'w') as f:
        f.write(' '.join(list(map(str,res))))
        print("is primary  finished")
def fact():
    res = []
    with open(user_path, 'r') as f:
        data = f.readline()
        num = list(map(int, list(data.replace(' ', ''))))
        res = list(map(lambda x: math.factorial(x), num))
    with open('fact', 'w') as f:
        f.write(' '.join(list(map(str,res))))
        print("Factorial finished")
t1 = Thread(target=fill)
t1.start()
t1.join()
t2 = Thread(target=find)
t2.start()
t3 = Thread(target=fact)
t3.start()