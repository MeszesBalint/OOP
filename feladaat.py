class Etel:
    def __init__(self, nev, ar):
        self.nev = nev
        self.ar = ar

etel1 = Etel("pizza", 2000)
etel2 = Etel("asd", 2200)
etel3 = Etel("awsd", 20000)

class Etterem:
    def __init__(self, nev):
        self.nev = nev
        self.menu = []
    def __str__(self):
        print(f"{self.nev}")

    def kiir(self, menu):
        for etel in menu:
            print(etel)

   # def __add__(self, other):




my_etterem = Etterem("Etterem1")

my_etterem.menu = [etel1, etel2, etel3]

my_etterem.__str__()

my_etterem.kiir()

uj_ar = int(input("Írj be új árat"))

if uj_ar > 100000 or uj_ar < 0:
    raise ValueError("Nem megfelelő")


while True:
    try:
        uj_etel = str(input("Írj be új ételt"))
        break
    except ValueError:
        print("Számot nem lehet bele írni")




