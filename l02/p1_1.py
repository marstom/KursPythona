# funkcje

# return - ma sens tylko w funkcji, funkcja bez return to to samo co z "return None" albo po prostu return
def nazwa_funkcji():
    # body
    return None


def nazwa_funkcji():
    return


def greet():
    print('Hello World!')

greet()

# argumenty

# function with two arguments
def add_numbers(a, b):
    sum = a + b
    print('Sum: ', sum)


def divide_numbers(a, b):
    div = a / b
    print(f"{a} / {b} = {div}")


divide_numbers(18, 6)
divide_numbers(a=18, b=6)
divide_numbers(b=18, a=6)


# reużywalny kod
def get_square(number):
    return number ** 2


for num in [11, 3, 4, 7, 8]:
    result = get_square(num)
    print(f"Kwadrat {num} = {result}")


# argumenty domyślne
# def draw_rectangle(width=10, height=5):
#     horizontal_line = '+' + '-' * (width - 2) + '+'
#     vertical_line = '|' + ' ' * (width - 2) + '|'
#
#     print(horizontal_line)
#     for _ in range(height - 2):
#         print(vertical_line)
#     print(horizontal_line)
#
# draw_rectangle(height=8)


def display_info(first_name, last_name):
    print('First Name:', first_name)
    print('Last Name:', last_name)


display_info(last_name='John', first_name='Doe')


def three_arguments(a='pierwszy', b='srodkowy', c='ostatni'):
    print(f"{a} {b} {c}")


three_arguments(b='QWERTY')


def find_sum(*numbers):
    result = 0

    for num in numbers:
        result = result + num

    return result


result = find_sum(1, 5, 33, 2, 7, 5, 4, 3)
print("Sum = ", result)


def example(*args):
    # czym są *args, to po prostu tuple!
    print(args)


example('tomek', 1, 2, [2, 3, 4])


# zwracanie wielu argumentów
def basic_math(a, b):
    sum_ = a + b
    mul = a * b
    div = a / b
    return sum_, mul, div


#
print(basic_math(2, 3))  # krotka!
suma, iloczyn, dzielenie = basic_math(8, 6)
print(suma, iloczyn, dzielenie)



# funkcja w funkcji, czasami się przydaje we wzorcu dekorator
def greeting(name):
    def inner():
        print(f"Cześć {name}")

    def inner2():
        print(f"Hejo {name}")

    inner()
    inner2()


greeting("Tomasz")

# funkcja zwracająca funkcje tzw. "Closure"

def generate_power_function(exponent):
    def power(base):
        return base ** exponent
    return power

power = generate_power_function(6)
print(power(3))
print(power(2))
