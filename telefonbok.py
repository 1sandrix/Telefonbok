def skapa_telefonbok():
    telefonbok = {
        "Jonathan": "070-1234567",
        "Sophie": "070-5432109",
        "Daniel": "070-5555555",
        "Philippe": "070-1111111",
        "Sandra": "070-2222222",
    }
   
    return telefonbok

def sök_telefonnummer(telefonbok, namn):
    try:
        return telefonbok[namn]
    except KeyError:
        return "Kontakten finns inte."

def lista_kontakter(telefonbok):
    for namn in telefonbok:
        print(namn + ": " + telefonbok[namn])



