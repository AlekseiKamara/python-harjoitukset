print('Moikka maailma, nimeni on Aleksei!!')
print('Kiva nähdä!')

name=input('Mikä sinun nimesi on:')
print('Terve', name)

sade=float(input('Anna ympyrän säde:'))

import math

pinta_ala=math.pi*sade**2
print(f'Ympyrän pinta-ala on {pinta_ala:.2f}')

kanta=float(input('Anna kannan:'))
korkeus=float(input('Anna korkeuden:'))

piiri=2*kanta+2*korkeus
pinta_ala=kanta*korkeus

print(f'Suorakulmion piiri on {piiri:.2f}')
print(f'Suorakulmion pinta-ala on {pinta_ala:.2f}')

luku1=int(input('Anna ensimmäinen luku:'))
luku2=int(input('Anna toinen luku:'))
luku3=int(input('Anna kolmas luku:'))

summa=luku1+luku2+luku3
tulo=luku1*luku2*luku3
keskiarvo=summa/3

print(f'Lukujen summa on {summa:.1f}')
print(f'Lukujen tulo on {tulo:.1f}')
print(f'Lukujen keskiarvo on {keskiarvo:.1f}')

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