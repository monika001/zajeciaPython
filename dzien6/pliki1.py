sciezka = "tekst1.txt"

plik = open(sciezka, 'r')


print(plik.read())


#trzeba pamietac o zamykaniu plikow, bo sa trzymane w pamieci,
#poki nie zostana zamkniete
plik.close()