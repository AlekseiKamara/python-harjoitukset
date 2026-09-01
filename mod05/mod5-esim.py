'''suorita=True
while suorita:
    print('Tämä printautuu vain kerran')
    suorita=False

print('Suoritus loppui')



# while == toista niin kauan kune ehto on tosi

luku=1  # 1. alkuarvo/kierrosmuuttuja

while luku<=5:  # 2. ehto
    print(luku)
    #luku=luku+1 # 3. muuttujan arvon muuttaminen
    luku+=1

print('Jatketaan ohjelmaa')

#Lasketaan luku 10 alaspäin
###########################

luku=int(input('Anna luku josta laskemma alaspäin:'))

while luku >=1:
    print('luku')
    luku-=1

#kerrat = int(input("Montako kertaa tervehditään: "))
#tehdyt = 0
#while tehdyt < kerrat:
    #print("Hyvää huomenta")
    #tehdyt = tehdyt + 1

# käyttäjä lopettaa toiston
###################

salasana=input('Anna salainen salasana, jotta pääset sisään (python):').strip()

while salasana !='python':
    print('Väärä salasana')
    salasana=input('Anna salasana uudestaan:')

print('Tervetuloa sisään, koodi oli oikea')

#while/else rakenne
#suoritus siirtyy else-haaran kun toistoehto on epätosi
#sitä ei suoriteta jos poistutaan break-lauseella
#else rakenne on harvemmin käytetty

komento=input('Anna komento (lopeta, APUA):').strip().lower() #poistaa välilyöntien ja pikku/isokirjaiten merkitystä

while komento !='lopeta':
    if komento=='apua':
        break
    print('Annoit komennon:', komento)
    komento=input('Anna uusi komento:')
else:
    print('Annoit käskyn lopeta, joten näin tehdään!!!')

print('Ohjelma jatkuu')

import random

noppa1 = noppa2 = heitot = 0
while (noppa1 != 6 or noppa2 != 6):

    noppa1 = random.randint(1,6)
    noppa2 = random.randint(1,6)
    print(noppa1, noppa2)
    heitot = heitot + 1

print(f"Tarvittiin {heitot:d} heittoa.")

eka = 1
while eka <= 5:
    toka = 1
    while toka <= 5:
        print(f"{eka} kertaa {toka} on {eka*toka:d}")
        toka = toka + 1
    eka = eka + 1
import random

pelikerta=0
heitot=0
while pelikerta<1000:

    noppa1=noppa2=0
    while (noppa1 != 6 or noppa2 != 6):

        noppa1 = random.randint(1,6)
        noppa2 = random.randint(1,6)
        #print(noppa1, noppa2)
        heitot = heitot + 1

    pelikerta += heitot+1
print('Pelikertoja meillä oli:', pelikerta)
print(f"Tarvittiin {heitot:d} heittoa.")
print(f'Jokaisella kierroksella oli keskimäärin {heitot/pelikerta} heittoa')
'''
#usein while rakennetta käytetetään ns. pääsilmukka eli main loop

peli_käynnissä=True
#main loop
print('Tervetuloa oeliini!!!')

while peli_käynnissä:
    print('Valitse minne mennään (j tai l) eli jatka tai lopeta')
    # j jatkaa peliä ja l lopettaa
    valinta=input('Anna komento:')
    if valinta=='j':
        print('Jatkoit peliä')
    if valinta=='l':
        print('Lopetit pelin')
        peli_käynnissä=False
