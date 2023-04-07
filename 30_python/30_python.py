import random


array1 = [random.randint(0, 10) for x in range(1, 9)]
array2 = [random.randint(0, 10) for s in range(1, 9)]
# array1 = [1,2,3,3,5] # Example
# array2 = [1,2,3,6,7] # Example

array3 = array1.copy()
array3.extend(array2)

print(f'arr1: {array1}')
print(f'arr2: {array2}')
print(f'arr3: {array3}')
print(f'arr4: {list(set(array3))}')
print(f'arr5: {[i for i in list(set(array1)) if i in list(set(array2))]}')
print(f'arr6 only arr1: {[x for x in array1 if x not in array2]}')
print(f'arr6 only arr2: {[x for x in array2 if x not in array1]}')
print(f'arr7 min arr1: {min(array1)} and max arr1: {max(array1)}')
print(f'arr7 min arr1: {min(array2)} and max arr1: {max(array2)}')