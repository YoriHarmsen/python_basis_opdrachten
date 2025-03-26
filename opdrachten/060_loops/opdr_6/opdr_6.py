# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

# Hier start de for-loop

my_list = pizzas = ['margharita', 'calzone', 'verdi', 'olivio', 'quattro stagioni']

# Sorteer op alfabet
pizzas.sort()
print(pizzas)

# Voeg pizza toe
pizzas.append('yo-favorito')
print(pizzas)

# Verwijder minst favoriete pizza (olivio)
pizzas.remove('olivio')
print(pizzas)

# Print eerste 3 pizza's
print(pizzas[:3])

# Print middelste pizza
print([pizzas[len(pizzas)//2]])

# Print laatste 3 pizza's
print(pizzas[-3:])