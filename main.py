# 1. Sugeneruokite masyvą iš 30 elementų (indeksai nuo 0 iki 29),
# kurių reikšmės yra atsitiktiniai skaičiai nuo 5 iki 25.
import random

print("---1. uzduotis----------------")

numbers = [random.randint(5, 25) for i in range(30)]
print(numbers)


# 2. Naudodamiesi 1 uždavinio masyvu:
# a. Suskaičiuokite kiek masyve yra reikšmių didesnių už 10;
print("---2a. uzduotis----------------")

kiekis = 0
for i in numbers:
    if i > 10:
        kiekis += 1

print(kiekis, end=" ")

# 2.B Raskite didžiausią masyvo reikšmę;
print("---2b. uzduotis----------------")

max = max(numbers)
print(max)

# 2.c Suskaičiuokite visų reikšmių sumą;
print("---2c. uzduotis----------------")

suma = sum(numbers)
print(suma)

# 2.d Sukurkite naują masyvą, kurio reikšmės yra 1 uždavinio masyvo reikšmes minus tos reikšmės indeksas;
print("---2d. uzduotis----------------")

#masyvas2 = [ x- i for i, inumbers - ]

numbers = [random.randint(5, 25) for i in range(30)]
print(numbers)

numbers_new = []

for i in range(len(numbers)):
    skaicius = numbers[i] - i
    numbers_new.append(skaicius)

print(numbers_new)

# 2.e Papildykite masyvą papildomais 10 elementų su reikšmėmis nuo 5 iki 25, kad bendras masyvas padidėtų iki indekso 39;
print("---2e. uzduotis----------------")

numbers = [random.randint(5, 25) for i in range(30)]
print(numbers)

for _ in range(10):
    skaicius = random.randint(5, 25)
    numbers.append(skaicius)

print(f"sekos ilgis: {len(numbers)}") # Turėtų būti 40
print(f"paskutinis indeksas: {len(numbers) - 1}") # Bus 39
print(numbers)

# 2.f Iš masyvo elementų sukurkite du naujus masyvus. Vienas turi būti sudarytas iš neporinių indekso reikšmių, o kitas iš porinių;
print("---2f. uzduotis----------------")

porinisindeks = []
neporinisindeks = []

for i, skaicius in enumerate(numbers):
    if i % 2 == 0:
        porinisindeks.append(skaicius)
    else:
        neporinisindeks.append(skaicius)

print(f'Poriniai indekso skaiciai: {porinisindeks}')
print(f'Neporiniai indekso skaiciai: {neporinisindeks}')

porinis = numbers[::2]
neporinis = numbers[1::2]
print(f'2Poriniai indekso skaiciai: {porinis}')
print(f'2Neporiniai indekso skaiciai: {neporinis}')

# 2.g Masyvo elementus su poriniais indeksais padarykite lygius 0 jeigu jie didesni už 15;
print("---2g. uzduotis----------------")

numbers = [random.randint(5, 25) for i in range(30)]
print(numbers)

for i in range(0, len(numbers), 2):
    if numbers[i] > 15:
            numbers[i] = 0
print(f'Poriniai indekso skaiciai didesni nei 15 prilyginami 0:')
print(numbers)

# 2.h Suraskite pirmą (mažiausią) indeksą, kurio elemento reikšmė didesnė už 10;
print("---2f. uzduotis----------------")

numbers = [random.randint(5, 25) for i in range(30)]
print(numbers)

for i, skreiksme in enumerate(numbers):
    if skreiksme > 10:
            print(f'Skaiciaus reiksme {skreiksme}, jo eiles indeksas {i}')
            break
else:
        print("nera skaiciu didesniu uz 10")

print()

# 3.Sugeneruokite masyvą, kurio reikšmės atsitiktinės raidės A, B, C ir D, o ilgis 200. Suskaičiuokite kiek yra kiekvienos raidės.
print("---3. uzduotis----------------")

#raides = [random.randint(A, D) for i in range(200)]

sarasas = "ABCD"

raides = [random.choice(sarasas) for _ in range(200)]
print(raides)

raidziukiekis = {r: raides.count(r) for r in sarasas}
print("\nRezultatai:")
for raide, kiekis in raidziukiekis.items():
    print(f'Raidė {raide} pasikartojo: {kiekis} kartus')

print()

# 4. Išrūšiuokite 3 uždavinio masyvą pagal abecėlę.
print("---4. uzduotis----------------")

sarasas = "ABCD"

raides = [random.choice(sarasas) for _ in range(200)]
print(raides)

raides.sort()
print(raides)

# 5. Sugeneruokite 3 masyvus pagal 3 uždavinio sąlygą. Sudėkite masyvus, sudėdami atitinkamas reikšmes.
# (turi gautis masyvas, kurio elementai, kaip pvz atrodo taip: “AAB”, “CBC”, “DDA”, 200 reikšmių).
# Paskaičiuokite kiek skirtingų reikšmių kombinacijų gavote.

raides1 = [random.choice(sarasas) for _ in range(200)]
raides2 = [random.choice(sarasas) for _ in range(200)]
raides3 = [random.choice(sarasas) for _ in range(200)]

raides_bendras = []
for i in range(200):
    raides123 = raides1[i]+ raides2[i] + raides3[i]
    raides_bendras.append(raides123)

print(raides_bendras)

ABCDkombinacijos = len(set(raides_bendras))
print(f'Skirtingos reiksmiu kombinacijos: {ABCDkombinacijos}')


