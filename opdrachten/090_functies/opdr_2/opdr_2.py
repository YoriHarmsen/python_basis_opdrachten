# Opdracht 1 functies
# Naam student:
# Groep:


def kilometers_naar_miles(km):
    # je code komt hier
    # het woordje pass hieronder kun je weghalen
    pass

def miles_naar_kilometers(miles):
    # je code komt hier
    # het woordje pass hieronder kun je weghalen
    pass

kilometers = 1223
miles = 867

print(kilometers_naar_miles(kilometers))
print(miles_naar_kilometers(miles))

def kilometers_naar_miles(km):
    """
    Converteert kilometers naar miles.
    :param km: Aantal kilometers
    :return: Aantal miles
    """
    return km / 1.609344

def miles_naar_kilometers(miles):
    """
    Converteert miles naar kilometers.
    :param miles: Aantal miles
    :return: Aantal kilometers
    """
    return miles * 1.609344

# Voorbeeld van gebruik
kilometers = 1223
miles = 867

converted_miles = kilometers_naar_miles(kilometers)
converted_km = miles_naar_kilometers(miles)

print(f"{kilometers} kilometers = {converted_miles} miles")
print(f"{miles} miles = {converted_km} kilometers")