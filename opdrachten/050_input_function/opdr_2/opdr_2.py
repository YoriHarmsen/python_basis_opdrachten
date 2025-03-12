# Opdracht 2 berekeningen
# Naam student:
# Groep:

# Hier komt je code...

# Maak een lege lijst voor gasten
gasten = []

# Maak een lijst met de gasten
gasten = ["Jij", "Paul", "Kees", "Marie", "Hilda"]

# Print de originele gastenlijst
print(gasten)

# Marie belt af, verwijder haar uit de lijst als ze erin staat
if "Marie" in gasten:
    gasten.remove("Marie")

# Print de lijst na het verwijderen van Marie
print(gasten)

# George wil naast Kees zitten, zoek de index van Kees en voeg George toe
if "Kees" in gasten:
    index_kees = gasten.index("Kees")  # Zoek de index van Kees
    gasten.insert(index_kees + 1, "George")  # Voeg George toe naast Kees

# Print de uiteindelijke gastenlijst
print(gasten)

