# Opdracht 1 functies
# Naam student:
# Groep:


def write_to_file(afile, atext):
    # je code komt hier
    # het woordje pass hieronder kun je weghalen
    pass

my_tekst = "Schrijf dit maar even in een bestandje"
my_file = "test.txt"

def write_to_file(filename, text):
    try:
        with open(filename, "a", encoding="utf-8") as file:  # "a" voor append modus
            file.write(text + "\n")
        print(f"Tekst toegevoegd aan {filename}")
    except Exception as e:
        print(f"Er is een fout opgetreden: {e}")

# Voorbeeld van gebruik
my_tekst = "Schrijf dit maar even in een bestandje"
my_file = "test.txt"
write_to_file(my_file, my_tekst)