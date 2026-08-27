#Tuntiharjoituksia 26.8.2026


#Sähkölaskulaskin

kulutus = float(input('Syötä sähkölaskukulutus (kWh):'))

if kulutus <= 50:
    hinta=kulutus*10
    print(f'Sähkön hinta on {hinta} senttiä.')