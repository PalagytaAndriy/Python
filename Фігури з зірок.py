print('------ а ------')
print()
i = 5
count = 0
while i > 0:
    print('  '*count+'* '*i)
    count +=1
    i -= 1
print()
print('------ б  ------')
print()

i = 0
count = 6
while i < 6:
    print('* '*i+' '*count)
    count -=1
    i += 1
print()
print('------ в ------')
print()

i = 7
count = 0
while i > 0:
    print('  '*count+'* '*i+'  '*count)
    count += 1
    i -= 2
print()
print('------ г  ------')
print()

i = 1
count = 6
while i < 8:
    print('  '*int(count/2)+'* '*i+'  '*int(count/2))
    count -= 2
    i += 2
print()
print('------ д  ------')
print()
i = 7
count = 0
while i > 0:
    print('  '*count+'* '*i+'  '*count)
    count += 1
    i -= 2
j = 1
count = 7
while j < 8:
    print('  '*int(count/2)+'* '*j+'  '*int(count/2))
    count -= 2
    j += 2
print()
print('------ е ------')
print()
i = 9
count = 0
while i > 1:
    print('* '*count+'  '*i+'* '*count)
    count += 1
    i -= 2
j = 1
count = 9
while j < 8:
    print('* '*int(count/2)+'  '*j+'* '*int(count/2))
    count -= 2
    j += 2
print()
print('------ ж ------')
print()
i = 5
count = 0
while i > 0:
    print('* '*count+'  '*i)
    count += 1
    i -= 1
j = 5
count = 0
while j > 0:
    print('* '*j+'  '*count)
    count += 1
    j -= 1
print()
print('------ з ------')
print()
i = 5
count = 0
while i > 0:
    print('  '*i+'* '*count)
    count += 1
    i -= 1
j = 5
count = 0
while j > 0:
    print('  '*count+'* '*j)
    count += 1
    j -= 1
print()
print('------ и ------')
print()
i = 5
count = 0
while i > 0:
    print('* '*i+' '*count)
    count += 1
    i -= 1
print()
print('------ к ------')
print()
i = 1
count = 5
while i < 6:
    print('  '*count+'* '*i)
    count -= 1
    i += 1