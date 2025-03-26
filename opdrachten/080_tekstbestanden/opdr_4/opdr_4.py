# Opdracht 4 Tekst opslaan
# Naam student:
# Groep:

# party_organisatie.py - Feestgangers bevragen en opslaan

# Lijst met vragen
vragen = [
    "Wat is je voornaam?",
    "Wat is je achternaam?",
    "Wat neem je mee aan drank?",
    "Wat neem je mee om te eten?"
]

def vraag_feestganger():
    antwoorden = {}
    print("Vul de vragenlijst in:")
    
    for i, vraag in enumerate(vragen, 1):
        antwoord = input(f"{i}. {vraag}\n")
        sleutel = ""
        if i == 1:
            sleutel = "voornaam"
        elif i == 2:
            sleutel = "achternaam"
        elif i == 3:
            sleutel = "drank"
        elif i == 4:
            sleutel = "eten"
        antwoorden[sleutel] = antwoord
    
    print("\nBedankt voor het invullen!")
    print("See you at the party.\n")
    return antwoorden

def bewaar_gegevens(gast, bestandsnaam="feestgangers.txt"):
    with open(bestandsnaam, "a") as bestand:
        bestand.write("----\n")
        for key, value in gast.items():
            bestand.write(f"{key}: {value}\n")
        bestand.write("\n")

# Hoofdprogramma
while True:
    gast = vraag_feestganger()
    bewaar_gegevens(gast)
    
    nog_een = input("Nog een feestganger toevoegen? (j/n) ").lower()
    if nog_een != 'j':
        break

print("Feestregistratie voltooid. Check feestgangers.txt!")
