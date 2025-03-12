# Opdracht 1 lists
# Naam student:Yori Harmsen                         
# Groep:IT2A

# Maak een lege lijst
personen = []

# Maak 4 dictionaries met gegevens van personen
persoon1 = {"id": 0, "voornaam": "Mark", "achternaam": "De Groot"}
persoon2 = {"id": 1, "voornaam": "Lisa", "achternaam": "Van Dijk"}
persoon3 = {"id": 2, "voornaam": "Tom", "achternaam": "Jansen"}
persoon4 = {"id": 3, "voornaam": "Sophie", "achternaam": "Bos"}

# Voeg de dictionaries toe aan de lijst met extend() of append()
personen.extend([persoon1, persoon2, persoon3, persoon4])

# Print de volledige naam van de 2e persoon
print(f"{personen[1]['voornaam']} {personen[1]['achternaam']}")
