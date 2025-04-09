def lees_csv(bestandsnaam):
    with open(bestandsnaam, 'r') as file:
        regels = file.readlines()
        return [regel.strip().split(',') for regel in regels]