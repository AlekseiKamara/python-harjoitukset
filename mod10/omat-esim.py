'''
lampotila=int(input('Anna lämpötila:'))
if lampotila <10:
    print('Kylmä')
elif lampotila >=10:
    print('Sopiva')
else:
    print('Lämmin')

hedelmat = ["omena", "banaani", "appelsiini", "päärynä"]
for hedelma in hedelmat:
    print(hedelma)

luvut = [4, 7, 2, 9, 6, 3]
summa=0
for luku in luvut:
    print(luku)
    summa=summa+luku
print(f'Lukuejen summa on {summa}')

lista=[]
nimi=input('Anna nimesi:')
for i in range(4):
    lista.append(nimi)
nimi=input('Anna uusi nimesi:')
'''
'''
luku=int(input('Anna luku:'))
def onko_jaollinen(self,luku):
    self.luku=luku
    return
if luku!=5:
    print('Luku on parillinen')
else:
    print('Luku ei ole parillinen')
'''
'''
pisteet=int(input('Anna pisteiden määrä:'))
if pisteet >=80:
    print('Erinomainen')
elif pisteet >=50:
    print('Hyväksytty')
else:
    print('Hylätty')
'''
'''luku=1
while luku <=10:
    print(luku)
    luku=luku+1


nimet=[]
nimi=input('Anna nimesi:')
for i in range(3):
    print(nimi)
    nimet.append(nimi)

def laske_tulo(luku1, luku2):
    return luku1*luku2
tulos=laske_tulo(10,2)
print(tulos)

def onko_taydellinen_ika(ika):
    if ika >=18:
        print(True)
    else:
        print(False)
onko_taydellinen_ika(20)'''

'''class Talo:
    def __init__(self,osoite,huoneita):
        self.osoite=osoite
        self.huoneita=huoneita
    def esittele(self):
        print(f'Talo sijaitsee osoitteessa, {self.osoite} ja siinä on {self.huoneita} huonetta.')

talo=Talo('Nuijamäki', 5)
talo.esittele()'''

'''

class Koira:
    def __init__ (self, nimi, ika, haukahdus):
        self.nimi=nimi
        self.ika=ika
        self.haukahdus=haukahdus

    def esittely (self):
        print(f'Koiran nimi on {self.nimi}, ikäsi on {self.ika} ja haukahdus on {self.haukahdus}')

koira1=Koira('Leo', 7, 'Wuf, Wuf')
koira1.esittely()
'''
'''class Kirja:
    def __init__(self, nimi, kirjoittaja):
        self.nimi=nimi
        self.kirjoittaja=kirjoittaja

    def esittele(self):
        print(f'Kirjan nimi on {self.nimi}, ja kirjoittaja on {self.kirjoittaja}')

kirja1=Kirja('Lord of the rings', 'Andry Breakfill')
kirja1.esittele()'''

'''
class Pankkitili:
    def __init__(self, omistaja, saldo):
        self.omistaja=omistaja
        self.saldo=saldo

    def talletu(self,maara):
        self.saldo=self.saldo+maara
        print(f'Tilin omistaja om {self.omistaja}, tilin saldo on {self.saldo}')
        print(maara)
    def nayta_saldo(self, saldo):
        print(saldo)
tili=Pankkitili('Aleksei', 10000)
tili.talletu(100)
tili.nayta_saldo()
'''

'''class Auto:
    def __init__(self, merkki, nopeus):
        self.merkki=merkki
        self.nopeus=nopeus

    def kiihdy(self,maara):
        self.nopeus=maara+self.nopeus
        print(f'Auton merkki {self.merkki}, auton nopeus on {self.nopeus} km/h')

auto1=Auto('Mercedes', 55)
auto1.kiihdy(20)
'''

'''
class Opiskelija:
    def  __init__(self,nimi, pisteet):
        self.nimi=nimi
        self.pisteet=pisteet

    def lisaa_pisteita(self, maara):
        self.pisteet=self.pisteet+maara
        print(f'Nimi on {self.nimi} ja pisteet {self.pisteet}')

    def nayta_pisteet(pisteet):
        print(pisteet)

opiskelija1=Opiskelija('Aleksei', 67)
opiskelija1.lisaa_pisteita(69)'''

