import random
import tkinter as tk



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
        random_beseda = random.choice(self.slovar[dolzina])
        self.beseda = random_beseda
        return random_beseda

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
            print(ugibana_crka)
            if ugibana_crka in self.beseda:
                print(" Bravo, pravilno si uganil, crka {}, se res skriva v iskani besedi. ".format(ugibana_crka))
                return True
            else:
                self.stevilo_napak += 1
                print(" Napačno ugibas, poskusi se enkrat! ")
                return False

    def ali_je_konec_igre(self):
        if self.stevilo_napak == 10:
            return True

        for x in self.beseda:
            if x not in self.ze_ugibano:
                return False

        return True

nova_igra = Igra()
nova_igra.pripravi_slovar()
beseda = nova_igra.izberi_besedo()
okno = tk.Tk()
okvir = tk.Frame(okno)

okno.title('Vislice')

vislice = tk.Label(okno, text='Obesi se.')
vislice.grid(row=1, sticky="w,e,n,s")

stevec=0
seznam_crk = []

for crka in beseda:
    vislice = tk.Label(okno, text='_')
    vislice.grid(row=0, column=2+stevec)
    seznam_crk.append(vislice)
    stevec += 1
    

vnosno_polje = tk.Entry(okno)
vnosno_polje.grid(row=2, column=0)

def vnos():
    ugibana_crka = vnosno_polje.get()
    nova_igra.ali_je_ugib_pravilen(ugibana_crka)
    seznam_crk[0].config(text=ugibana_crka)
    return ugibana_crka
    
gumb_ugibaj = tk.Button(okno, text = 'Ugibaj!', command=vnos)
gumb_izhod = tk.Button(okno, text = 'Izhod!', command=quit)

gumb_ugibaj.grid(row=2, column=1)
gumb_izhod.grid(row=3, column=1)


okno.mainloop()
i = Igra()
i.igraj()













