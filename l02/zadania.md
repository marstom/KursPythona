

1. Napisz funkcje zwracającą liste zawierającą n wyrazów ciągu fibonacciego

2. Lista zakupów od myśliników, poprzednie zadanie domowe, zamień na funkcje która zwraca tekst od myślników

3. Napisać funkcje która zamieni napis "1,2,3,4,5" na liste float'ów [1.0, 2.0 ...]


4. Masz skelp internetowy, klient obsługuje sklep przez terminal
```py 
# dodanie przedmiotu do koszyka
add_to_cart(shopping_cart, 'Shirt', 2, 25.99)

# usuwanie przedmiotu z koszyka
remove_from_cart(shopping_cart, 'Shirt', 1)

# drukowanie zawartości koszyka w formie czytelnej dla użytkownika
print_shopping_cart(shopping_cart)
total_amount = calculate_total(shopping_cart)

```

`shopping_cart` niech będzie na początku pustym słownikiem
`shopping_cart = dict()`

Przykładowy koszyk:
```py
{'Shirt': {'quantity': 1, 'price': 25.99}, 'Jeans': {'quantity': 1, 'price': 49.99}, 'Shoes': {'quantity': 1, 'price': 79.99}}
```
