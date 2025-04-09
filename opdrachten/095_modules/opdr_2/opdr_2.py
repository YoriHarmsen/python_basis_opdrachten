# Opdracht 1 modules
# Naam student: Yori Harmsen
# Groep: IT2A

# import .....
# for line in open("test.csv", 'rt'):

from my_modules import csv_module

persons = []
with open("voorbeeld.csv", 'rt') as file:
    for line in file:
        lst = csv_module.sanitize(line)
        person = csv_module.create_person(lst)
        person = csv_module.add_fullname(person)
        persons.append(person)

print("Alle personen:")
csv_module.print_persons(persons)

print("\nFilter op achternaam die begint met 'V':")
csv_module.filter(persons, "achternaam", "V")

print("\nFilter op plaats die begint met 'd':")
csv_module.filter(persons, "plaats", "d")