import math

class Jel:
    def __init__(self, o, p, mp, x, y):
        self.o = int(o)
        self.p = int(p)
        self.mp = int(mp)
        self.x = int(x)
        self.y = int(y)
    
    def __str__(self):
        return f'{self.o} {self.p} {self.mp}'

def eltelt(elso, masodik):
    ido1 = elso[0] * 3600 + elso[1] * 60 + elso[2]
    ido2 = masodik[0] * 3600 + masodik[1] * 60 + masodik[2]
    telt = ido2-ido1
    return telt

def vissza(mp):
    ora = math.floor(mp / 3600)
    mp = mp - ora*3600
    perc = math.floor(mp / 60)
    mp = mp - perc*60
    return [str(ora), str(perc), str(mp)]


jelek = []

fajl = open("jel.txt", 'rt', encoding='utf-8')

for sor in fajl:
    sor = sor.strip().split()
    jelek.append(Jel(sor[0], sor[1], sor[2], sor[3], sor[4]))

print("2. feladat")
sorszam = int(input("Adja meg a jel sorszámát! ")) - 1
print(f'x={jelek[sorszam].x} y={jelek[sorszam].y}')


elso = jelek[0]
utolso = jelek[-1]
print('\n4. feladat')
kozott = eltelt([elso.o, elso.p, elso.mp], [utolso.o, utolso.p, utolso.mp])
print("Időtartam:", ':'.join(vissza(kozott)))


bal = jelek[0].x
also = jelek[0].y
jobb = jelek[0].x
felso = jelek[0].y
for j in jelek:
    if j.x > jobb:
        jobb = j.x
    if j.x < bal:
        bal = j.x
    if j.y < also:
        also = j.y
    if j.y > felso:
        felso = j.y
print('\n5. feladat')
print(f'Bal alsó: {bal} {also}, jobb felső: {jobb} {felso}')

osszeg = 0
for i in range(0, len(jelek)-1):
    osszeg += math.sqrt(pow((jelek[i].x - jelek[i+1].x), 2) + pow((jelek[i].y - jelek[i+1].y), 2))
print('\n6. feladat')
print('Elmozdulás:', round(osszeg, 3), 'egység')


txt = open('kimaradt.txt', 'wt', encoding='utf-8')


for j in range(1, len(jelek)):
    jel1 = jelek[j-1]
    jel2 = jelek[j]
    elteresx = abs(jel1.x-jel2.x) / 10
    elteresy = abs(jel1.y-jel2.y) / 10
    koordinataelteres = 0

    if elteresx > elteresy:
        koordinataelteres = elteresx
    else:
        koordinataelteres = elteresy
    
    if koordinataelteres % 1 == 0:
        koordinataelteres -= 1
        

    idoelteres = eltelt([jel1.o, jel1.p, jel1.mp], [jel2.o, jel2.p, jel2.mp]) / 300
    if idoelteres % 1 == 0:
        idoelteres -= 1

    if koordinataelteres >= 1 and koordinataelteres > idoelteres:
        txt.write(f'{jel2} koordináta-eltérés {(int(koordinataelteres))}\n')
    elif idoelteres >= 1 and idoelteres > koordinataelteres:
        txt.write(f'{jel2} időeltérés {(int(idoelteres))}\n')