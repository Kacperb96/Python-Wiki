# Zadanie 1
def dodaj(a, b):
    return a + b

# Zadanie 2
def powitaj(imie):
    return f"Witaj {imie}"

# Zadanie 3
def pole_prostokata(a, b):
    return a * b

# Zadanie 4
def formatuj_imie(imie="nieznajomy"):
    return imie

# Zadanie 5
def policz_srednia(lista):
    return sum(lista)/len(lista)

# Zadanie 6 
def jest_parzysta(n):
    return True if n % 2 == 0 else False

# Zadanie 7
def suma_wszystkiego(*args):
    return sum(args)

# Zadanie 8
def pokaz_profil(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v}")

# Zadanie 9
def dodaj_prefix(prefix, *args):
    lista = []
    for a in args:
        lista.append(prefix + a)
    return lista


# Zadanie 10
dane = [("Anna", 30), ("Jan", 25)]
sortowanko = sorted(dane, key=lambda x: x[1])