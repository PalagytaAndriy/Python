word = input("Введіть слово - ")
l = len(word)
for i in range(l // 2):
    if word[i] != word[-1-i]:
        print("Це не паліндром")
        quit()

print("Це  поліндром")
