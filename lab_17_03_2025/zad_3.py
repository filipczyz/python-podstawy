def prawda_falsz(numer):
    return numer % 2 == 0
numer = 3
czy_numer = prawda_falsz(numer)

if czy_numer:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")