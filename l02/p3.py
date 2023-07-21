"""
zip
map
filter
"""

# zip
names = ["Mark", "John", "Albert", "Ann", "Joe", "Lisa"]
ids = [1, 12, 13, 14, 5, 16, 17]
genders = ["m", "m", "m", "f", "m", "f"]

zipped = zip(names, ids, genders)
print(zipped)
employees = list(zipped)
print(employees)

# przyklad2
zipowane = zip([1, 2, 3], ['a', 'b', 'c'])
print(list(zipowane))


# map

def square(a):
    return a * a


digits = [2, 3, 4, 5, 6, 7, 8]
new_list = list(map(square, digits))
print(new_list)

# filter
# employees = list(zipped)
print(employees)

inty = [1, 2, 5, 6, 7]
floaty = tuple(map(float, inty))
print(floaty)

"""
[('Mark', 1, 'm'), ('John', 12, 'm'), ('Albert', 13, 'm'), ('Ann', 14, 'f'), ('Joe', 5, 'm'), ('Lisa', 16, 'f')]
"""


# funkcja wytwarzająca funkcje
def select_employee_by_gender(gender):
    def inner(employee):
        return employee[2] == gender

    return inner


def select_female_employee(employee):
    return employee[2] == "f"


def filter_by_name_len(employee):
    name, id_, gender = employee
    return len(name) <= 3


# uwaga! pierwszy argument musi być funkcją, nie wywołaniem funkcji!
filtered_gender = filter(select_female_employee, employees)
print(list(filtered_gender))

filtered_name = filter(filter_by_name_len, employees)
print(list(filtered_name))

# funkcje lambda, funkcja anonimowa, pozwala zapisać funkcje w 1 linijce

lista_do_filtrowania = ["a", "ba", "a", "da", "a", "ta", "a", "sa", "qwera", "ha", "hahaha", "ab", "i"]

# Funkcja
# def only_two_letters(word):
#     return len(word) == 2

# filtered = filter(only_two_letters, lista_do_filtrowania)
# można powyższe zapisać w jednej linijce

filtered = filter(lambda word: len(word) == 2, lista_do_filtrowania)
print(list(filtered))

# nie powinno się przypisywać funkcji, lepiej użyć def to tylko przykład
# PEP 8: E731 do not assign a lambda expression, use a def
# funkcja anonimowa przydaje się gdy wiemy że chcemy użyć jej tylko raz
# składnia lambda ..argumenty: to co zwraca
fun = lambda a, b, c: a + b + c
print(fun(1, 2, 3))
print(lambda: "Hello world")
print((lambda: "Hello world")())
