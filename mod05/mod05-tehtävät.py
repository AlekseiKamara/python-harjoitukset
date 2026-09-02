#tehtävä 1

luku=1
while luku<=1000:
    if luku%3==0:
        print(luku)
    luku+=1
#####################
#tehtävä 2

tuumat=float(input('Anna tuumat:'))

while tuumat >=0:
    sentimetrit=tuumat*2.54
    print(f'Sentimetreinä se on {sentimetrit}')
    tuumat=float(input('Anna tuumat:'))
####################
#tehtävä 3

luku=input('Anna jokin luku:')

pienin=float(luku)
suurin=float(luku)

while luku !='':
    luku=input('Anna luku:')

    if luku !='':
        luku=float(luku)

        if luku<pienin: 
            pienin=luku

        if luku >suurin: 
            suurin=luku

print(f'Pienin luku on {pienin}')
print(f'Suurin luku on {suurin}')
############################
#tehtävä 4

import math
import random

oikea_numero=random.randint(1,10)

arvaus=int(input('Arvaa numeroa 1 ja 10 välillä:'))

while arvaus!=oikea_numero:

    if arvaus>oikea_numero:
        print('Arvaus on liian suuri!!')

    if arvaus<oikea_numero:
        print('Arvaus on liian pieni!!')

    arvaus=int(input('Oho, väärin! Kokeile arvata uudestan:'))
print('Arvaus meni oikein!!')
#########################
#tehtävä 5

kokeilut=0

while kokeilut<5:
    tunnus=input('Anna käyttäjätunnuksen:')
    salasana=input('Anna salasanan:')

    if tunnus=='python' and salasana=='rules':
        print('Tervetuloa!')
        break
    else:
        kokeilut=kokeilut+1
    if kokeilut==5:
        print('Pääsy evätty!')
#############################
#tehtävä 6

import random

N=1000
n=0
counter=0

while counter<N:
    x=random.uniform(-1,1)
    y=random.uniform(-1,1)
    print(f'{counter} Arvotun pisteen koordinaatit ovat, x={x}, y={y}')
    counter+=1
    if x**2+y**2<1:
        n+=1
        print('Piste on ympyrän sisällä')
print(f'Pisteitä arvottu yhteensä {N}, joista ympyrän sisälle osui {n} kpl.')

import math
pi=4*n/N
print(f'piin likiarvo on {pi}')