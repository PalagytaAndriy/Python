### 2 ###
dictionary = {'hello':'bonjur'}

def add_word():
    global dictionary
    english_word = input('Enter a word of english: ')
    french_woed = input('Enter a word of french: ')
    dictionary[english_word] = french_woed

def menu_second():
    print('Choose action:\n'
          '1.Add a word of english and french\n'
          '2.Remove a word of english and french\n'
          '3.Search a word\n'
          '4.Replace a word\n'
          '5.Show dictionary\n'
          '6.Exit')
    return input('Enter choose: ')

def main_second():
    choose = ''
    while not choose.startswith('6'):
        choose = menu_second()
        if choose.startswith('1'):
            add_word()
        elif choose.startswith('2'):
            english_word = input('Enter a word of english: ')
            if english_word in dictionary:
                del dictionary[english_word]
            else:
                print('Unknown english word')
        elif choose.startswith('3'):
            english_word = input('Enter a word of english to search: ')
            if english_word in dictionary:
                print(f'Fiend: \n\t English Word: {english_word} \t French Word: {dictionary[english_word]}')
            else:
                print('Unknown english word')
        elif choose.startswith('4'):
            english_word = input('Enter a word of english to replace: ')
            if english_word in dictionary:
                add_word()
            else:
                print('Unknown english word')
        elif choose.startswith('5'):
            if len(dictionary) > 0:
                for k, v in dictionary.items():
                    print(f'Country: {k}\t Capital: {v}')
        elif choose.startswith('6'):
            print("Good buy")
        else: print('Error')


firma = {
    1:{
        'First Name':'Alex',
        'Last Name': 'Holenko',
        'Tel':'+380986071514',
        'Email':'kek@gmail.com',
        'Post':'Programmer',
        'Number cabinet': '356',
        'Skype':'dek33'
    }

}

def add_person():

    firs_name = input('Enter a firs name: ')
    last_name = input('Enter a last name: ')
    tel = input('Enter a tel number: ')
    email = input('Enter a email: ')
    post = input('Enter a post: ')
    number_cabinet = input('Enter a number cabinet: ')
    skype = input('Enter a skype: ')
    return {'Firs Name':firs_name,'Last Name':last_name,'Tel':tel,'Email':email,'Post':post,'Number cabinet':number_cabinet,'Skype':skype}


def menu_third():
    print('Choose action:\n'
          '1.Add a information of man\n'
          '2.Remove a information of man\n'
          '3.Search a information of man\n'
          '4.Replace a information of man\n'
          '5.Show information of people\n'
          '6.Exit')
    return input('Enter choose: ')

def main_third():
    choose = ''
    while not choose.startswith('6'):
        choose = menu_third()
        if choose.startswith('1'):
            firma[len(firma)+1] = add_person()
        elif choose.startswith('2'):
            last_name = input('Enter a last name: ')
            for k,v in firma.items():
                if last_name in v['Last Name']:
                    del firma[k]
                    break
                else:
                    print('Unknown Last name')
        elif choose.startswith('3'):
            last_name = input('Enter a last name: ')
            for k, v in firma.items():
                if last_name in v['Last Name']:
                    print(f'\nPerson: {k} Info ', end=" ")
                    for k1, v1 in v.items():
                        print(f'\n\t {k1} : {v1}', end=' ')
                    print()
                else:
                    print('Unknown Last name')
        elif choose.startswith('4'):
            last_name = input('Enter a last name: ')
            for k, v in firma.items():
                if last_name in v['Last Name']:
                    firma[k] = add_person()
                else:
                    print('Unknown Last name')
        elif choose.startswith('5'):
            for k,v in firma.items():
                print(f'\nPerson: {k} Info ', end=" ")
                for  k1,v1 in v.items():
                     print(f'\n\t {k1} : {v1}' ,end=' ')
            print()
        elif choose.startswith('6'):
            print("Good buy")
        else:
            print('Error')
if __name__ == '__main__':
    main_second()
    # main_third()