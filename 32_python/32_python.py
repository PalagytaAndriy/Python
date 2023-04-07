local_sum = 0
global_sum = -100000

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

for i in arr:
    local_sum = max(i,local_sum+i)

    global_sum = max(global_sum,local_sum)

print(f'source array: {arr}')
print(f'should be {global_sum}')