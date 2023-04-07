try:
    with open('11.txt', 'r') as f1:
        s1 = f1.readlines()

except:
    print('Помилка при роботі з файлами')

try:
    with open('22.txt', 'r') as f2:
        s2 = f2.readlines()

except:
    print('Помилка при роботі з файлами')

print(s1)
print(s2)
s3 = []
for i in s1:
       if s2.count(i.replace('\n', '')) == 0:
           s3.append(i.replace('\n', ''))
for i in s2:
       if s1.count(i.replace('\n', '')) == 0:
           s3.append(i.replace('\n', ''))

print(s3)

for i in s3:
    if s3.count(i) == 1:
        print(i, '\t')

f1.close()
f2.close()