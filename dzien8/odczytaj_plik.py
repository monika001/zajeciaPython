#plik znajduje sie w tym samym folderze co program
import os

file_path = "dane.txt"

#Pierwszy sposob:
if os.path.exists(file_path):
    print("Sciezka istnieje, otwieram plik")
    with open(file_path, 'r') as file:
        print(file.read())
else:
    print("Sciezka nie istnieje!")


#Drugi sposob:
#lepszy ten drugi sposob
