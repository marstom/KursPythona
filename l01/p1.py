# operacje
# interaktywny interpreter
from mypy.types import NoneType

# Zmienna
# jak deklarować

# opt/alt + shift + e
a = 2
b = 3

a = 'c'

2 / 3

12 // 3

12 / 3

type(12 // 3)

type(12 / 3)

print('tom')

type(a)

a // b

# operator % to reszta z dzielenia, może się przydać przy sprawdzaniu np czy liczba jest parzysta
print(f"9/2 = {9 // 2} reszta {9 % 2}")
print(f"18/7 = {18 // 7} reszta {18 % 7}")


x = 3
y = 4
a = x / y
print("%d / %d = %.2f liczba" % (x, y, a))
print("{} / {} = {}".format(x, y, a))
print("{arg1} / {arg2} = {wynik}".format(arg1=x, arg2=y, wynik=a))

# od python3.6 dostępny f-string
zmienna = "Hello"
print(f"{x:.2f} / {y} = {a:.4f} {zmienna}, a nawet wyrażenie: {5**3}")



# nic w pythonie to None

# cos = None  # po prostu NULL, jest obiektem NoneType, każda zmienna z None wskazuje na ten sam obiekt



# napisy
'Hello' + ' ' + 'Word'

napis = ''
napis = napis + 'Kurs'
napis = napis + ' '
napis += 'pythona'
print(napis)

napis2 = 'Ala ma kota.'  # 12
len(napis2)
# indexy od zera
napis2[11]

# pierwsze trzy
napis2[:3]

# po 3cim znaku
napis2[3:]
'0123456789...'
'Ala ma kota.'
napis2[4:6]

napis2[11]
napis2[0:12]

napis2[::2]

napis3 = 'Interpretery pythona są dostępne na wiele systemów operacyjnych'
napis3[::2]
napis3[13:20:1]  # pythona
napis3[13:20:2]  # ptoa

# bez ostatnich n
napis3[:-5]

# tylko ostatnie n
napis3[-5:]

# odwrócony napis!!
napis3[::-1]
napis3[::-2]

# znak nowej linii
print("to jest\nnastępna linia\njescze następna.")

# split
napis4 = 'fasef s a kot wuerouwp kot uqpruwurp pies u kot fhoho haoehow ef kot'

podzielony = napis4.split('kot')
print(podzielony)


"id;name;surname;age"
"1;tomek;marszal;35"