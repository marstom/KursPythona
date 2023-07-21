
def count_word_occurrences(text):
    words = text.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

# Example: Counting word occurrences in a text
text = "powtarzamy te same slowa w tekscie ile razy sa te same slowa w tekscie ile asdf asdf asdf qwer asdf"
word_occurrences = count_word_occurrences(text)
print(word_occurrences)


# zad dom
def most_frequent_element(lst):
    element_count = {}

    for element in lst:
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1

    most_frequent = max(element_count, key=element_count.get)
    return most_frequent, element_count[most_frequent]


# Example: Finding the most frequent element in a list
numbers = [1, 3, 5, 3, 2, 1, 4, 3, 2, 3, 4, 2, 5]
most_freq_element, freq_count = most_frequent_element(numbers)
print(f"The most frequent element is {most_freq_element}, occurring {freq_count} times.")





def find_duplicate_elements(input_list):
    element_count = {}
    duplicates = []

    for element in input_list:
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1

    for element, count in element_count.items():
        if count > 1:
            duplicates.append(element)

    return duplicates

# Example: Finding duplicate elements in a list
my_list = [1, 2, 3, 4, 2, 5, 6, 7, 3, 8, 9, 1]
duplicates_list = find_duplicate_elements(my_list)
print("Duplicate elements:", duplicates_list)


"""
Sklep
"""

def add_to_cart(cart, item, quantity, price):
    if item in cart:
        cart[item]['quantity'] += quantity
    else:
        cart[item] = {'quantity': quantity, 'price': price}

def remove_from_cart(cart, item, quantity):
    if item in cart:
        if cart[item]['quantity'] <= quantity:
            del cart[item]
        else:
            cart[item]['quantity'] -= quantity

def calculate_total(cart):
    total = 0
    for item, details in cart.items():
        total += details['quantity'] * details['price']
    return total

# Example: Simulating an online shopping cart
shopping_cart = {}
add_to_cart(shopping_cart, 'Shirt', 2, 25.99)
add_to_cart(shopping_cart, 'Jeans', 1, 49.99)
add_to_cart(shopping_cart, 'Shoes', 1, 79.99)
remove_from_cart(shopping_cart, 'Shirt', 1)

print("Current Shopping Cart:")
for item, details in shopping_cart.items():
    print(f"{item}: Quantity={details['quantity']}, Price=${details['price']}")

total_amount = calculate_total(shopping_cart)
print(f"\nTotal Amount: ${total_amount:.2f}")
print(shopping_cart)