# Programozási tételek

# 1. Írjunk  programot,  mely  véletlenszerűen  generál  200  kétjegyű  számot,  a  számokat  a  képernyőre  írja  sorfolytonosan, 
# szóközzel elválasztva, majd válaszol a következő kérdésekre! 
# a. Mennyi a számok átlaga? 
# b. Hány darab átlagon felüli szám van? 
# c. Hány darab 0-ra végződő szám van köztük? 
# d. Mi a legnagyobb szám? Hányszor szerepel? 
# e. Mi a legkisebb szám? Hányszor szerepel? 
# f. Mi a legnagyobb 0-ra végződő szám? 
# g. Van a számok közt a 15-nek többszöröse? Ha igen, melyik?


from moduls import *
from random import randint

szamok=[]
for _ in range(200):
    szam=randint(10,99)
    szamok.append(szam)
    print(szam, end=' ')
print('')

print(f'A számok átlaga: {atlag(szamok):.3f}')

print(f'A listában {nagy(szamok)} átlagnál nagyobb szám van.')

print(f'A listában {darab(szamok)} 0-ra végződő szám van.')

print(f'A lista legnagyonobb eleme: {legnagyobb(szamok)[0]} és {legnagyobb(szamok)[1]}-szor szerepel benne.')

print(f'A lista legkisebb eleme: {legkisebb(szamok)[0]} és {legkisebb(szamok)[1]}-szor szereple benne.')

print(f'A lista legnagyobb tízzel osztható száma: {legtiz(szamok)}')

print(f'A 15-nek többszöröse {tobbszoros(szamok)} a listában.')