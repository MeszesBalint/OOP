class Szam:
    def __init__(self, ertek):
        self.ertek = ertek

    def __str__(self):
        return f"szám: {self.ertek}"

    def __add__(self, masik):
      return Szam(self.ertek + masik.ertek)

szam1 = Szam(9)
szam2 = Szam(10)

print(szam1)
print(szam2)

print("---------------")

szam3 = szam1 + szam2

print(szam3)