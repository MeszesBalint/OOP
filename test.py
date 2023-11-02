class Etel:
    def __init__(self, nev, ar):
        self.nev = nev
        self.ar = ar


etel1 = Etel("pizza", 2000)
etel2 = Etel("keksz", 2200)
etel3 = Etel("csoki", 20000)


class Etterem:
    def __init__(self, nev):
        self.nev = nev
        self.menu = []

    def __str__(self):
        return f"{self.nev}"

    def kiir(self):
        for etel in self.menu:
            print(etel.nev, etel.ar)

    def __add__(self, other):
        self.menu.append(other)

my_etterem = Etterem("Etterem1")
my_etterem.menu = [etel1, etel2, etel3]

print(my_etterem.__str__())
my_etterem.kiir()

while True:
    try:
        uj_etel = str(input("Írj be új ételt: "))
        break
    except ValueError:
        print("Számot nem lehet bele írni")

uj_ar = int(input("Írj be új árat: "))

if uj_ar > 100000 or uj_ar < 0:
    raise ValueError("Nem megfelelő")

uj_etel = Etel(uj_etel, uj_ar)

my_etterem + uj_etel

print("Frissített menü:")
my_etterem.kiir()
