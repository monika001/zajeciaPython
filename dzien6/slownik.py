elementy = { 0:"ala", 1:"ola", 2:"ela"}

print(elementy)
print(elementy[1])

slownik = {"imie": "Adam", "nazwisko":"kowalski", "wiek":32}

#print(slownik.keys())
#print(slownik.values())

#for klucz, wartosc in slownik.items():
#    print(f"Klucz: {klucz} ma wartość {wartosc}")


#if "adres" in slownik.keys():
#    print("Adres dostępny")
#else:
#    print("Adres niedostępny")

print(slownik)
slownik["adres"] = "Gdańsk"
print(slownik)
#podmiana wartosci Gdańśk na Gdynia
slownik["adres"] = "Gdynia"
print(slownik)