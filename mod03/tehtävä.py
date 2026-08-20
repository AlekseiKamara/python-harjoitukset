print('Moikka maailma, nimeni on Aleksei!!')
print('Kiva nähdä!')

name=input('Mikä sinun nimesi on:')
print('Terve', name)

sade=float(input('Anna ympyrän säde:'))

pinta_ala=3.14*sade*sade
print('Pinta-ala:', pinta_ala)

kanta=float(input('Anna kannan:'))
korkeus=float(input('Anna korkeuden:'))

piiri=2*kanta+2*korkeus
pinta_ala=kanta*korkeus

print('Piiri:',piiri)
print('Pinta-ala:',pinta_ala)

luku1=int(input('Anna ensimmäinen luku:'))
luku2=int(input('Anna toinen luku:'))
luku3=int(input('Anna kolmas luku:'))

summa=luku1+luku2+luku3
tulo=luku1*luku2*luku3
keskiarvo=summa/3

print('Lukujen summa:',summa)
print('Lukujen tulo:',tulo)
print('Lukujen keskiarvo:',keskiarvo)

leiviska=float(input('Anna leiviskät:'))
naula=float(input('Anna naulat:'))
luotit=float(input('Anna luodit:'))

grammat=leiviska*20*32.4+naula*32.4+luotit*1.0

kilogrammat=int(grammat//1000)
grammat=int(grammat%1000)

print('Paino on',kilogrammat,'kg ja',grammat,'g')

import random

koodi1=random.randint(0,9), random.randint(0,9), random.randint(0,9)
koodi2=random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)

print('Kolmenumeroinen koodi:', koodi1)
print('Neljänumeroinen koodi:', koodi2)