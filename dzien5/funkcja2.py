#funkcja przyjmujaca argument

def print_greeting(name):
    print(f"Hello my name is {name.capitalize()}")

print_greeting("monika")
print_greeting("jan")
print_greeting("kasia")

imie = input("Podaj imię:")

print_greeting(imie)