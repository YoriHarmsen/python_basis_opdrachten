# Opdracht 1 modules
# Naam student:
# Groep:

# import .....
# for line in open("test.csv", 'rt'):
#   jouw code komt hier!

import csv  # Importeren van de csv.py module

def filter(persoon, filterveld, filterwaarde):
    """Filtert de lijst van personen op basis van het opgegeven veld en filterwaarde."""
    gefilterde_personen = []
    for p in persoon:
        # Controleer of het veld begint met de filterwaarde (case-insensitief)
        if p[filterveld].lower().startswith(filterwaarde.lower()):
            gefilterde_personen.append(p)
    return gefilterde_personen

def main():
    bestandspad = 'personen.csv'  # Zorg ervoor dat dit bestand er is

    # Lees de data van het CSV-bestand
    data = csv.lees_csv(bestandspad)
    print("Ingelezen data:")
    for persoon in data:
        print(f"{persoon['voornaam']} {persoon['achternaam']}")

    # Filteren van de data
    filterwaarde = "ja"  # Dit kan je veranderen naar iets anders zoals "Pie" of "d"
    gefilterde_data = filter(data, "voornaam", filterwaarde)

    print(f"\nGefilterde resultaten voor voornaam die begint met '{filterwaarde}':")
    for persoon in gefilterde_data:
        print(f"{persoon['voornaam']} {persoon['achternaam']}")

    # Schrijf de gefilterde data naar een nieuw bestand
    csv.schrijf_csv('gefilterd.csv', gefilterde_data, ['voornaam', 'achternaam', 'plaats'])
    print("\nGefilterde data is geschreven naar 'gefilterd.csv'.")

if __name__ == "__main__":
    main()
