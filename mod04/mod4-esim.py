import random

## kolikkoheittosimulaattori
random_number=random.randint(0,1)
print(random_number)

onko_totta= False
if onko_totta:
    print('Onhan se totta!')

#if lauseen _ehto_ muodostuu aina True tai False arvoksi.
#jos ehto on tosi suoritetaan if-lohko muuten else-lohko
if random_number==0:
    result='Kruuna'
    print('Kruunu tuli!')
else:
    result='Klaava'

print(f'Heitit kolikkoa ja sait {result}!')

## kolikkoheittosimulaattori 2.0
# kolikko pystyyn tod.näk. oikeasti jotain 1/6000 luokkaa?
random_number=random.random() #sulut loppuun muuten ei toimi
print(random_number) #liukulukuarvo välillä 0-1

#kolikko jää pystyyn todennäköisyys 1/100
if random_number < 0.01:
    print('Kolikko jäi pystyyn')
elif random_number<0.505:
    print('Kruuna tuli.')
else:
    print('Klaava tuli.')

#erilaisia ehtoja

arvo=100

print(90<arvo<110)
print(100 != 101)

#kalvo esimerkki

ikä = int(input("Anna ikä: "))
if 15 <= ikä <18:
    paino = float(input("Anna paino (kg): "))

if ikä >= 18 or (ikä >= 15 and paino >= 55):
    print("Lääkkeen käyttö on sallittua.")
else:
    print("Lääkettä ei saa käyttää.")

#jälkimmäinen if-lause ikäarvolla 18
#print(True or (True and False))

print(not True)