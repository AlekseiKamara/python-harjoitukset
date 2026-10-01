class Pelaaja:
    def __init__(self, nimi, ika, inventaario, sijainti):
        self.nimi=nimi
        self.ika=ika
        self.inventaario=inventaario
        self.sijainti=sijainti

class Huone:
    def __init__(self, nimi, esine):
        self.nimi=nimi
        self.esine=esine

class Esine:
    def __init__(self, nimi):
        self.nimi=nimi
        self.kunto='Hyvä'