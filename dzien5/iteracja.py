#Wypisz na ekranie:
#Przedmiot: x ma indeks nr y

rzeczy = ("pisak", "długopis", "szklanka", "portfel", "myszka", "myszka")
print(rzeczy[0])
#while:
indeks = 0
#oddzielna zmienna dla len,len to funkcja,
# wiec zeby w petli funkcja nie liczyła za każdą iteracją długości petli
#oszczednosc czasu, jesli mam pewnosc, ze dlugosc petli sie nie zmienia
dlugosc = len(rzeczy)

while indeks < dlugosc:
    print(f"Przedmiot: {rzeczy[indeks]} ma indeks nr {indeks}")
    indeks += 1

print(15*"-")

#for:
indeks2 = 0
for rzecz in rzeczy:
    print(f"Przedmiot: {rzecz} ma indeks nr {indeks2}")
    indeks2 += 1

print(15*"-")

#for + enumerate
for indeks3, przedmiot in enumerate(rzeczy):
    print(f"Przedmiot: {przedmiot} ma indeks nr {indeks3}")