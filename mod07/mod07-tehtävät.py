#Tehtävä 1
import random

print('===Noppapeli===')
def heita_noppaa():
    return random.randint(1,6)

silmaluku=0
while silmaluku!=6:
    silmaluku=heita_noppaa()
    print(silmaluku)

####
# Tehtävä 2

print('===Noppapeli===')
def heita_noppaa(tahkojen_lkm):
    return random.randint(1,tahkojen_lkm)

nopan_koko = int(input('Anna nopan koko (maksimisilmäluku):'))

silmaluku=0
while silmaluku!=nopan_koko:
    silmaluku=heita_noppaa(nopan_koko)
    print(silmaluku)

###
# Tehtävä 3

def gallonat_litroiksi(gallona):
    return gallona*3.785

gallonat=float(input('Anna gallonat:'))
while gallonat >=0:
    litrat=gallonat_litroiksi(gallonat)
    print(f'{gallonat} gallonaa on {litrat} litraa')
    gallonat=float(input('Anna gallonat:'))

####
#Tehtävä 4
def laske_summa(luvut):
    return sum(luvut)
numerot=[3,5,8,9,12]
laske_summa(numerot)
print(f'listan {numerot} summa on {laske_summa(numerot)}')

###
#Tehtävä 5
def karsi_parittomat(luvut):
    parilliset=[]
    for luku in luvut:
        if luku%2==0:
            parilliset.append(luku)
    return(parilliset)

alkuperainen_lista=[1,2,3,4,5,6,7,8,9]
karsittu_lista=karsi_parittomat(alkuperainen_lista)

print(f'alkuperäinen lista on {alkuperainen_lista} ja karsittu lista on {karsittu_lista}')

###
#Tehtävä 6
import math
def calculate_unit_price(diameter_in_cm, price):
    r=diameter_in_cm/100/2
    area=math.pi*r**2
    return price/area

unit_prices=[]
for pizza_number in range(2):
    diameter=float(input(f'Anna {pizza_number+1}. pizzan halkaisijan (cm):'))
    price=float(input(f'Anna {pizza_number+1}. pizzan hinta (eur):'))
    unit_price=(calculate_unit_price(diameter, price))
    unit_prices.append(unit_price)
    print(f'{pizza_number}. Pizzan yksikköhinta (eur/m2): {unit_prices[pizza_number]:0.2f}')

if unit_prices[0]<unit_prices[1]:
    print('Ensimmäinen pizza on halvempi.')
elif unit_prices[0]>unit_prices[1]:
    print('Toinen pizza on halvempi')
else:
     print('Yhtä halpoja.')