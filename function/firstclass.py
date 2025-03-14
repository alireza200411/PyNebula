# ----> Task 01 <----
def quest(name):
    print(f'hello {name}')


def second_function(func):
    return func


# ----> Task 02 <----
def double(number):
    return 2 * number


# ----> Task 03 <----
twofold = lambda y: 2 * y
square = lambda y: y ** 2
cube = lambda y: y ** 3

func_list = [twofold, square, cube]


def runner(number):
    for function in func_list:
        print(function(number))


# ----> Task 04 <----
def counter(func, count, *args):
    for i in range(count):
        func(*args)
    return None


# ----> Task 05 <----
name_list = ['john', 'tom', 'william', 'james', 'oliver', 'henry']
x = list(map(lambda name: name.upper(), name_list))

# ----> Task 06 <----
