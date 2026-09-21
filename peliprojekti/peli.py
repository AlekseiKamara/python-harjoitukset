nimi=input('Mikä sinun nimesi on?:')
ikä=int(input('Mikä sinun ikäsi on?:'))

if ikä<12:
    print('Olet alaikäinen!')
else:
    print(f'Hauska tavata {nimi}!')
    print(f'Ikäsi on {ikä}!')

inventaario=[]
def tervetuloa():
    print(f'Hei {nimi}! Tervetuloa pelaaman oma peliä!')
def ohjeet():
    print('Peli ei ole tarjoitettu alle 12 vuotiaille')
    print('Lue tarkasti ohjeet ja säänöt ennen pelin alkamista')
def lisaa_esine():
    esine=input('Anna jokin esine:')
    inventaario.append(esine)

def nayta_inventaario():
    print(inventaario)

komento=''

while komento !='lopeta':
        print('Päävalikko:')
        print('1 - Tervetuloa ja alkusanat')
        print('2 - Yleiset ohjeet')
        print('3 - Lisää esineen inventaarion')
        print('4 - Näytä oma inventaariota')
        print('lopeta - Lopeta pelin')

        komento=input('Valitse jonkin komennon: ')
        if komento=='1':
            tervetuloa()
        if komento=='2':
           ohjeet()
        if komento=='3':
            lisaa_esine()
        if komento=='4':
            nayta_inventaario()