'''nimi=input('Anna nimesi:')
ika=int(input('Anna ikäsi:'))
print(f'Hei {nimi}! Ikäsi on {ika}')

pisteet=int(input('Anna pisteet:'))
if pisteet>=80:
    print('Erinomainen')
elif pisteet >=50:
    print('Hyväksytty')
else:
    print('Hylätty')

luvut=[4, 11, 8, 15, 2, 20, 7]

for luku in luvut:
    if luku >10:
        print(luku)

lista=[]


def laske_summa(luku1, luku2):
    return luku1+luku2
tulos=laske_summa(10,5)
print(tulos)

def onko_negatiivinen(luku):
    if luku <0:
        return True
    elif luku >=0:
        return False
tulos=onko_negatiivinen(-5)
print(tulos)


numerot=[3, 8, 12, 5, 20, 7, 15]
laskuri=0

for luku in numerot:
    if luku >=10:
        laskuri = laskuri + 1
print(laskuri)

class Luokka:
    def __init__(self, nimi, ika):
        self.nimi=nimi
        self.ika=ika

    def tervehdi (self):
        print(f'Hei {self.nimi}, {self.ika} ikäinen')

henkilo=Luokka('Aleksei', 18)
henkilo.tervehdi()

class Pankkitili:
    def __init__(self, omistaja, saldo):
        self.omistaja=omistaja
        self.saldo=saldo

    def nostaa(self, maara):
        self.saldo=self.saldo-maara
        print(f'Omistaja {self.omistaja} ja saldosi on {self.saldo}')

tili=Pankkitili('Aleksei', 500)
tili.nostaa(100)'''

'''class Elain:
    def __init__(self, nimi):
        self.nimi=nimi

    def tulosta_tiedot(self):
        print(f'Nimi: {self.nimi}')

class Kissa(Elain):
    def __init__(self, nimi, vari):
        self.vari=vari
        super().__init__(nimi)

    def tulosta_tiedot(self):
        print(f'Nimi on {self.nimi} ja väri {self.vari}')

kissa=Kissa('Misu', 'Musta')
kissa.tulosta_tiedot()'''

'''class Opiskelija:
    def __init__(self, nimi, ika):
        self.nimi=nimi
        self.ika=ika

class Henkilo (Opiskelija):
    def __init__(self,nimi,ika):
        self.nimi=nimi
        self.ika=ika
        super().__init__(nimi, ika)

    def tulosta_tiedot(self):
        print(f'Nimesi on {self.nimi} ja ikäsi on {self.ika}')

henkilo=Henkilo('Aleksei', 18)
henkilo.tulosta_tiedot()

class Ajoveuvo:
    def __init__ (self,malli):
        self.malli=malli

class Auto(Ajoveuvo):
    def __init__(self, merkki):
        self.merkki=merkki
        super().__init__(self, self.malli, merkki)

    def tulosta_tiedot(self):
        print(f'Auton merkki on {self.merkki} ja auton malli on {self.malli}')

auto=Auto('Mercedes', '2018')
auto.tulosta_tiedot()'''


'''class Henkilo:
    def __init__(self, nimi, ika):
        self.nimi=nimi
        self.ika=ika

    def tulostaa_tiedot(self):
        print(f'Nimi on {self.nimi} ja ikä {self.ika}')

class Opiskelija(Henkilo):
    def __init__ (self,nimi, ika, opiskelijanumero):
        self.opiskelijanumero=opiskelijanumero
        super().__init__(nimi,ika)

    def tulosta_tiedot(self):
        print(f'Opiskelijan nimi on {self.nimi}, ikä on {self.ika} ja opiskelijanumero on {self.opiskelijanumero}')

class Ammattiopiskelija(Opiskelija):
    def __init__(self, nimi, ika, opiskelijanumero):
        super().__init__(nimi, ika, opiskelijanumero)

    def tulosta_tiedot(self):
        print(f'Opiskelijan nimi on {self.nimi}, ikä on {self.ika} ja opiskelijanumero on {self.opiskelijanumero}')

ammattiopiskelija=Ammattiopiskelija('Aleksei', 18, 298345)
ammattiopiskelija.tulosta_tiedot()'''

