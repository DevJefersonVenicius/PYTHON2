# fatiamento
frase = ('A minha casa é verde')
print(frase[2:7])
print(frase[::-1])
print(frase[8:12])
print(frase[-5::])
frase = ''.join(frase)
print(frase)



# listas
lista =  ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
print(len(lista))
print(lista[0::2]) # impares
print(lista[1::2]) # pares
print(lista[0::3])
print(lista.copy())
lista.append('11')
print(lista)
del lista[10]
print(lista)
lista.remove('10')
print(lista)
lista.pop()
print(lista)
lista.insert(0, '0')
print(lista)
lista2 = ['9', '10']
lista.extend(lista2)
print(lista)

# conjutos
conjuto = {'1', '2', '3', '4', '5'}
print(conjuto)
conjuto2 = set('6')
print(conjuto2)
conjuto.add('6')
print(conjuto)
conjuto.discard('1')
print(conjuto)
conjuto.update('1')
print(conjuto)
conjuto.clear()
print(conjuto)
conjunto3 = conjuto | conjuto2
print(conjunto3)