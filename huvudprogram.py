from telefonbok import skapa_telefonbok, sök_telefonnummer, lista_kontakter
from hantera_telefonbok import lägg_till_kontakt, ta_bort_kontakt, ändra_nummer

telefonbok = skapa_telefonbok()

while True:
    print("\nTelefonbok")
    print("1. Visa alla kontakter")
    print("2. Sök telefonnummer")
    print("3. Lägg till kontakt")
    print("4. Ändra nummer")
    print("5. Ta bort kontakt")
    print("6. Avsluta")

    val = input("Välj ett alternativ: ")

    if val == "1":
        lista_kontakter(telefonbok)

    elif val == "2":
        namn = input("Ange namn: ")
        nummer = sök_telefonnummer(telefonbok, namn)
        print(nummer)

    elif val == "3":
        namn = input("Ange namn: ")
        nummer = input("Ange telefonnummer: ")
        lägg_till_kontakt(telefonbok, namn, nummer)
        print("Kontakten har lagts till.")

    elif val == "4":
        namn = input("Ange namn: ")
        nytt_nummer = input("Ange nytt telefonnummer: ")
        ändra_nummer(telefonbok, namn, nytt_nummer)

    elif val == "5":
        namn = input("Ange namn: ")
        ta_bort_kontakt(telefonbok, namn)
    
    elif val == "6":
        print("Programmet avslutas.")
        break
