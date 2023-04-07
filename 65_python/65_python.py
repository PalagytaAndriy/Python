import random
import threading
import time


def show(func):

    def inner(*arr):
        print(func(*arr))

    return inner

@show
def random_list(i):
    global rand_ls
    time.sleep(2)
    rand_ls = [random.randint(0,10) for i in range(i)]
    b.wait()
    return f'list: {rand_ls}'

@show
def sum_list():
    global rand_ls
    b.wait()
    return f'Sum: {sum(rand_ls)}'

@show
def avg_list():
    global rand_ls
    b.wait()
    return f'Avg: {sum(rand_ls) / len(rand_ls)}'

b = threading.Barrier(3)
rand_ls = []

t1 = threading.Thread(target=random_list,args=(10,)).start()
t2 = threading.Thread(target=sum_list).start()
t3 = threading.Thread(target=avg_list).start()