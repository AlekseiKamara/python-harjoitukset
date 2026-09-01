nimi=input('Mikä sinun nimesi on?:')
ikä=int(input('Mikä sinun ikäsi on?:'))

if ikä<12:
    print('Olet alaikäinen!')
else:
    print(f'Hauska tavata {nimi}!')
    print(f'Ikäsi on {ikä}!')

    komento=''

    while komento !='lopeta':
        print('Päävalikko:')
        print('1 - Tervetuloa ja alkusanat')
        print('2 - Yleiset ohjeet')
        print('lopeta - Lopeta pelin')

        komento=input('Valitse jonkin komennon: ')
        if komento=='1':
            print(f'Hei {nimi}! Tervetuloa pelaamaan peliä. Toivottavasti peli herättää jonkinlaisen kiinnostuksen')

        if komento=='2':
            print('Peli ei ole tarkoitettu alle 12-vuotiaille. Lue tarkasti ohjeet ja keskeiset säännöt!')


