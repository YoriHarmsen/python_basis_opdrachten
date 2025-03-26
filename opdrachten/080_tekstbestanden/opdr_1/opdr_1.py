# Opdracht 1 while-loops
# Naam student:
# Groep:

# Vraag 1: Huidige regering
antwoord1 = input("Wat vind je van de huidige regering?\n")

# Vraag 2: Python-lessen
antwoord2 = input("Wat vind je van de Python-lessen tot nu toe?\n")

# Vraag 3: Mooiste stad
antwoord3 = input("Wat vind jij de mooiste stad van Nederland?\n")

# Opslaan in tekstbestand
with open("enquete_resultaten.txt", "w") as bestand:
    bestand.write("=== Enquête Resultaten ===\n")
    bestand.write(f"1. Huidige regering: {antwoord1}\n")
    bestand.write(f"2. Python-lessen: {antwoord2}\n")
    bestand.write(f"3. Mooiste stad: {antwoord3}\n")

print("Bedankt voor het invullen! De resultaten zijn opgeslagen in enquete_resultaten.txt")