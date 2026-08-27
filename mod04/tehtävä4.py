pituus = float(input('Anna kuhan pituus (cm):'))

if pituus<37:
    print('Laske kuhan takaisin järveen!')
    print(f'Puuttuu vielä {37-pituus} cm')
else:
    print('Kuhan voi ottaa talteen!')

hytti=input('Anna hyttiluokka (LUX, A, B, C):')
if hytti=='LUX':
    print('Parvekkeellinen hytti yläkannella')
elif hytti=='A':
    print('Ikkunallinen hytti autokannen yläpuolella')
elif hytti=='B':
    print('Ikkunaton hytti autokannen yläpuolella')
elif hytti=='C':
    print('Ikkunaton hytti autokannen alapuolella')
else:
    print('Virheellinen hyttiluokka!')

sukupuoli=input('Anna oma sukupuolisi (Nainen, Mies):')
hemoglobiini=int(input('Anna arvio omasta hemoglobiinistä:'))

if sukupuoli == 'nainen' and hemoglobiini < 117:
    print('Hemoglobiini on alhainen')
elif sukupuoli == 'nainen' and hemoglobiini <= 175:
    print('Hemoglobiini on normaali')
elif sukupuoli == 'nainen' and hemoglobiini > 175:
    print('Hemoglobiini on korkea')

elif sukupuoli == 'mies' and hemoglobiini < 134:
    print('Hemoglobiini on alhainen')
elif sukupuoli == 'mies' and hemoglobiini <= 195:
    print('Hemoglobiini on normaali')
elif sukupuoli == 'mies' and hemoglobiini > 195:
    print('Hemoglobiini on korkea')
else:
    print('Virheelinen sukupuoli')

vuosiluku = float(input('Valitse ja kirjoita jonkun vuosiluvun:'))

if (vuosiluku%400==0):
    print('Valitsemasi vuosiluku on karkausvuosi')
elif (vuosiluku%100==0):
    print('Valitsemasi vuosiluku ei ole karkausvuosi')
elif (vuosiluku%4==0):
    print('Valitsemasi vuosiluku on karkausvuosi')
else:
    print('Valitsemasi vuosiluku ei ole karkausvuosi')