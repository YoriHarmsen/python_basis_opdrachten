# Opdracht 3 condities
# Naam student:
# Groep:
5
normale_toegangsprijs = 12.50
kortings_percentages = {"baby": 100, "kinderen": 50, "volwassenen": 0, "ouderen": 30}
leeftijdsgroepen = {"baby": (0,2), "kinderen": (3,18), "volwassenen": (19,64), "ouderen": (65,150)}

try:
    leeftijd = int(input("Geef uw leeftijd in aantal jaar\n"))
    
    # Bepaal de juiste leeftijdsgroep
    groep = None
    for groepsnaam, (min_leeftijd, max_leeftijd) in leeftijdsgroepen.items():
        if min_leeftijd <= leeftijd <= max_leeftijd:
            groep = groepsnaam
            break
    
    if groep is None:
        print("Ongeldige leeftijd ingevoerd")
    else:
        korting = kortings_percentages[groep]
        eindprijs = normale_toegangsprijs * (1 - korting / 100)
        
        print(f"U behoort tot de groep {groep}")
        print(f"U krijgt {korting}% korting")
        print(f"U betaalt daarom {eindprijs:.2f}")

except ValueError:
    print("Voer een geldig leeftijdsnummer in")