'''class Tyontekija:
    def __init__(self,nimi, palkka):
        self.nimi=nimi
        self.palkka=palkka

    def tulosta_tiedot(self):
        print(f'Nimesi on {self.nimi} ja palkkasi on {self.palkka}')

class Tuntityontekija(Tyontekija):
    def __init__(self, nimi, palkka, tuntipalkka, tunnit):
        self.tuntipalkka=tuntipalkka
        self.tunnit=tunnit
        super().__init__(nimi,palkka)
    def laske_palkka(self):
        return self.tuntipalkka*self.tunnit
    def tulosta_tiedot(self):
            print(f'Nimesi on {self.nimi}, palkkasi on {self.palkka}, tunnit tehtyä työtä {self.tunnit} ja tuntipalkka {self.tuntipalkka}')

class Esihenkilo(Tyontekija):
    def __init__(self, nimi, palkka, tiimi):
        self.tiimi=tiimi
        super().__init__(nimi,palkka)
    def tulosta_tiedot(self):
        print(f'Nimesi on {self.nimi}, palkkasi on {self.palkka} ja tiimiläiset ovat {self.tiimi}!')
tuntityontekija=Tuntityontekija('Aleksei', 1800, 10, 12)
tuntityontekija.tulosta_tiedot()
esihenkilo=Esihenkilo('Aleksei', 1800, 'Anni')
esihenkilo.tulosta_tiedot()'''

#Harjoitus koe-1:

'''nimi=input('Anna tuotteen nimi:')
kappalehinta=float(input('Anna hinta:'))
kappalemaara=int(input('Anna kappalemäärä:'))

print(f'Tuotteen nimi {nimi}, kappalehinta {kappalehinta} euroa ja kappalemäärä {kappalemaara} !')

luku=int(input('Anna luku:'))
if luku >0:
    print('Suuri')
elif luku==0:
    print('Nolla')
else:
    print('Luku on alle nolla')

salasana=input('Anna salasana:')
oikea_salasana='python123'
yritykset=0
limit_yritykset=3
while True:
    yritykset+=1
    if salasana==oikea_salasana:
        print('Tervetuloa')
        break
    else:
        print('Väärä salasana.')
        if yritykset >=limit_yritykset:
            print('Pääsy estetty')
            break

lämpötilat = [12, 18, 21, 7, 25, 16, 9]
for luku in lämpötilat:
    if luku >=10:
        print(luku)'''

'''arvot = [4, 11, 8, 19, 3, 15, 22, 6]
summa=0
for luku in arvot:
    if luku >10:
        summa=summa+1

print(summa)'''

'''class KirjastoKirja:
    def __init__(self, nimi, kirjoittaja, sivut):
        self.nimi=nimi
        self.kirjoittaja=kirjoittaja
        self.sivut=sivut

    def esittele(self):
        print(f'Kirjan nimi on {self.nimi}, kirjoittaja on {self.kirjoittaja} ja sivut ovat {self.sivut} ')

kirja1=KirjastoKirja('Albaska', 'Kay Murphy', 215)
kirja1.esittele()'''

'''class Opiskelija:
    def __init__(self, nimi):
        self.nimi=nimi

    def esittele(self):
        print(f'Opiskelijan nimi on {self.nimi}')

class Kurssi(Opiskelija):
    def __init__(self,nimi, kurssinimi):
        self.kurssinimi=kurssinimi
        super().__init__(nimi)

    def esittele(self):
        print(f'Opiskelijan nimi on {self.nimi} ja hän on kursilla {self.kurssinimi}')

opiskelija=Kurssi('Aleksei', 'Python-ohjelmointi')
opiskelija.esittele()'''


'''class Viesti:
    def __init__(self, teksti):
        self.teksti=teksti

    def nayta(self):
        print(f'Viestissä luki {self.teksti}')

class Sahkoposti(Viesti):
    def __init__(self, teksti, lahettaja):
        self.lahettaja=lahettaja
        super().__init__(teksti)

    def nayta(self):
        print(f'Viestissä luki {self.teksti} ja viestin on lähettänyt {self.lahettaja}!')

viesti1=Sahkoposti('Tervetuloa kurssille', 'Aleksei Kämärä')
viesti1.nayta()'''

