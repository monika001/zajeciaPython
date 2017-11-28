#sprawdzić czy liczby sa w podanym zakresie
#na wyjściu:
#x - tak
#y - nie

liczby = [2,4324,25,43,4,5765,756,7,3425,325,364]

#mozna tez zdefiniowac funkcje, ktora bedzie przyjmowac liste, czyli zrobic for'a w funkcji
def czy_w_zakresie(liczba, zakres=range(100)):
    """
Sprawdza czy podana licza jest w zakresie
        :param liczba: liczba, która jest sprawdzana
        :param zakres:
        :return:
        """
    if liczba in zakres:
        print(f"{liczba} - yes")
    else:
        print(f"{liczba} - no")

for x in liczby:
    czy_w_zakresie(x)
