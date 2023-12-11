lista = ["Noite", 1, 2, 3, 4, 5]
lista2 = ["Noite", 1, 2, 3, 4, 5]
print(len(lista))
lista.append(7)
print(lista)
del lista[0]
print(lista)
lista.remove(2)
print(lista)
lista = lista2.copy()
print(lista)