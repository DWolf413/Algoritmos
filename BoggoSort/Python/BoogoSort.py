import random as rnd

def verificar(arreglo):
    for i in range(0, len(arreglo)-1):
        if arreglo[i]>arreglo[i+1]:
            return False
    return True

print(verificar([1,2,3,4,5]))
print(verificar([1,7,3,4,5]))

def ordenar(arreglo):
    while not (verificar(arreglo)):
        posA = rnd.randint(0, len(arreglo)-1)
        posB = rnd.randint(0, len(arreglo)-1)

        aux = arreglo[posA]
        arreglo[posA] = arreglo[posB]
        arreglo[posB] = aux

    return arreglo

arreglo = [4,5,1-4,7,8,-9,5]

print(ordenar(arreglo))