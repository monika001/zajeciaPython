def pole_kwadratu(bok):
    pole = bok * bok
    return pole

powierzchnia = pole_kwadratu(535)
print(f"Powierzchnia wynosi {powierzchnia}")

#przekazanie funkcji do drugiej funkcji - print:
print(pole_kwadratu(5632))

print(pole_kwadratu)

x = pole_kwadratu
print(x(2))
