# napis funkcje

napis = 'Ala ma kota.'

napis.upper()
napis.lower()

# funkcja format
napis2 = 'Witaj {name}! Ukończyłeś poziom {level}'
napis2.format(name='Tomasz', level=3)

'Witaj {name}! Ukończyłeś poziom {level}'.format(name='Tomasz', level=12)
'Witaj {}! Ukończyłeś poziom {}'.format("tom", 13)
# dostępne od pythona 3.6
name = 'TOmek'
level = 40
f'Witaj {name}! Ukończyłeś poziom {level}'

# split, zamienia na liste
napis = 'Ala ma kota.'
lista = napis.split(' ')
lista[1], lista[2] = lista[2], lista[1]
'+'.join(lista)

# title, do imienia i nazwiska
'jan kowalski'.title()
'JAN koWaLsKi'.title()

# ZIP (daleka lekcja tam gdzie labdy itp\)
list(zip('ALA MA KOTA HAHA', 'ala ma kota'))

''.join(list(filter(lambda x: x not in ['.', '*'], 'ala.** ..ma..*.. kota.')))
