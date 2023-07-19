# funkcja find
napis4 = 'fasef s a kot wuerouwp kot uqpruwurp pies u kot fhoho haoehow ef kot'

print('start')
found = 0
while 1:
    phrase = 'kot'
    found = napis4.find(phrase, found + 1)
    if found == -1:
        print(f"Found jest równe: {found}")
        break # Wychodzi z nieskończonej pętli
    print(f"Found {napis4[found:found + len(phrase)]} at positoin: {found}")

