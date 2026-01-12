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
porinis[]
neporinis[]

for i, skaicius in enumerate(numbers):
    if i % 2 = 0:
        porinis.append(skaicius)
    else:
        neporinis.append(skaicius)

print(f'Poriniai skaiciai: {porinis}')
print(f'Neporiniai skaiciai: {neporinis}')





