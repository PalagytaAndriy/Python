# Exercise 1
def first():
    str = 'lorem ipsum dolor sit amet, consectetur. Adipiscing elit, sed! do eiusmod tempor incididunt ' \
          'ut labore et dolore magna al1qua. ut enim ad minim veniam, qu2s nostrud, exercitat3on ullamco ' \
          'laboris nisi ut aliquip! ex ea commodo consequat.'
    count = 0

    print('. '.join([i.capitalize() for i in str.split('. ')]))
    print(f'number of digits: {len([i for i in str if i.isdigit()])}')
    print(f'punctuation marks : {len([i for i in str if i == "," or i == "."])}')
    print(f'exclamation points : {len([i for i in str if i == "!"])}')

# Exercise 2
def second():
    num = []
    num.extend(input('Enter your value vio space: ').split(' '))
    secret = input('Please enter your secret number: ')

    print(f'secret number {secret} amount: {len([int(i) for i in num if i == secret])}')

# Exercise 3
def third():
    num = []

    num.extend(input('Enter your value vio space: ').split(' '))

    print(f'sum: {sum([int(i) for i in num])}')
    print(f'avg: {sum([int(i) for i in num]) / len(num)}')