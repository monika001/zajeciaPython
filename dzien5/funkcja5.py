def wypisz_dane(imie, nazwisko, kurs="Python", ile_dni=15):
    print(f"Kursant {imie} {nazwisko}, kurs: {kurs} trwa {ile_dni} dni.")

wypisz_dane("Monika", "Cz")
wypisz_dane("Anna", "Kowalska", "java")
wypisz_dane("Adam", "Nowak", "JS", 60)
wypisz_dane("Marta", "K", ile_dni=10)
wypisz_dane(ile_dni=20, imie="Jan", nazwisko="Kowalski", kurs="Java")
