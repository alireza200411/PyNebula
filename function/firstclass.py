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
main_list = [1, 6, 89, 91, 56]
newlist = list(map(lambda num: num + 100, main_list))


# ----> Task 07 <----
def operations_math(func, number_list):
    answer_list = [func(number) for number in number_list]
    return answer_list


# ----> Task 08 <----
operators_dic = {
    'add': lambda x, y: x + y,
    'subtraction': lambda x, y: x - y,
    'multiplication': lambda x, y: x * y,
    'division': lambda x, y: x // y,
    'power': lambda x, y: x ** y,

}


def math(operator, num1, num2):
    if operator in operators_dic:
        return operators_dic[operator](num1, num2)
    return "Error: Invalid operator"


# ----> Task 09 <----
def sum_of_calculations(list_, literal):
    return sum([func(literal) for func in list_])


# operators_list = [lambda x: x + 10, lambda x: x - 10, lambda x: x * 10, lambda x: x // 10, lambda x: x ** 3]
# ----> Task 10 <----
def bool_list(func, list_: list):
    return [item if func(item) else None for item in list_]
