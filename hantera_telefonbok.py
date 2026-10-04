def lägg_till_kontakt(telefonbok, namn, nummer):
    telefonbok[namn] = nummer


def ta_bort_kontakt(telefonbok, namn):
    try:
        del telefonbok[namn]
    except KeyError:
        print("Kontakten finns inte.")


def ändra_nummer(telefonbok, namn, nytt_nummer):
    try:
        telefonbok[namn]
        telefonbok[namn] = nytt_nummer
    except KeyError:
        print("Kontakten finns inte.")

    