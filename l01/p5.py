# krotki! Tuple

t1 = ("apple", "banana", "cherry")
len(t1)

t1 = t1 + ('asadf',)
print(f'id t1: {id(t1)}, {t1}')

# slice - tak samo jak dla list
t1[:2]

t2 = (1, 2, 3)

razem = (*t1, *t2)
razem = t1 + t2
razem
# jak usunąć element z tuple?
# NIE DA SIĘ
razem * 4  # nowa tuple

# iteracja
for el in razem:
    print(el)

sorted(t1)  # wynikiem sortowania jest nowa lista, nie tuple
t2[-1]

# deklarowanie wielu zmiennych
a, b, c = 12, 23, 'tomek'
print(a, b, c)
krotka = 12, 23, 'tomek'
print(krotka)