'''class Lippu:
    def __init__(self, hinta):
        self.hinta=hinta

    def nayta(self):
        print(f'Lipun hinta on {self.hinta}')

class Opiskelijalippu(Lippu):
    def __init__(self, hinta, alennus):
        self.alennus=alennus
        super().__init__(hinta)

    def nayta(self):
        print(f'Alkuperäinen hinta on {self.hinta} ja alenettuhinta on {self.alennus}')

    def lopullinen_hinta(self):
        return self.alennus
hinta1=Opiskelijalippu(255, 20)
hinta1.nayta()'''

'''suora_leveys=int(input('Anna leveyden:'))
suora_korkeus=int(input('Anna korkeus:'))

pinta_ala=suora_leveys*suora_korkeus
print(f'Suorakulmion pinta-ala on {pinta_ala}')

pisteet=int(input('Anna pisteet:'))
if pisteet >=80:
    print('Kiitettävä')
elif pisteet >=50:
    print('Hyväksytty')
else:
    print('Hylätty')

luku=int(input('Anna luku:'))
while luku !=7:
    if luku==7:
        print('Oikein')
    else:
        break

nimet = ["Anna", "Matti", "Liisa", "Jari", "Emilia"]

for lista in nimet:
    print(lista)'''

'''def laske_alennettu_hinta(hinta, alennus):
    alennettu_hinta=hinta*alennus/100
    lopullinen_hinta=hinta-alennettu_hinta
    return lopullinen_hinta
tulos=laske_alennettu_hinta(80,25)
print(tulos)'''

'''def laske_saatu_palkkio(hinta, palkkio):
    prosentti_hinta=hinta*palkkio/100
    loppullinen_hinta=prosentti_hinta
    return loppullinen_hinta
tulos=laske_saatu_palkkio(200, 15)
print(tulos)'''

###########
#Harjoituskoe 2:

'''sade=float(input('Anna säde:'))
pinta_ala=3.14*sade*sade
print(f'Pinta-ala on {pinta_ala}')

lampotila=int(input('Anna lämpötila:'))
if lampotila >=20:
    print('Lämmintä')
elif lampotila >=0:
    print('Viileää')
else:
    print('Pakkasta')

luku=int(input('Anna luku:'))
while luku %2!=0:
   luku=int(input('Anna luku:'))
print('Parillinen luku')

numerot = [3, 8, 12, 5, 20, 7]

for luku in numerot:
    if luku %2==0:
        print(luku)'''

'''arvosanat = [5, 7, 8, 4, 9, 6, 10, 3]
summa=0
for summa in arvosanat:
    if summa >=8:
        summa=summa+1

print(summa)'''

'''def laske_vuosipalkka(kuukausipalkka):
    return 12*kuukausipalkka
tulos=laske_vuosipalkka(2500)
print(tulos)'''

'''{'nimi=Aleksei'
'ika=12'
'kaupunki=Helsinki'
}'''

'''class Pankkitili:
    def __init__(self, omistaja, saldo):
        self.omistaja=omistaja
        self.saldo=saldo

    def nayta_saldo(self):
        print(f'Tilin omistaja on {self.omistaja} ja saldo on {self.saldo} euroa')
tili=Pankkitili('Aleksei',2500)
tili.nayta_saldo()'''

'''class Kirjailija:
    def __init__(self, nimi):
        self.nimi=nimi

class Kirja:
    def __init__(self, nimi, kirjailija):
        self.nimi=nimi
        self.kirjailija=kirjailija

    def nayta_tiedot(self):
        print(f'Kirjan {self.nimi} ja kirjailija on {self.kirjailija}.')
kirja1=Kirja('Python perusteet', 'Aleksei')
kirja1.nayta_tiedot()'''

'''class Hahmo:
    def __init__(self, nimi):
        self.nimi=nimi

    def tervehdi(self):
        print(f'Hei, olen {self.nimi}')

class Pelaaja(Hahmo):
    def __init__(self, nimi):
        super().__init__(nimi)

    def tervehdi(self):
        print(f'Hei, olen pelaaja {self.nimi}')
pelaaja1=Pelaaja('Aleksei!')
pelaaja1.tervehdi()'''

