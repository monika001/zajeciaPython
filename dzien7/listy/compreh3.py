liczby = []

for x in range(21):
    if x % 3 == 0:
        liczby.append(x**2)

print(liczby)

#list comprehension:
#warunek dodaje na końcu
numerki = [x**2 for x in range(21) if x % 3 == 0]

print(numerki)