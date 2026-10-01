import random
import json

from luokat import Pelaaja
from luokat import Huone
from luokat import Esine

with open('peliprojekti/intro.txt', 'r') as tiedosto:
    intro=tiedosto.read()

print(intro)

nimi=input('Mikä sinun nimesi on?:')
ikä=int(input('Mikä sinun ikäsi on?:'))

if ikä<12:
    print('Olet alaikäinen!')
else:
    print(f'Hauska tavata {nimi}!')
    print(f'Ikäsi on {ikä}!')

with open('peliprojekti/ohjeet.txt', 'r') as tiedosto:
    ohjeet=tiedosto.read()

print(ohjeet)

avain=Esine('Avain')
ruuvimeisseli=Esine('Ruuvimeisseli')
vesipullo=Esine('Vesipullo')

# Ruuvimeisselin kunto arvotaan satunnaisesti
numero=random.randint(1,2)
if numero == 1:
    ruuvimeisseli.kunto='Hyvä'
else:
    ruuvimeisseli.kunto='Vanha'

vanki_selli=Huone('Vankiselli', avain)
kaytava=Huone('Kaytava', vesipullo)
varasto=Huone('Varasto', ruuvimeisseli)
valvomo=Huone('Valvomo', None)
piha=Huone('Piha', None)

# Pelaajan luominen
pelaaja=Pelaaja(nimi, ikä, [], vanki_selli)

print('Tervetuloa pelaaman peliä!')
print('Tavoiteena on päästä pois vankilasta!')

def katso_huonetta(huone):

    print()

    if huone.esine != None:
        print(f'Tässä huoneessa on esine: {huone.esine.nimi}.')
        if huone.esine.nimi == 'Ruuvimeisseli':
            print(f'Ruuvimeisselin kunto on: {huone.esine.kunto}.')
    else:
        print('Tässä huoneessa ei ole esinettä.')

    print()

def ota_esine(pelaaja):
    if pelaaja.sijainti.esine != None:
        esine=pelaaja.sijainti.esine
        pelaaja.inventaario.append(esine)
        pelaaja.sijainti.esine=None
        print(f'Otit esineen: {esine.nimi}.')
        return True
    else:
        print('Tässä huoneessa ei ole esinettä.')
        return False

def nayta_inventaariota(inventaario):
    print()
    print('Inventaariossa on:')
    if inventaario == []:
        print('Inventaariossa ei ole esineitä.')
    else:
        for esine in inventaario:
            print(esine.nimi)
    print()
# Esineen tarkistaminen inventaariosta
def tarkista_esine(inventaario, nimi):
    loytyi=False
    for esine in inventaario:
        if esine.nimi == nimi:
            loytyi=True
        
    return loytyi
# Liikkuminen huoneesta toiseen   
def liiku(pelaaja):
    print()
    if pelaaja.sijainti == vanki_selli:
        print('1 - Kaytava')
        valinta=input('Mihin haluat mennä?:')
        if valinta == '1':
            pelaaja.sijainti=kaytava
        else:
            print('Väärä sijainti!')

    elif pelaaja.sijainti == kaytava:
        print('1 - Vankiselli')
        print('2 - Varasto')
        print('3 - Valvomo')
        print('4 - Piha')
        valinta=input('Minne haluat mennä?:')
        if valinta == '1':
            pelaaja.sijainti=vanki_selli
        elif valinta == '2':
            pelaaja.sijainti=varasto
        elif valinta == '3':
            pelaaja.sijainti=valvomo
        elif valinta == '4':
            avain_löytyy=tarkista_esine(pelaaja.inventaario, 'Avain')
            if avain_löytyy:
                pelaaja.sijainti=piha
                print('Avasit oven avaimella!')
                print('Onneksi olkoon! Pääsit pois vankilasta!')
                print('Voitit pelin!')
            else:
                print('Et voi avata ovea!')
                print('Tarvitset avaimen!')

    elif pelaaja.sijainti == varasto:
        print ('1 - Kaytava')
        print ('2 - Valvomo')
        valinta=input('Minne haluat mennä?:')
        if valinta == '1':
            pelaaja.sijainti=kaytava
        elif valinta == '2':
            pelaaja.sijainti=valvomo

    elif pelaaja.sijainti == piha:
        print('Olet jo pihalla!')

    elif pelaaja.sijainti == valvomo:
        print('1 - Kaytava')
        print('2 - Piha')
        valinta=input('Minne haluat mennä?:')
        if valinta == '1':
            pelaaja.sijainti=kaytava
        elif valinta == '2':
            ruuvimeisseli_löytyy=tarkista_esine(pelaaja.inventaario, 'Ruuvimeisseli')
            if ruuvimeisseli_löytyy:
                print('Avasit ovin ruuvimeisselillä!')
                pelaaja.sijainti=piha
                print('Onneksi olkoon! Pääsit pois vankilasta!')
                print('Voitit pelin!')
            else:
                print('Et voi avata ovea!')
                print('Tarvitset ruuvimeisselin!')
