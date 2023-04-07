f1 = open('44.txt', 'r')

#def punctuation(word):
 #   from string import punctuation
  #  for punc in punctuation:
   #     if punc in word:
    #        word = word.replace(punc, '')
    #return word


#word_punc = punctuation(word)
row_long = 0
row_str = ''
for row in f1:
    if row_long < len(row):
        row_long = len(row)
        row_str = row
print(row_str, '| - довжина строки - ', row_long)


f1.close()