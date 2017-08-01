import tkinter as tk


beseda = "delavec"
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
    seznam_crk[stevec].config(text=ugibana_crka)
    return ugibana_crka
    
gumb_ugibaj = tk.Button(okno, text = 'Ugibaj!', command=vnos)
gumb_izhod = tk.Button(okno, text = 'Izhod!', command=quit)

gumb_ugibaj.grid(row=2, column=1)
gumb_izhod.grid(row=3, column=1)





