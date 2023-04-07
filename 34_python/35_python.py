def show(func):

    def inner(arr):
        print(func(arr))

    return  inner

@show
def cursiv(text):
    return f'\x1B[3m{text}\x1B[3m'

@show
def diff(array):
    return f'even: {[i for i in range(array[0],array[1]) if i%2 == 0]}'

def paint_square(array):
    if array[2] == True:
        for x in range(0, array[0]):
            print( f'{array[1]} ' * array[0])
    elif array[2] == False:
        for x in range(0, array[0]):
            if x == 0 or x == array[0]-1 :
                print( f'{array[1]} ' * array[0])
            else:
                print( f'{array[1]} ' + '  ' * (array[0]-2) + f'{array[1]}')
    else:
        return 'undefine value'

paint_square([5,'@',True])

paint_square([5,'@',False])

@show
def min_value(array):
    return f'min value: {min(array)}'

@show
def products_numbers(array):
    if array[0] > array[1]:  array[0],array[1] = array[1],array[0]
    max = 1
    for i in range(array[0], array[1] + 1):
        max *= i
    return max

@show
def amount_numb(array):
    return f'amount number: {len(str(array))}'

@show
def palindrom(array):
    return 'palindrome' if ''.join(reversed(str(array))) == str(array) else  'no palindrome'


# cursiv('''
# "Don't compare yourself with anyone in this world…
# if you do so, you are insulting yourself."
#                                 Bill Gates
# ''')

# diff([5,20])

# paint_square([5,'@',True])
# print()
# paint_square([5,'@',False])
# min_value([1,2,3,4,5])
#
# products_numbers([5,1])
#
# amount_numb(3456)
#
# palindrom(123321)