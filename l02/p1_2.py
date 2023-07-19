"""
Rekurencja /rekursja

"""


# co się stanie?
# Stack Overflow
def recurse():
    recurse()


# recurse()


# silnia - rekursja, stos wywołań
# możesz sprawdzić debuggerem
def factorial(x):
    if x == 1:
        return 1
    else:
        # a = x
        # b = x-1
        result = x * factorial(x - 1)
        return result


print(factorial(6))


# czy ta implementacja jest lepsza? spróbuj  z 6000!
def factorial_no_recursion(number):
    result = 1
    for num in range(1, number + 1):
        result *= num
    return result


print(factorial_no_recursion(6))
