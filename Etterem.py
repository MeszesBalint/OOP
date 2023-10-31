class Ettermek:

    def __init__(self, names, type):
        self.names = names
        self.type = type

my_ettermek = Ettermek("KFC", "Gyors")
class Etterem1(Ettermek):

    def __init__(self, foods, ratings):
        self.foods = foods
        self.ratings = ratings

my_etterem1 = Etterem1("Burgers", ratings=4.5)

class Foods(Etterem1):

    def __init__(self, name):
        self.name = name

my_food = Foods("Zinger")

print(f"{my_ettermek.names}, {my_etterem1.foods}, {my_food.name}")
