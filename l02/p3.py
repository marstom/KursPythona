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


# map

def square(a):
    return a * a


digits = [2, 3, 4, 5, 6, 7, 8]
new_list = list(map(square, digits))
print(new_list)

# filter
# employees = list(zipped)
print(employees)


def select_female_employee(employee):
    return employee[2] == "f"


# funkcja wytwarzająca funkcje
def select_employee_by_gender(gender):
    def inner(employee):
        return employee[2] == gender

    return inner


# uwaga! pierwszy argument musi być funkcją, nie wywołaniem funkcji!
filtered = filter(select_employee_by_gender("f"), employees)
print(list(filtered))
