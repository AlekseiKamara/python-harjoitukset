#Mod08 esimerkit:

viikonpaivat = ("maanantai", "tiistai", "keskiviikko", "torstai", "perjantai", "lauantai", "sunnuntai")

print(viikonpaivat)

print('ensimmäinen viikonpäivä on', viikonpaivat[0])

#monikko moinkon sisällä (kaksi- tai moniulotteinen monikko)
print('narkipäivät ja viikonlopun päivät ovat omissa monikoissaan samassa monikossa:')
viikonpaivat_v2 = ("maanantai", "tiistai", "keskiviikko", "torstai", "perjantai"), ("lauantai", "sunnuntai")
print(viikonpaivat_v2)
print('arkipäivät ovat', viikonpaivat_v2[0])
print('viikonlopun päivät ovat', viikonpaivat_v2[1])
print('ensimmäinen arkipäivä on', viikonpaivat_v2[0][0])

#yksittäisten arvojen purku muuttujiin

(eka, toka, kolmas, neljas, viides, kuudes, seitsemas)=viikonpaivat
print(eka, kolmas, viides, seitsemas)


#monikko ja funktio muokattu esimerkki

import random

print('Tuplanoppa')

def heita():
    return (random.randint(1,6), random.randint(1,6))

nopat=heita()
print(f'Nopista tuli {nopat[0]} ja {nopat[1]}')

##Joukko (set)
print('Joukkoja')
viikonpaivat = ("maanantai", "tiistai", "keskiviikko", "torstai", "perjantai", "lauantai", "sunnuntai")
print(viikonpaivat)