'''class Tuote:
    def __init__(self, nimi, hinta):
        self.nimi=nimi
        self.hinta=hinta

    def laske_hinta(self):
        print(f'Tuoten nimi {self.nimi} ja hinta {self.hinta}')

class Alennustuote(Tuote):
    def __init__(self, nimi, hinta, alennus):
        self.alennus=alennus
        super().__init__(nimi, hinta)

    def laske_hinta(self):
        self.alennus=self.hinta-self.alennus
        print(f'Tuoten nimi on {self.nimi}, alkuperäinen hitna {self.hinta} ja alennushinta {self.alennus}')
tuote1=Alennustuote('PS', 2500, 300)
tuote1.laske_hinta()'''

#Harjoituskoe - 3:

'''tuotteen_hinta=int(input('Anna hinta:'))
tuotteiden_maara=(int(input('Anna tuotteiden määrä:')))
kokonaishinta=tuotteen_hinta+tuotteiden_maara
print(f'Kokonaishinta on {kokonaishinta}')

luku=int(input('Anna kokonaisluku:'))
if luku >50:
    print('Suuri')
elif luku >=10:
    print('Keskikokoinen')
else:
    print('Pieni')

numero=int(input('Anna numero:'))
while numero !=100:
    numero=int(input('Anna numero:'))
print('Numero löytyi!')

luvut = [14, 3, 22, 8, 31, 10, 5]

for luku in luvut:
    if luku >10:
        print(luku)

luvut = [2, 15, 7, 20, 4, 18, 9, 25]
summa=0
for luku in luvut:
    if luku >10:
        summa=summa+1
print(summa)

def laske_kolmion_ala(kanta, korkeus):
    pinta_ala=(kanta*korkeus)/2
    return pinta_ala
tulos=laske_kolmion_ala(2, 4)
print(tulos)

{
    'merkki':'mercedes'
    'malli','hachback'
    'vuosi':2025

}

class Opiskelija:
    def __init__(self, nimi, ika, koulu):
        self.nimi=nimi
        self.ika=ika
        self.koulu=koulu

    def tiedot(self):
        print(f'Opiskelijan nimi on {self.nimi}, ikä on {self.ika} ja koulu on {self.koulu}')
opiskelija1=Opiskelija('Aleksei', 18, 'Kivimaan Koulu')
opiskelija2=Opiskelija('Bella', 15, 'Espoon koulu')
opiskelija1.tiedot()
opiskelija2.tiedot()

class Ravintola:
    def __init__(self, ravintola_nimi):
        self.ravintola_nimi=ravintola_nimi
    def tiedot(self):
        print(f'{self.ravintola_nimi}')

class Asiakas(Ravintola):
    def __init__(self, ravintola_nimi, asiakas_nimi):
        self.ravintola_nimi=ravintola_nimi
        self.asiakas_nimi=asiakas_nimi
    def tiedot(self):
        print(f'{self.ravintola_nimi} käy ravintolassa {self.asiakas_nimi}.')
ravintola=Asiakas('Aleksei', 'Python Pizza')
ravintola.tiedot()

class Ajoneuvo:
    def __init__ (self, ajoneuvo_merkki):
        self.ajoneuvo_merkki=ajoneuvo_merkki

    def aja(self):
        print(f'{self.merkki} ajoneuvo liikkuu.')

class Auto(Ajoneuvo):
    def __init__(self, ajoneuvo_merkki,merkki):
        self.ajoneuvo_merkki=ajoneuvo_merkki
        self.merkki=merkki

    def aja(self):
        print(f'{self.ajoneuvo_merkki} Ajoneuvo liikku ja Auto {self.merkki} ajaa tiellä')
auto1=Auto('Suuri', 'Mercedes')
auto1.aja()

class Henkilo:
    def __init__(self, nimi, ika):
        self.nimi=nimi
        self.ika=ika

    def tiedot(self):
        print(f'Henkilon nimi on {self.nimi} ja ikä on {self.ika}')

class Tyontekija(Henkilo):
    def __init__(self, nimi, ika, palkka):
        self.palkka=palkka
        super().__init__(nimi, ika)

    def tiedot(self):
        print(f'Henkilon nimi on {self.nimi}, ikä on {self.ika} ja palkka on {self.palkka} euroa.')
        return 
tiedot=Tyontekija('Aleksei', 18, 1800)
tiedot.tiedot()'''

#####
#Harjoituskoe-4
'''tuotteen_hinta=int(input('Anna hinta:'))
alennus_prosentti=int(input('Anna alennus:'))

alennettu_hinta=tuotteen_hinta*alennus_prosentti/100
print(f'Alenettu hinta {alennettu_hinta} euroa')
'''