# Tallentaa pelaajan tiedot save.json tiedostoon
def tallenna_peli(pelaaja):
    print('Tallennetaan peli...')
    try:
        with open('save.json', 'w') as tiedosto:
            data={
                'nimi' : pelaaja.nimi,
                'ika': pelaaja.ika,
                'huone' : pelaaja.sijainti.nimi,
                'esineet' : []
            }
            for esine in pelaaja.inventaario:
                data['esineet'].append(esine.nimi)
            json.dump(data, tiedosto)
            print('Peli on tallennettu!')
    except FileNotFoundError:
        print('Tallenus epäonnistui!')
    except IOError:
        print('Tiedostossa tapahtui virhe!')
 
def lataa_peli():
    try:
       
       with open('save.json', 'r') as tiedosto:
            data=json.load(tiedosto)
            return data
    except FileNotFoundError:
        print('Tallennettua peliä ei löytynyt!')
    except IOError:
        print('Tiedostossa tapahtui virhe!')

jatka=input('Haluatko jatkaa tallennetusta pelistä? Kyllä/ei:')

if jatka == 'kyllä':
    data=lataa_peli()
    if data != None:
        pelaaja.nimi=data['nimi']
        pelaaja.ika=data['ika']

        for nimi in data['esineet']:
            if nimi == 'Avain':
                pelaaja.inventaario.append(avain)
            elif nimi == 'Ruuvimeisseli':
                pelaaja.inventaario.append(ruuvimeisseli)
            elif nimi == 'Vesipullo':
                pelaaja.inventaario.append(vesipullo)
        if data['huone'] == 'Vankiselli':
            pelaaja.sijainti=vanki_selli
        elif data['huone'] == 'Kaytava':
            pelaaja.sijainti=kaytava
        elif data['huone'] == 'Varasto':
            pelaaja.sijainti=varasto
        elif data['huone'] == 'Valvomo':
            pelaaja.sijainti=valvomo
        elif data['huone'] == 'Piha':
            pelaaja.sijainti=piha
        print('Peli on ladattu!')

komento=''

while komento != 'lopeta':
    print()
    print(f'Olet paikassa: {pelaaja.sijainti.nimi}')
    print('1 - Katso huonetta')
    print('2 - Liiku')
    print('3 - Ota esine')
    print('4 - Näytä oma inventaariota')
    print('5 - Tallenna peli')
    print('lopeta - Lopeta pelin')

    komento=input('Valitse jonkin komennon: ')

    if komento == '1':
        katso_huonetta(pelaaja.sijainti)
    elif komento == '2':
        liiku(pelaaja)
    elif komento == '3':
        ota_esine(pelaaja)
    elif komento == '4':
        nayta_inventaariota(pelaaja.inventaario)
    elif komento == '5':
        tallenna_peli(pelaaja)