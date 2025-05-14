import os

# Stap 1: Vraag om de naam van de map
folder_name = input("Geef de naam van de map met afbeeldingen: ")

# Stap 2: Maak een tekstbestand met de bestandsnamen
def generate_file_list(folder_name):
    try:
        # Verkrijg de lijst van bestandsnamen in de map
        files = os.listdir(folder_name)
        with open("bestand_namen.txt", "w") as file:
            for f in files:
                # Schrijf alleen afbeeldingsbestanden naar het bestand
                if f.lower().endswith(('.jpg', '.jpeg', '.png')):
                    file.write(f + "\n")
        print("De bestandsnamen zijn opgeslagen in 'bestand_namen.txt'.")
    except FileNotFoundError:
        print("De opgegeven map bestaat niet.")

# Voer de functie uit
generate_file_list(folder_name)