'''opiskelija={
    'aleksei':'aleksei',
    '18':'18',
    'Kivimaan':'Kivimaan',
    'Java':'Java',
    'arvosana':1

}
print(opiskelija['aleksei'])
print(opiskelija['Kivimaan'])
opiskelija['arvosana']=5
print(opiskelija['arvosana'])
opiskelija['kurssi']='Python'
print(opiskelija['kurssi'])'''

##
#Harjoituskoe 5

''''tuntipalkka=int(input('Anna palkka:'))
tehdyt_työt=int(input('Anna tuntien määrä:'))

palkka_yhteensa=tuntipalkka*tehdyt_työt
print(f'Palkka yhteensä {palkka_yhteensa}')

pistemaara=int(input('Anna pistemäärä:'))
if pistemaara >=85:
    print('Erinomainen')
elif pistemaara >=70:
    print('Hyvä')
elif pistemaara >=50:
    print('Tyydyttävä')
else:
    print('Hylätty')

luku=int(input('Anna luku:'))
while luku >0:
    luku=int(input('Anna luku:'))
print('Negatiivinen luku anettu')

lampotilat = [12, 18, 7, 21, 15, 4, 19, 9]
summa=0
for luku in lampotilat:
    if luku >=15:
        summa=summa+1
print(summa)

def laske_kokonaispalkka(tuntipalkka, tunnit):
    return tuntipalkka*tunnit
laske_kokonaispalkka(200, 2)
print(laske_kokonaispalkka)

puhelin={
    'merkki':'Apple',
    'malli':'Iphone',
    'hinta':1600,
    'vuosi':2025
}
print(puhelin['merkki'])
print(puhelin['hinta'])
puhelin['hinta']=599
print(puhelin['hinta'])
puhelin['vuosi']=2026
print(puhelin['vuosi'])

print(puhelin)'''

# HARJOITUS KOE:

'''luku=input('Anna luku:')
if luku >0:
    print('Positiivinen')
elif luku <0:
    print('Negatiivinen')
else: 
    print('Luku on nolla')'''

'''ika=int(input('Anna ikäsi:'))
if ika <13:
    print('Lapsi')
elif ika >=13 and ika <18:
    print('Nuori')
else:
    print('Aikuinen')'''
'''luku=int(input('Anna kokonaisluku:'))
while luku:
    if luku == 0:
        print(luku)
    else: 
        break'''
'''for i in range(1, 21):
    if i %2==0 and i >10:
        print(i)'''

'''luvut = [4, 7, 2, 9, 12, 3, 8]

for luku in luvut:
    suurin=luku
    pienin=luku
    if luku >suurin:
        print(luku)
    elif luku <pienin:
        print(luku)
    if luku %2==0:
        print(luku)'''

'''def onko_parillinen(kokonaisluku):
    if kokonaisluku %2==0:
        return True
    else:
        return False'''


'''def laske_parilliset(kokonaislukuja):
    return kokonaislukuja %2==0'''

'''maara = 0 
 
luku = int(input("Anna luku: ")) 
 
while luku != 0: 
 
    if luku %2==0: 
        maara = maara+1
 
    luku = maara+luku
 
print("Parillisia:", maara)'''

'''luvut = [4, 11, 6, 15, 8, 3, 20]

for luku in luvut:
    if luku >5 and luku <15 and luku %2==0:
        print(luku)'''

'''anna_salasana=input('Anna salasana:')
salasana='python'
yrtityksiä=0
while salasana:
    if salasana =='python':
        print('Oikein')
        break
    else:
        anna_salasana=input('Anna salasana uudestan:')
        print('Virheelinen salasana')'''

'''opiskelijat = {
    "Matti": 18,
    "Anna": 20,
    "Liisa": 17,
    "Ville": 21
}
opiskelija='''

'''def kolmekertainenluku(luku):
    tulos=luku*3
    return tulos

tulos=kolmekertainenluku(4)
print(tulos)'''


def on_parillinen(kokonaisluku):
    if kokonaisluku %2==0:
        return True
    else:
        return False

opiskelija = {
    "nimi": "Matti",
    "ika": 22,
    "kurssi": "Python"
}





    


