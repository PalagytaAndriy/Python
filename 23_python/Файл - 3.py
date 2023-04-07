f1 = open('55.txt', 'r')
f2 = open('55_1.txt', 'w')

row_l = []
for row in f1:
    row_l.append(row)

print(row_l)
print(row_l[-1:])
f2.write(str(*row_l[-1:]))

f1.close()
f2.close()




