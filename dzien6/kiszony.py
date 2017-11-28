#zapisanie do pliku za pomoca pickle

#import modułu pickle
import pickle


baza = [{"imie": "Adam", "nazwisko":"kowalski", "wiek":32},
{"imie": "Anna", "nazwisko":"nowak", "wiek":23},
{"imie": "Jan", "nazwisko":"nowacki", "wiek":34},
{"imie": "Tomasz", "nazwisko":"lato", "wiek":43}]

#zapisujemy
#rozszerzenie nie ma znaczenia
#dump wrzuca do pliku
with open("baza.pickle", 'wb') as plik:
    pickle.dump(baza, plik)

#otwieramy

odczytana_baza = None

#znaki, ktore dostaje, mam rozkodowywac wg utf-8
#wartoto pisac, zaznaczac jakie jest kodowanie, bo w sarszym pythonie jest np kodowanie ascii
#windows moze iec strone kodowa wincp
with open("baza.pickle", "rb") as plik:
    odczytana_baza = pickle.load(plik, encoding="utf-8")

print(odczytana_baza)