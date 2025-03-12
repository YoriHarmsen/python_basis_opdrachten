# Opdracht 2 lists
# Naam student:
# Groep:


rivier_info = {
    "rijn": ["nederland", "duitsland", "Frankrijk"],
    "maas": ["nederland", "belgië", "duitsland"],
    "nijl": ["egypte", "soedan", "oeganda"]
}

rivieren = list(rivier_info.keys())
# rivieren is nu een list met alleen de riviernamen: ['rijn', 'maas', 'nijl']

# Maak een dictionary met rivieren en de landen waar ze doorheen stromen
rivier_info = { 
    "rijn": ["nederland", "duitsland", "frankrijk"], 
    "maas": ["nederland", "belgië", "duitsland"], 
    "nijl": ["egypte", "soedan", "oeganda"] 
}

# Maak een lijst met alleen de riviernamen
rivieren = list(rivier_info.keys())

# Print de naam van de 1e rivier met hoofdletter en het 2e land waar deze doorheen stroomt
print(f"De rivier {rivieren[0].capitalize()} stroomt onder andere door {rivier_info[rivieren[0]][1].capitalize()}")

# Print de naam van de 2e rivier met hoofdletter en het 1e land waar de 1e rivier doorheen stroomt
print(f"De rivier {rivieren[1].capitalize()} stroomt onder andere door {rivier_info[rivieren[0]][0].capitalize()}")

# Print de naam van de 3e rivier met hoofdletter en het 3e land waar deze doorheen stroomt
print(f"De rivier {rivieren[2].capitalize()} stroomt onder andere door {rivier_info[rivieren[2]][2].capitalize()}")
