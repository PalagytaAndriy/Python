import random

def random_word(arr):
    return random.choice(arr)

def result(guessed_word,attempts,used_letter):
    print(*guessed_word)
    print(f'chance: {attempts}')
    print(f'used letter: {" ".join(used_letter)}')

def check_word(let):
    if word.find(let) >= 0:
        used_letter.append(let)
        for i in [i for i in range(len(word)) if word[i] == let]:
            guessed_word[i] = let
        return 0

    else:
        used_letter.append(let)
        return -1

def restar(word):
    return [['_' for i in range(len(word))],[]]

def print_word():
    print(*guessed_word)
    print(word)

words = ['apple', 'juice', 'morning', 'guese']
word = random_word(words)
attempts = 15
win = 0
guessed_word, used_letter = restar(word)

def main():
    global word,win,attempts,guessed_word,used_letter

    print_word()

    while attempts != 0 and len(words) > 0:
        if ''.join(guessed_word) == word:
            words.remove(word)
            win = win + 1
            print(f'you win: {win}')
            if len(words) == 0:
                break
            else:
                word = random_word(words)
                guessed_word, used_letter = restar(word)
                print_word()

        else:
            guessed_letter = str(input('Enter letter: '))

            if guessed_letter in used_letter:
                print('you used this letter')
                guessed_letter = str(input('Enter letter: '))

            if guessed_letter == word:
                words.remove(word)
                win = win + 1
                print(f'you win: {win}')
                if len(words) == 0:
                    break
                else:
                    word = random_word(words)
                    guessed_word, used_letter = restar(word)
                    print_word()
                    continue

            attempts = attempts + check_word(guessed_letter)

            result(guessed_word, attempts, used_letter)


    else:
        print(f'victory: {win}')
        print('you lose')

if __name__ == '__main__':
    main()