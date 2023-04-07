import random
sps = [random.randint(-10, 10) for i in range(0, 15)]
print(sps, '\n')

sym = 0
ser = 0
i = 0
j = 0
jj = 0
temp = 0

for i in range(len(sps)):
    sym += sps[i]
ser = sym / len(sps)
print('середне арифметичне = ', ser, '\n')
if ser < 0:
    for j in range((len(sps)-1)//3):
        for jj in range((len(sps) - j - 1)//3):
            if sps[jj]>sps[jj+1]:
                temp = sps[jj]
                sps[jj] = sps[jj+1]
                sps[jj+1] = temp

if ser > 0:
    for j in range(len(sps)-6):
        for jj in range(len(sps) - j - 6):
            if sps[jj]>sps[jj+1]:
                temp = sps[jj]
                sps[jj] = sps[jj+1]
                sps[jj+1] = temp

print(sps)










