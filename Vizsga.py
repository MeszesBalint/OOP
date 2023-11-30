"""
Név: Meszes Imre Bálint
Szak: MI
Neptun azonosító: C2SOWJ


1. Mi az objektumorientált programozás alapegysége?
a) Függvény
b) Objektum
c) Változó
d) Ciklus
Válasz: Objektum


2. Mit jelent a 'self' kulcsszó egy osztály metódusán belül Pythonban?
a) Az osztályt magát
b) Az osztály egy példányát
c) A metódust magát
d) A futtató környezetet
Válasz: Az osztály egy példányát


3. Melyik NEM tartozik a Pythonban az objektumorientált programozás alapvető jellemzői közé?
a) Egységbezárás
b) Modulok
c) Öröklődés
d) Polimorfizmus
Válasz: Modulok


4. Mire szolgál az init metódus Pythonban?
a) Egy osztály törlésére
b) Egy osztály példányának inicializálására
c) Az osztály statikus metódusainak definiálására
d) Egy osztály metódusainak futtatására
Válasz: Egy osztály példányának inicializálására


5. Mi a célja az absztrakt osztályoknak Pythonban?
a) Egy osztály teljes funkcionalitásának megvalósítása
b) Egy osztály öröklésének megakadályozása
c) Egy osztály példányosításának lehetővé tétele
d) Egy osztály öröklési szerkezetének és alapvető viselkedésének definiálása
Válasz: Egy osztály öröklési szerkezetének és alapvető viselkedésének definiálása


6. Mi az eredménye az alábbi Python kód futtatásának?

class Animal:
   def speak(self):
   print("Animal speaks")
class Dog(Animal):
  def speak(self):
  print("Dog barks")

d = Dog()
d.speak()

a) Animal speaks
b) Dog barks
c) Semmi, hiba lép fel
d) A kód nem fut le
Válasz: Semmi, hiba lép fel mert a print előtt nincs még egy space.


7. Melyik NEM egy valós Python adattípus?
a) list
b) tuple
c) Linked list
d) dictionary
Válasz: Linked list


8. Mit jelent a Pythonban az egységbezárás (encapsulation)?
a) Az adatok elrejtése közvetlen hozzáféréstől
b) Egy függvény többszörös meghívása
c) Az osztálypéldányok többszörös létrehozása
d) Az adatok megosztása minden osztálypéldány között
Válasz: Az adatok elrejtése közvetlen hozzáféréstől


9. Mi a helyes módja az osztálypéldány attribútumának elérésének Pythonban?
a) Class>attribute
b) Class->attribute
c) Class::attribute
d) instance.attribute
Válasz: instance.attribute


10. Melyik Python kulcsszót használjuk az öröklődés megvalósításához?
a) extends
b) implements
c) inherits
d) class Child(Parent):
Válasz: class Child(Parent):


11. Mi a feladata a super() függvénynek?
a) Az aktuális osztály szuperosztályának metódusainak hívása
b) Az aktuális osztály törlése
c) Az összes osztálypéldány törlése
d) A program gyorsítása
Válasz: Az aktuális osztály szuperosztályának metódusainak hívása


12. Mikor használjuk a 'pass' kulcsszót Pythonban?
a) Az osztályok és függvények konkrét implementációjának írásához
b) Egy függvény vagy osztály azonnali végrehajtásához
c) Egy hurok vagy feltétel azonnali befejezéséhez
d) Egy üres blokk megadásához, ahol a kód még nem került implementálásra
Válasz: Egy üres blokk megadásához, ahol a kód még nem került implementálásra


13. Melyik a helyes módja egy osztálypéldány metódusának meghívásának?
a) classname.methodname()
b) classname->methodname()
c) methodname(classname)
d) instance.methodname()
Válasz: instance.methodname()


14. Mi történik, ha egy osztályban nem definiáljuk a __init__ metódust?
a) A program hibát generál
b) Az osztály nem használható
c) Az osztály automatikusan kap egy alapértelmezett __init__ metódust
d) Az osztály minden metódusa hibás lesz
Válasz: Az osztály automatikusan kap egy alapértelmezett __init__ metódust


15. Mi a szerepe az objektumorientált programozásban a polimorfizmusnak?
a) Azonos interfész megvalósítása különböző osztályok által
b) Az objektumok létrehozásának automatizálása
c) Különböző osztályok közötti adatátvitel megkönnyítése
d) Az öröklődési hierarchia egyszerűsítése
Válasz: Azonos interfész megvalósítása különböző osztályok által


16. Mi az a tervezési minta (design pattern) a szoftverfejlesztésben?
a) Egy programozási nyelv
b) Egy konkrét kódreszlet, amelyet minden programban fel lehet használni
c) Egy megoldási sablon gyakori problémákra
d) Egy szoftverfejlesztési metodológia
Válasz: Egy megoldási sablon gyakori problémákra

17. Mi a Gang of Four (GoF) hozzájárulása a szoftvertervezéshez?

a) A Python programozási nyelv megalkotása
b) Az első operációs rendszer fejlesztése
c) A tervezési minták gyűjteményének létrehozása
d) A leggyorsabb számítógép megépítése
Válasz: A tervezési minták gyűjteményének létrehozása

18. Mi az OOP célja az alábbiakból?
a) Adatbázis kezelés
b) Eljárási, procedurális programozás kiegészítése
c) Alacsony szintű memóriakezelés
d) Grafikus felhasználói felület kialakítása
Helyes válasz: Eljárási, procedurális programozás kiegészítése

19. Mi a "class" kulcsszó szerepe Pythonban?
a) Fájl kezelés
b) Modul importálás
c) Osztály létrehozása
d) Függvény definiálás
Helyes válasz: Osztály létrehozása

20. Mire használjuk az öröklődést (inheritance) az OOP-ban?
a) Kódmegosztás és újrafelhasználhatóság
b) Memóriakezelés optimalizálása
c) Fájlkezelés egyszerűsítése
d) Végtelen ciklusok elkerülése
Helyes válasz: Kódmegosztás és újrafelhasználhatóság
"""
from abc import ABC, abstractmethod
from datetime import datetime

