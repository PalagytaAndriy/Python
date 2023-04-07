import time

start_time = time.time()


def decorator_function(func):
    def wrapper(*args):
        print(*func(*args))
        print(f"--- {time.time() - start_time} seconds ---")
    return wrapper

@decorator_function
def return_simple_number(start=2, end=1000):
    if end < start:
        start,end = end, start

    lst = []
    for i in range(start, end + 1):
        for j in range(start, i):
            if i % j == 0:
                break
        else:
            lst.append(i)
    return lst



start, end = [int(input("start n: ")), int(input("end n: "))]
# TODO 0 - 1000
return_simple_number()
# TODO start n -> end n
return_simple_number(start, end)