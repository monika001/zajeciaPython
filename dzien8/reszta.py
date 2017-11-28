#napisz program wydajacy resztę z zakupów

#założenie:
#zakupy - wartośc, płacę banknotem
#wydać monetami o nominałach: 5 - 0.1
#jak najmniej monet wydac
#poczakowo ustawiam ilosc monet do wydania na 0,
# bo nie wiem, ile monet bedzie do wydania
monety = {5:0, 2:0, 1:0, 0.5:0, 0.2:0, 0.1:0}

wartosc_zakupow = 11.30
banknot = 20

reszta = banknot - wartosc_zakupow
print("Wydaj: ", reszta)

if reszta < 0:
    print("Za mała wartość banknotu.")
    quit()
elif reszta == 0:
    print("Bez reszty.")
    quit()

#porzadkujemy klucze w slowniku, istotna jest kolejnosc
# w pythonie 3.6 kolejnosc i tak jest zachowana
#nalezaloby osorotwac, uzywajac funkcji lambda
#reszta // moneta - ile monet potrzebujemy do wydania
# np 10 // 5 = 2
#11 // 5 = 2
#formatowanie stringa {}xxx:>4 rownaj do 4 znakow po prawej, < lub ^

for moneta in monety.keys():
    if reszta >= moneta:
        ilosc = reszta // moneta
        monety[moneta] = ilosc
        #na nowow liczymy reszte
        reszta = round(reszta - (moneta * ilosc), 2)
        print("Tyle reszty jeszcze jest: ", reszta)
print("Wydać:")
for moneta, ilosc in monety.items():
    print(f"moneta: {moneta:>4} - {ilosc:>4} sztuk")