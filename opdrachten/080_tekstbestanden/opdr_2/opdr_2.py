# Opdracht 2 tekstbestanden
# Naam student:
# Groep:

import random
prompt = "Raad mijn geheime getal \n"
geheim_getal = random.randint(1, 100)

# opdr_2.py - Raad een nummertje spel
import random

def raad_het_getal():
    # Genereer een willekeurig getal tussen 1 en 100
    geheim_getal = random.randint(1, 100)
    aantal_pogingen = 0
    
    print("Raad mijn geheime getal")
    
    while True:
        try:
            # Vraag om een gok
            gok = int(input("Raad mijn geheime getal\n"))
            aantal_pogingen += 1
            
            # Controleer de gok
            if gok < geheim_getal:
                print("hoger")
            elif gok > geheim_getal:
                print("lager")
            else:
                print(f"Je hebt het getal geraden het is {geheim_getal}!")
                print(f"Je hebt het in {aantal_pogingen} keer gedaan")
                break
                
        except ValueError:
            print("Voer alstublieft een geldig getal in")

# Start het spel
raad_het_getal()

