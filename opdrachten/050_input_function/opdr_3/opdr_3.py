# Opdracht 3 input functie
# Naam student:
# Groep:


# Vraag de gebruiker om een lijst van minimaal 5 objecten in te voeren
objecten = []

# Vraag de gebruiker om de objecten in te voeren
for i in range(5):
    object = input(f"Voer object {i + 1} in: ")
    objecten.append(object)

# Sorteer de lijst in omgekeerde volgorde
objecten.sort(reverse=True)

# Print de gesorteerde lijst
print(objecten)




