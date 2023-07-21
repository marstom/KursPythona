"""
Struktura danych
Dictionary - słownik, hash-tabela hashtable
przechowuje danie klucz-wartość


- klucz musi być niemutowalny

Słownik podobnie jak lista jest MUTOWALNY

"""
slownik = {
    "klucz": "Wartość",
    3: "wartość pod kluczem liczbowym",
    3.14: "asdf"
}
print(slownik)
print(slownik["klucz"])
print(slownik[3])
print(slownik[3.14])

# key error exception
# print(slownik[0])

# TypeError: unhashable type: 'list'
# nieprawidlowy_slownik = {
#     [1,2]: "asdf"
# }
print(hash("asdf"), hash("qwer"), hash("asdf"))

lista = [1, 2, 3]
# hash(lista)


# dictionary
# creating a dictionary
country_capitals = {
    "United States": "Washington D.C.",
    "Italy": "Rome",
    "England": "London"
}

# printing the dictionary
print(country_capitals)

for country in country_capitals:
    print(f"Country: {country} \t|\t capital: {country_capitals[country]}")

# albo items() metoda zwraca tuple(klucz, wartość)
for country, capital in country_capitals.items():
    print(f"Country: {country} \t|\t capital: {capital}")

# przykład, maszyna z batonikami :)
vending_machine = {
    "snickers": 10,
    "bounty": 10,
    "mily-way": 10,
}


def buy_snack(vending_machine, item):
    if vending_machine[item] > 0:
        vending_machine[item] -= 1
    else:
        print(f"Item {item} is out of stock!! Please select other snack.")


print(vending_machine)
for _ in range(15):
    buy_snack(vending_machine, "snickers")
    print(vending_machine)

#
#
#

slownik = {
    "type": "player",
    "person": {"name": "Adam", "age": 32, "items": ["iphone", "headphones"]},
    "missions": ["go to work", "go shopping", "repair a car"],
}

print(slownik["person"]["items"])
print(slownik.get("missions"))
print(slownik.get("unknown key")) # get nie rzuci wyjątku tylko zwróci none
print(slownik.get("unknown key", "")) # można podać co ma zwrócić gdy nie ma klucza np pusty string

slownik["nowy klucz"] = 1234
print(slownik)
slownik["nowy klucz"] = "asdf" # przypisanie pod ten sam klucz nadpisuje go
print(slownik)
print(slownik.get("person").get("age"))

print(len(slownik)) # ilość kluczy w słowniku
slownik.clear() # czyści słownik, usuwa wszystko
print(slownik)

# tworzenie pustego słownika
nowy_slownik = dict()
print(nowy_slownik)


# kolejność elementów
# od pythona 3.7 każdy słownik jest ordered-dict, wcześniej rozkład elementów był nieprzewidywalny
# kolejność elementów jest taka jak podamy
order = {
    "tom": 1,
    "zzz": 22,
    "aaa": 19,
    "qwert": 1,
}
print(order.keys())
print(order)
