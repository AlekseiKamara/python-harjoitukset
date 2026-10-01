class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus=rekisteritunnus
        self.huippunopeus=huippunopeus
        self.nopeus=0
        self.kuljettu_matka=0

    def kiihdytä(self, muutos):
        self.nopeus=self.nopeus+muutos
        if self.nopeus>self.huippunopeus:
            self.nopeus=self.huippunopeus
        if self.nopeus<0:
            self.nopeus=0

    def kulje(self, tunnit):
        self.kuljettu_matka=self.kuljettu_matka+self.nopeus*tunnit
auto=Auto('ABC-123', 142)

auto.kiihdytä(30)
auto.kiihdytä(70)
auto.kiihdytä(50)
print('Nopeus kiihdytyksen jälkeen:', auto.nopeus)
auto.kulje(1.5)
print('Auton kuljettu matka on:', auto.kuljettu_matka)

auto.kiihdytä(-200)

print('Auton nopeus hätäjarrutuksen jälkeen:', auto.nopeus)
      
        