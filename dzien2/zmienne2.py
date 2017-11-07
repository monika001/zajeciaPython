zdanie = "Ala ma kota, kot ma Ale."
zdanie2 = "ja wolę psy!"


#\t, \n - znaki specjalne
moj_plik = "C:\teamwork\nowy_folder\skrypt.py"
moj_plik2 = "C:\\teamwork\\nowy_folder\\skrypt.py"

#r"" - traktuj stringa jak row, wszystkie znaki jako drukowane
moj_plik3 = r"C:\teamwork\nowy_folder\skrypt.py"



print(moj_plik)
print(moj_plik2)
print(moj_plik3)

#wypisanie pintów koło siebie
print(zdanie, end = ' ')
print(zdanie2)

#kub:
print(zdanie + zdanie2)

#lub:
print(zdanie, zdanie2, 65)