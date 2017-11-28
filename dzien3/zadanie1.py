#oblicz czy rok jste prestepny
#podzielny przez 4 i niepodzielny przez 100, ale podzielny przez 400

#rok = input("Podaj rok:\n")

#rok = int(rok)

#lub:
rok = int(input("Podaj rok:\n"))

if rok % 400 == 0:
    print(f"Rok {rok} przestepny")

elif rok % 4 == 0 and rok % 100 != 0:
    print(f"Rok {rok} przestepny")
else:
    print(f"{rok} to nie jest rok przestepny")