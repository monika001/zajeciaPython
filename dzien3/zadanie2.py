#podane 3 boki trojkata, okresl czymozna zbudowac trojkat
#jeden z bokow musi byc < od sumy pozostalych
#czy jest to trojkat rownoboczny rownoramienny czy rownoboczny

bok_a = int(input("Podaj bok a: "))
bok_b = int(input("Podaj bok b: "))
bok_c = int(input("Podaj bok c: "))

if bok_a < bok_b + bok_c and \
    bok_b < bok_a + bok_c and \
    bok_c < bok_a + bok_b:
    print("Można zbudowac trójkąt")
    if bok_a == bok_b and bok_b== bok_c:
        print("Trójkąt równoboczny")
    elif bok_a == bok_b or bok_a == bok_c or bok_b == bok_c:
        print("Trójkąt równoramienny")
else:
    print("Nie można zbudowac trójkąta")