class Szoba(ABC):
    @abstractmethod
    def __init__(self, ar, szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam

class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(5000, szobaszam)

class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(8000, szobaszam)

class Foglalas:
    def __init__(self, szoba, nap):
        self.szoba = szoba
        self.nap = nap


class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []

    def inditas(self):
        szoba1 = EgyagyasSzoba(1)
        szoba2 = KetagyasSzoba(2)
        szoba3 = EgyagyasSzoba(3)

        self.szobak.extend([szoba1, szoba2, szoba3])

        self.foglalas(szoba1, "2024-06-01")
        self.foglalas(szoba2, "2024-05-13")
        self.foglalas(szoba3, "2024-03-30")
        self.foglalas(szoba1, "2024-04-10")
        self.foglalas(szoba2, "2024-02-06")

    def foglalas(self, szoba, nap):
        ma = datetime.now().strftime("%Y-%m-%d")
        if nap <= ma:
            return "A foglalás dátuma nem lehet a mai napnál korábbi."

        for foglalas in self.foglalasok:
            if foglalas.szoba == szoba and foglalas.nap == nap:
                return "A szoba ezen a napon nem elérhető."

        foglalas = Foglalas(szoba, nap)
        self.foglalasok.append(foglalas)
        return szoba.ar

    def lemondas(self, foglalas):
        if foglalas in self.foglalasok:
            self.foglalasok.remove(foglalas)
            return "A foglalás lemondva."
        else:
            return "A foglalás nem található."

    def foglalasok_listazasa(self):
        for foglalas in self.foglalasok:
            print(f"Szoba száma: {foglalas.szoba.szobaszam}, Nap: {foglalas.nap}")

    def futtat(self):
        while True:
            print("1. Foglalás")
            print("2. Lemondás, előtte ajánlott listázni")
            print("3. Foglalások listázása")
            print("4. Kilépés")

            valasztas = input("Írja be a választott művelet számát: ")

            if valasztas == "1":
                self.foglalas_menu()
            elif valasztas == "2":
                self.lemondas_menu()
            elif valasztas == "3":
                self.foglalasok_listazasa_menu()
            elif valasztas == "4":
                break
            else:
                print("Érvénytelen választás. Válasszon újra.")

    def foglalas_menu(self):
        szoba_szam = input("Adja meg a foglalandó szoba számát: ")
        foglalas_datum = input("Adja meg a foglalás dátumát (YYYY-MM-DD): ")

        szoba = self.szoba_kereses(int(szoba_szam))
        if szoba:
            ar = self.foglalas(szoba, foglalas_datum)
            print(f"Az ár: {ar}")
        else:
            print("Érvénytelen szoba szám.")

    def lemondas_menu(self):
        foglalas_index = input("Adja meg a lemondandó foglalás indexét(0 = legtávolabbi foglalás): ")
        foglalas = self.foglalas_kereses(int(foglalas_index))

        if foglalas:
            eredmeny = self.lemondas(foglalas)
            print(eredmeny)
        else:
            print("Érvénytelen foglalás index.")

    def foglalasok_listazasa_menu(self):
        print("\nFoglalások listája:")
        self.foglalasok_listazasa()

    def szoba_kereses(self, szoba_szam):
        for szoba in self.szobak:
            if szoba.szobaszam == szoba_szam:
                return szoba
        return None

    def foglalas_kereses(self, foglalas_index):
        if 0 <= foglalas_index < len(self.foglalasok):
            return self.foglalasok[foglalas_index]
        return None

szalloda = Szalloda("GDE Hotel")
szalloda.inditas()
szalloda.futtat()
