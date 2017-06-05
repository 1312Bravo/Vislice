import random

class Igra():

    def __init__(self):
        self.slovar = {}
        self.pripravi_slovar()
        self.beseda = None
        self.ze_ugibano = []
        self.konec = False # smo že uganili
        self.stevilo_napak = 0

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
        self.beseda = self.izberi_besedo()
        self.porocaj_o_stevilu_crk()

        while not self.konec:
            self.porocaj()
            crka = self.ugibaj()
            pravilno = self.ali_je_ugib_pravilen(crka) 
            if not pravilno:
                # narišemo človeka
                print("Število napačnih ugibanj: {}".format(self.stevilo_napak))
            self.konec = self.ali_je_konec_igre()

        # konec igre
        if self.stevilo_napak == 10: 
            print("Joj, stevilo napacnih ugibanj je preseglo omejitev, zal si obesen.")
        else: 
            print("Bravo, uganil si besedo! Napacno si ugibal le: {}-krat".format(self.stevilo_napak))
            
    def porocaj(self):
        for x in self.beseda:
            if x in self.ze_ugibano:
                print(x, end = " ")
            else:
                print("_", end = " ")
        print(" \n")
    def izberi_besedo(self):
        dolzina = input("Besedo kaksne težavnosti bos probal uganiti? (lahko, srednje-tezko, tezko, zelo-tezko) ")
        beseda = random.choice(self.slovar[dolzina])
        return beseda

    def porocaj_o_stevilu_crk(self):
        stevilo_crtic = len(self.beseda)
        print("Tvoja beseda ima {} crk{}.".format(stevilo_crtic, "" if stevilo_crtic > 4 else "e" ))

    def ugibaj(self):
        print("Ugibaj!")
        ugibana_crka = input("Katera crka mislis, da se skriva v besedi? ")
        return ugibana_crka

    
    
    def ali_je_ugib_pravilen(self, ugibana_crka):
        if ugibana_crka in self.ze_ugibano:
            self.stevilo_napak += 1
            print("To crko si enkrat ze ugibal, zresni se!")
            return False
        else: 
            self.ze_ugibano += ugibana_crka
            if ugibana_crka in self.beseda:
                print(" Bravo, pravilno si uganil, crka {}, se res skriva v iskani besedi. ".format(ugibana_crka))
                return True
            else:
                self.stevilo_napak += 1
                print(" Napačno ugibaš, poskusi se enkrat! ")
                return False

    def ali_je_konec_igre(self):
        if self.stevilo_napak == 10:
            return True

        for x in self.beseda:
            if x not in self.ze_ugibano:
                return False

        return True

        

i = Igra()
i.igraj()












