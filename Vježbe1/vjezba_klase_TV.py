class Pero:
    pass

ante = Pero()

class Tv:
    dijagonala = 165
    sirina = 65
    proizvodjac = "Saba"

grunding = Tv()
print(grunding.proizvodjac)
philips = Tv()
print(philips.proizvodjac)


class Televizija:
    dijagonala = 165
    sirina = 65

    def __init__(self, proizvodjac):
        self.proizvodjac = proizvodjac

    def ispisi(self):
        print(f'Televizor proivođača {self.proizvodjac} ima dijagonalu {self.dijagonala}.')

saba = Televizija("Saba")
print(saba.proizvodjac)
saba.ispisi()

sony = Televizija("Sony")
print(sony.proizvodjac)
sony.ispisi()
print()