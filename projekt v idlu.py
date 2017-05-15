import random
slovar_besed = {}

for kljuc in ["lahko", "srednje-tezko", "tezko", "zelo-tezko"]:
    with open(kljuc + ".txt") as f:
        besede = []
        for x in f:
            besede.append(x.strip())
        slovar_besed[kljuc] = besede


def izberi_besedo():
    dolzina = input("Besedo kaksne težavnosti bos probal uganiti? (lahko, srednje-tezko, tezko, zelo-tezko) ")
    beseda = random.choice(slovar_besed[dolzina])
    print(beseda)

