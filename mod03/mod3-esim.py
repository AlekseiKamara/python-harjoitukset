# Tuntiesimerkit 19.8.2026
'''
teksti = 'Tämä on merkkijono'
luku = 10
luku2 = 12.3

summa = luku + luku2
print('summa', summa)

#print('Lukujen', luku , luku2 , 'summa on' , summa)

print('Lukujen', luku , luku2 , 'summa on' , summa)

str(summa)
print('summa', summa)

kayttaja=input('Anna nimesi:')
print('Hauska tavata,'+ kayttaja +'!')
'''
'''
ikä=22
uusi_kayttaja=input('Anna nimesi:')
print('Hauska tavata, '+ uusi_kayttaja +'!')

#Tulosteen muotoilu fstringilla (kannattaa)
##############
print('Hauska tavata {uusi_kayttaja}!!!!')
print(f'Hauska tavata {uusi_kayttaja} ja ikäni on')

#printataan muuttujan tyyppi
print(f'Muuttujan tyyppi voidaan tutkia {type(kompleksiluku)}')
'''
########

a = float(input('Anna ensimmäinen luku:'))
b = float(input('Anna toinen luku:'))

yhteenlasku=a+b
jakolasku=yhteenlasku/2

print(f'Yhteenlasku:{yhteenlasku}')
print(f'Jakolasku:{jakolasku}')