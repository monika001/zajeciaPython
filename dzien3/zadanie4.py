#po podaniu nazwy miesiaca program napisze ilosc dni w miesiacu

miesiac = input("Podaj nazwę miesiąca: ")

if miesiac == 'kwiecien' or miesiac == 'czerwiec' or miesiac == 'wrzesien' or miesiac == 'listopad':
    print(f"{miesiac} ma 30 dni")

elif miesiac == 'luty':
    print("Luty ma 28 lub 29 dni")

else:
    print(f"{miesiac} ma 31 dni")
