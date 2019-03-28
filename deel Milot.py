from tkinter import*

def clicked1():
    grondtal = int(entry.get())
    kwadraat = grondtal ** 2
    tekst = "kwadraat: van {} = {}"
    label["text"] = tekst.format(grondtal, kwadraat)

def clicked2():
    grondtal = int(entry.get())
    kwadraat = grondtal ** 2
    tekst = "kwadraat: van {} = {}"
    label["text"] = tekst.format(grondtal, kwadraat)


root = Tk()
label = Label(master=root,
              text='Maak een keuze: ',
              background='white',
              foreground='black')
label.pack()

button1 = Button(master=root, text='Overzicht alle films aanbieder', command=clicked1)
button.pack(pady=10)

button2 = Button(master=root, text='Overzicht films niet aangeboden door andere aanbieder', command=clicked2)
button.pack(pady=10)

entry = Entry(master=root)
entry.pack(padx=10, pady=10)