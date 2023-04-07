import time

def decorator_function(func):
    def wrapper(*args):
        print(*func(*args))
        print(* '       Кінець роботи')
        print(f"************ {time.time()} секунд ***************")
    return wrapper

@decorator_function
def return_pro_number(pochat, kin):
    ls = []
    for i in range(pochat, kin + 1):
        for j in range(pochat, i):
            if i % j == 0:
                break
        else:
            ls.append(i)
    return ls



start = int(input("Початок "
                   "\n --> "))
end = int(input("Кінець "
                "\n --> "))
print(* '\n      Початок роботи')
print(f"************ {time.time()} секунд ***************")
return_pro_number(start, end)