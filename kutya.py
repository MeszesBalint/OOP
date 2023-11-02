class Kutya:
    def __init__(self, nev, uzenet):
        self.nev = nev
        self.uzenet = uzenet

    def ugat(self):
        print(f"{self.nev} mondja: {self.uzenet}")


my_kutya = Kutya("Bodri", "Vau")

my_kutya.ugat()