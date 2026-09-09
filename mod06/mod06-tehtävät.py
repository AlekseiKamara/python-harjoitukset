#Tehtävä 1

import random

maara=int(input('Anna arpakuutioiden määrä:'))
summa=0

for i in range(maara):
    heitto=random.randint(1,6)
    summa+=heitto
    print(f'Silmlukujen summa on {summa}')


#Tehtävä 2
numbers=[]
while True:
    input_number=input('Anna luku:')
    if input_number=='':
        break
    int(input_number)
    numbers.append(int(input_number))
numbers.sort(reverse=True)
for input_number in range(5):
    print(numbers)

#Tehtävä 3
luku=int(input('Anna kokonaisluku:'))
alkuluku=True

for i in range(2, luku):
        if luku % i==0:
            luku=False
if alkuluku and luku >1:
     print('Luku on alkuluku')
else:
     print('Luku ei ole alkuluku')


#Tehtävä 4
kaupungit=[]

for i in range(5):
     kaupungien_nimet=input('Anna kaupungin nimi:')
     kaupungit.append(kaupungien_nimet)
print('Annetut kaupungit:')
for kaupunki in kaupungit:
     print(kaupunki)

