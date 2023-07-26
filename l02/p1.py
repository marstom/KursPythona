from math import sqrt


# ! konstrukcja with ... costam, contextmanager

# zwraca domyślnie None
def funkcja():
    pass


print(funkcja())


def funkcja2():
    return 1


print(funkcja2())

# scope zmiennych, ERROR

a = 5


def funkcja3():
    a += 12


# funkcja3()

# można tak...
a = 5


def funkcja3():
    global a
    a += 12


funkcja3()
print(a)

# argument
a = 5


def funkcja3(a):
    a += 12
    return a


result = funkcja3(a)
print(result)
print(a)


# Trójkąt
def triangle(a, b, c):
    """Wzór Herona"""
    area = 0.25 * sqrt((a + b - c) * (a - b + c) * (-a + b + c) * (a + b + c))
    perimeter = a + b + c
    return area, perimeter


area, perimeter = triangle(10, 10, 10)
print(f"Pole: {area}, {perimeter}")


# funkcja może przyjmować dowolny obiekt
def extend_list_sth(lista: list):
    # lista = lista.copy()
    lista.extend(['hej', 'nowe', 'elementy'])


lista = [1, 2, 3]
extend_list_sth(lista)
# bo jest mutowalna!
print(lista)


def average(*args):
    return sum(args) / len(args)


average(1, 2, 3, 4, 5)


def check_number(n):
    if a > 0:
        return "n is psitive"
    elif a == 0:
        return "n is zero"
    else:
        return "n is positive"


check_number(2)


# Fibonacci - (z zadania l01 przekształć)

def fibonacci(how_many):
    fibonacci_numbers = []
    count = 0
    n1 = 0
    n2 = 1
    while count < how_many:
        fibonacci_numbers.append(n1)
        next = n1 + n2
        n1, n2 = n2, next
        count += 1
    return fibonacci_numbers


print(fibonacci(9))
print(fibonacci(3))


# print(fibonacci(-5))


# funkcje wywołane w funkcji

def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def calculator():
    print("Podaj 2 liczby")
    a, b = input().split(' ')
    a, b = int(a), int(b)
    print("Dodawanie (dodaj) czy odejmowanie (odejmij)?")
    operation = input()
    if operation == "dodaj":
        return add(a, b)
    elif operation == "odejmij":
        return sub(a, b)
    else:
        return "Zły typ operacji"


# calculator()

# average salary
employees = [
    ('Eve', 2000),
    ('John', 1500),
    ('Sarah', 1100),
    ('Sarah', 1100),
]


# z list comperhension i bez
def average_salary(employees):
    # sum_of_salaries = 0
    # for employee in employees:
    #     name, salary = employee
    #     sum_of_salaries += salary
    #
    # return sum_of_salaries / len(employees)
    return sum([salary for name, salary in employees]) / len(employees)

print("average salary is : ", average_salary(employees))
