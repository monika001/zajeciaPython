#lista zawierajaca liczby całkowite od 0 do 20

liczby = []

for x in range(21):
    liczby.append(x)


print(liczby)

#list comprehension
#jesli chcemy uworzyc listez elementami w srodku (range, kwadraty liczb itp)
#to uzywamy ponizszej składni:

numerki = [x for x in range(21)]
print(numerki)