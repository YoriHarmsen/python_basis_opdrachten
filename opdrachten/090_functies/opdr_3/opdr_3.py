# Opdracht 1 functies
# Naam student:
# Groep:


def kubus_vol(m):
    # je code komt hier
    # het woordje pass hieronder kun je weghalen
    pass

def bol_vol(r):
    # je code komt hier
    # het woordje pass hieronder kun je weghalen
    pass

zijde = 5
radius = 4

print(kubus_vol(5))
print(bol_vol(4))

import math

def kubus_vol(zijde):
    """
    Bereken het volume van een kubus.
    :param zijde: Lengte van een zijde van de kubus
    :return: Volume van de kubus
    """
    return zijde ** 3

def bol_vol(straal):
    """
    Bereken het volume van een bol.
    :param straal: Straal van de bol
    :return: Volume van de bol
    """
    return (4/3) * math.pi * (straal ** 3)

# Voorbeeld van gebruik
kubus_volume = kubus_vol(5)
bol_volume = bol_vol(4)

print(f"De inhoud van deze kubus is: {kubus_volume}")
print(f"De inhoud van deze bol is: {bol_volume}")