"""
napisz skrypt który wydrukuje liczby parzyste do 100
napisz skrypt który wydrukuje liczby nieparzyste do 99
napisz skrypt drukujący n wyrazów ciągu fibonacciego. Ciąg fibonacciego to taki którego następny wyraz równa się aktualny dodać poprzedni. Pierwsze dwa wyrazy to 0, 1
0 1 1 2 3 5 8 13 21 34 ...

Bonus: napisz skrypt sprawdza czy liczba jest liczbą pierwszą czy nie i drukuje odpowiedź na ekran
"""


for i in range(0, 100+2, 2):
    print(i)


for i in range(101):
    if i%2==0:
        print(i)


[i for i in range(101) if i%2!=0]


# prime
liczba = 30

if liczba == 1:
    print("Liczba 1 jest liczbą pierwszą.")
elif liczba > 1:
    for i in range(2, liczba):
        if liczba % i == 0:
            print(f"liczba {liczba} nie jest pierwsza")
            break
    else: # gdy pętla skończy się normalnie bez break
        print(f"Liczba {liczba} jest pierwsza")
else:
    print(f"Liczba {liczba} niej jest liczbą pierwszą.")



# fibonacci

how_many = 12
count = 0
n1, n2 = 0, 1

if how_many <= 0:
    print("Ilość liczb do wydrukowaia musi być większa lub równa zero!")
else:
    while count < how_many:
        print(f"Count {count}: {n1}")
        next = n1 + n2
        n1 = n2
        n2 = next
        count += 1


"""
Mam listę zakupów 'lista_zakupow', zamień ją obiekt typu 'list' posortuj i zapisz jako liste wypisaną od myślników w
formie tekstowej i wydrukuj ją na ekran, ma to wyglądać tak:
- bułki
- jogurt
- kakao
- masło
- sok jabłkowy
- szynka
"""

lista_zakupow = "bułki, masło, jogurt, kakao, szynka, sok jabłkowy"

lista = lista_zakupow.split(", ")
lista.sort()
lista_tekstowa = '\n- '.join(lista)
lista_tekstowa = '- ' + lista_tekstowa
print(lista_tekstowa)


"""
lista zawierająca stan lodówki, połącz
"""