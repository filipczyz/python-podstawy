def pomnoz_liczby(liczby):
    for i in range(len(liczby)):
        liczby[i] = liczby[i] * 2
    return liczby

liczby = [1, 2, 3, 4, 5]
wynik = pomnoz_liczby(liczby)
print(wynik)


def pomnoz_przez_2(liczby):
    return [liczba * 2 for liczba in liczby]

liczby = [1, 2, 3, 4, 5]
wynik = pomnoz_przez_2(liczby)
print(wynik)