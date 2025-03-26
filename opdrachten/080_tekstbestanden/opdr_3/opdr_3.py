# Opdracht 3 Tekst opslaan
# Naam student:
# Groep:

def caesar_encrypt(tekst, verschuiving=5):
    resultaat = ""
    for karakter in tekst:
        if karakter.isalpha():
            # Bepaal basis ('a' voor lowercase, 'A' voor uppercase)
            basis = ord('a') if karakter.islower() else ord('A')
            # Verschuiving toepassen met modulo voor wraparound
            nieuwe_code = (ord(karakter) - basis + verschuiving) % 26 + basis
            resultaat += chr(nieuwe_code)
        else:
            # Behoud niet-alfabetische karakters
            resultaat += karakter
    return resultaat

# Vraag om invoer en toon versleutelde tekst
tekst = input("Geef de tekst die je wilt encrypten..\n")
versleuteld = caesar_encrypt(tekst)
print(versleuteld)

