class Jel:
    def __init__(self, o, p, mp, x, y):
        self.o = o
        self.p = p
        self.mp = mp
        self.x = x
        self.y = y

def eltelt(elso, masodik):
    ido1 = elso[0] * 3600 + elso[1] * 60 + elso[2]
    ido2 = masodik[0] * 3600 + masodik[1] * 60 + masodik[2]
    telt = ido2-ido1
    return telt


jelek = []

fajl = open("jel.txt", 'rt', encoding='utf-8')

for sor in fajl:
    sor = sor.strip().split()
    jelek.append(Jel(sor[0], sor[1], sor[2], sor[3], sor[4]))

print("2. feladat")
sorszam = int(input("Adja meg a jel sorszámát! ")) - 1
print(f'x={jelek[sorszam].x} y={jelek[sorszam].y}')
