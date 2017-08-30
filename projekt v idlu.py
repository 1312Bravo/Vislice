import random
import tkinter as tk
from tkinter.messagebox import showinfo



class Igra():
    def __init__(self):

        self.slovar = {}
        self.beseda = None
        self.ze_ugibano = []
        self.dolzina_besede = 0
        self.uganjene_crke = 0
        self.stevilo_napak = 0


    def pripravi_slovar(self):
        slovar_besed = {}
        for kljuc in ["lahko",  "srednje-težko", "težko", "zelo-težko"]:
            with open(kljuc + ".txt") as f:
                besede = []
                for x in f:
                    besede.append(x.strip())
                slovar_besed[kljuc] = besede
        self.slovar = slovar_besed


    def izberi_besedo(self): 

        def potrdi_besedo():
            dolzina = zacetno_vnosno_polje.get()
            random_beseda = random.choice(self.slovar[dolzina])
            self.beseda = random_beseda
            self.dolzina_besede = len(self.beseda)
            zacetno_okno.destroy()
            self.igralno_okence()
            
        zacetno_okno = tk.Tk() 
        zacetno_okno.geometry("500x200")
        zacetno_okno.resizable(width=False, height=False)
        zacetno_okno.title('Izbira težavnosti')

        zacetni_okvir = tk.Frame(zacetno_okno)
        zacetni_napis = tk.Label(zacetno_okno, text='Besedo kakšne tezavnosti boš probal uganiti? (lahko, srednje-težko, težko, zelo-težko)')
        zacetni_napis.place(x=25, y=20)

        zacetno_vnosno_polje = tk.Entry(zacetno_okno) 
        zacetno_vnosno_polje.place(x=190, y=50)
        gumb_tezavnost = tk.Button(zacetno_okno, text='Potrdi', command=potrdi_besedo)
        gumb_tezavnost.place(x=230, y=100)
        
        zacetno_okno.mainloop()

    def igralno_okence(self):
       
        def ali_je_ugib_pravilen(ugibana_crka):
            if ugibana_crka in self.ze_ugibano: 
                self.stevilo_napak += 1

                if self.stevilo_napak == 10:                   
                    showinfo("Rezultat", "Izgubil si, kupi si slovar!")
                    
                stevec_napak.config(text=self.stevilo_napak) 
                izpis.config(text="To črko si enkrat že ugibal, zresni se!")

            else:
                self.ze_ugibano += ugibana_crka
                if ugibana_crka in self.beseda:
                    self.uganjene_crke += self.beseda.count(ugibana_crka)
                    izpis.config(text=" Bravo, pravilno si uganil, črka {} se res skriva v iskani besedi. ".format(ugibana_crka))

                    if self.uganjene_crke == self.dolzina_besede:
                        showinfo("Rezultat", "Bravo, zmagal si!")

                else:
                    self.stevilo_napak += 1
                    
                    if self.stevilo_napak == 10:                   
                        showinfo("Rezultat", "Izgubil si, kupi si slovar!")
                        
                    stevec_napak.config(text=self.stevilo_napak)
                    izpis.config(text=" Napačno ugibaš, poskusi še enkrat! ")

        def porocaj():
            st_element = 0  
            for x in self.beseda: 
                if x in self.ze_ugibano: 
                    seznam_crk[st_element].config(text=x.upper()) 
                    st_element += 1                    
                else:
                    seznam_crk[st_element].config(text="___")  
                    st_element += 1
        

        okno = tk.Tk() 
        okno.geometry("500x200")
        okno.resizable(width=False, height=False)
        okvir = tk.Frame(okno) 
        okno.title('Vislice, by Urh Peček')
        vislice = tk.Label(okno, text='Katera črka misliš da se skriva v besedi?') 
        vislice.place(x=50, y=10)
        
        stevec = 0 
        seznam_crk = [] 
        
        for crka in self.beseda: 
            crtica = tk.Label(okno, text='___') 
            crtica.place(x=50 + stevec, y=110)
            seznam_crk.append(crtica) 
            stevec += 30
            
        vnosno_polje = tk.Entry(okno) 
        vnosno_polje.place(x=50, y=40)
        
        izpis = tk.Label(okno, width=50, text=' ') 
        izpis.place(x=30, y=60)
        
        okno_napak = tk.Label(okno, text='Število napak')
        okno_napak.place(x=400, y=20)
        
        stevec_napak = tk.Label(okno, text='0') 
        stevec_napak.place(x=430, y=40)

        def vnos(): 
            ugibana_crka = vnosno_polje.get()
            ali_je_ugib_pravilen(ugibana_crka)  
            porocaj()
            vnosno_polje.delete(0)  
            return True

        gumb_ugibaj = tk.Button(okno, text='Ugibaj!', command=vnos)
        gumb_izhod = tk.Button(okno, text='Izhod!', command=quit)
        
        gumb_ugibaj.place(x=430, y=100)
        gumb_izhod.place(x=430, y=150)
        
        okno.mainloop()


nova_igra = Igra()
nova_igra.pripravi_slovar()
nova_igra.izberi_besedo() 
