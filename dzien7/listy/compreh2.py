#kwadraty liczb od 0 do 20

liczby = []

for x in range(21):
    liczby.append(x**2)

print(liczby)

#uzywajac list comprehension:
#jedna linijka kodu

numerki = [x**2 for x in range(21)]

print(numerki)