a = int(input("Введіть кількість клітинок = "))
shur = 4
vusot = 3
i = 1
j = 1
while i <= vusot:
                i+=1
                j = 1
                while j <= shur:
                              j+=1
                              print('*'*a,'_'*a, end="\t")
                print("\n")

i = 1
j = 1

while i <= vusot:
                i+=1
                j = 1
                while j <= shur:
                              j+=1
                              print('_'*a,'*'*a, end="\t")
                print("\n")