#szam1 = int(input("írj ide egy számot: "))

#print(f"{szam1}")

#if not isinstance(szam1, int):
#    raise TypeError("Nem szám")
#else:
#    if szam1 > 10:
#        raise ValueError("10-nél nagyobbat ne adj meg")


while True:
    try:
        x = int(input("Írj egy számot"))
        break
    except ValueError:
        print("Nem jó, próbáld újra")