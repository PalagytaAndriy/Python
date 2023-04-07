chusla = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
golosni = ['й', 'у', 'е', 'ї', 'і', 'а', 'о', 'є', 'я', 'ю']
prugolosni = ['ц', 'к', 'н', 'г', 'ш', 'щ', 'з', 'х', 'ф', 'в', 'п', 'р', 'л', 'д', 'ж', 'ч', 'с', 'м', 'т', 'б']

f1 = open('33.txt', 'r')


row_1 = 0
letter_1 = 0
letter_chusla = 0
letter_golosni = 0
letter_prugolosni = 0
for row in f1:
    row_1 += 1
    for letter in row:
        letter_1 += 1
        if letter in chusla:
            letter_chusla += 1
        if letter in golosni:
            letter_golosni += 1
        if letter in prugolosni:
            letter_prugolosni += 1

print('Кількість строк - ', row_1)
print('Кількість літер - ', letter_1)
print('Кількість цифр - ', letter_chusla)
print('Кількість голосних - ', letter_golosni)
print('Кількість приголосних - ', letter_prugolosni)

f1.close()


