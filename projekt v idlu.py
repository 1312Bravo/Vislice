import random

class Igra():

    def __init__(self):
        self.slovar = {}
        self.pripravi_slovar()
        self.beseda = None

    def pripravi_slovar(self):
        slovar_besed = {}

        for kljuc in ["lahko", "srednje-tezko", "tezko", "zelo-tezko"]:
            with open(kljuc + ".txt") as f:
                besede = []
                for x in f:
                    besede.append(x.strip())
                slovar_besed[kljuc] = besede

        self.slovar = slovar_besed

    def igraj(self):
        beseda = self.izberi_besedo()
        self.beseda = beseda
        self.porocaj_o_stevilu_crk()

    def izberi_besedo(self):
        dolzina = input("Besedo kaksne težavnosti bos probal uganiti? (lahko, srednje-tezko, tezko, zelo-tezko) ")
        beseda = random.choice(self.slovar[dolzina])
        return beseda

    def porocaj_o_stevilu_crk(self):
        stevilo_crtic = len(self.beseda)
        if stevilo_crtic <= 4:
            print("Tvoja beseda ima {} crke.".format(stevilo_crtic))
        else: 
            print("Tvoja beseda ima {} crk.".format(stevilo_crtic))



i = Igra()
i.igraj()













def prvo_ugibanje():
    ugibana_crka = input(" Katera crka mislis, da se skriva v besedi? ")
    return ugibana_crka




def ali_je_ugib_pravilen(ugibana_crka):
    beseda_kot_niz = str(izberi_besedo)
    posamezne_crke = list(beseda_kot_niz)
    print(posamezne_crke)
    




#class Obesalni
