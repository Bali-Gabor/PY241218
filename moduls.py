def atlag(lista:list)->int:
    sum=0
    for x in range(len(lista)): sum+=lista[x]
    return sum / len(lista)


def nagy(lista:list)->int:
    darab=0
    for x in range(len(lista)):
        if lista[x]>sum(lista)/len(lista): darab+=1
    return darab


def darab(lista:list)->int:
    darab=0
    for x in range(len(lista)):
        if lista[x] % 10 == 0: darab+=1
    return darab


def legnagyobb(lista:list)->int:
    index=0
    for x in range(1,len(lista)):
        if lista[index]<lista[x]: index=x
    darab=0
    for x in lista:
        if x == lista[index]: darab+=1
    return lista[index], darab


def legkisebb(lista:list)->int:
    index=0
    for x in range(1,len(lista)):
        if lista[index]>lista[x]: index=x
    darab=0
    for x in lista:
        if x == lista[index]: darab+=1
    return lista[index], darab


def legtiz(lista:list)->int:
    index=None
    for x in range(len(lista)):
        if lista[x] % 10 == 0:
            if index == None or lista[x] > lista[index]: index=x
    return lista[index]


def tobbszoros(lista:int)->str:
    for szam in lista:
        if szam % 15 == 0: return 'szerepel'
    return 'nem szerepel'
            