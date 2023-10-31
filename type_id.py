a = 5

print(type(a))

lista = [1, 2, 3, 4]

print(type(lista))

print(id(a))

b = a

print(id(b))

print(id(lista))

lista2 = lista.copy()

print(id(lista2))

print(a is b)
