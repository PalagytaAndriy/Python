import random

arr = [random.randint(-10, 10) for i in range(0, 15)]

print(*arr)
print(f'Avg: {sum(arr)/len(arr)}')

rev067 = arr[round(len(arr) * 0.67):].copy()
rev033 = arr[round(len(arr) * 0.33):].copy()

rev067.reverse()
rev033.reverse()

if sum(arr)/len(arr) > 0:
    print('2/3 array:', end=' ')
    [print(i, end=' ') for i in sorted(arr[:round(len(arr) * 0.67)])]
    print(*rev067)

else:
    print('1/3 array:', end=' ')
    [print(i, end=' ') for i in sorted(arr[:round(len(arr) * 0.33)])]
    print(*rev033)