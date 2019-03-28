from tkinter import *

def login():
    global screen
    screen = Tk()
    screen.geometry('300x250')
    screen.title('thuisbioscoop.program')
    Label(text='thuisbioscoop', bg= 'grey', width = '300', height = '2').pack()
    Label(text = '').pack()
    Button(text = 'aanbieder', height = '2', width = '30', command = login_aanbieder).pack()
    Label(text='').pack()
    Button(text = 'bezoeker', height = '2', width = '30', command = login_bezoeker).pack()
    screen.mainloop()

def login_bezoeker():
    global screen1
    screen1= Toplevel(screen)
    screen1.title('login bezoeker')
    screen1.geometry('300x250')

    global gebruikersnaam
    global email
    global gebruikersnaam_entry
    global email_entry

    gebruikersnaam = StringVar()
    email = StringVar()

    Label(screen1, text='vul hieronder gegevens in').pack()
    Label(screen1, text= '').pack()
    Label(screen1, text='gebruikersnaam').pack()
    gebruikersnaam_entry = Entry(screen1, textvariable = gebruikersnaam)
    gebruikersnaam_entry.pack()
    Label(screen1, text='email').pack()
    email_entry = Entry(screen1, textvariable = email)
    email_entry.pack()
    Label(screen1, text= '').pack()
    Button(screen1, text = 'inloggen', width = 10, height = 1, command = check_bezoeker).pack()

def check_bezoeker():
    bezoekers= open("gegevensbezoeker.txt", 'r')
    gegevens = bezoekers.readlines()
    testlist=[]
    for item in gegevens:
        testlist.append(item.rstrip('\n'))
    print(gebruikersnaam_entry.get(), email_entry.get())
    if (gebruikersnaam_entry.get() in testlist) and (email_entry.get() in testlist):
        Label(screen1, text = 'login bezoeker succes', fg = 'green').pack()
        bezoekers.close()
    else:
        Label(screen1, text='login bezoeker onsuccesvol', fg='red').pack()
        bezoekers.close()

def login_aanbieder():
    global screen2
    screen2= Toplevel(screen)
    screen2.title('login aanbieder')
    screen2.geometry('300x250')

    global gebruikersnaam
    global email
    global gebruikersnaam_entry
    global email_entry

    gebruikersnaam = StringVar()
    email = StringVar()

    Label(screen2, text='vul hieronder gegevens in').pack()
    Label(screen2, text= '').pack()
    Label(screen2, text='gebruikersnaam').pack()
    gebruikersnaam_entry = Entry(screen2, textvariable = gebruikersnaam)
    gebruikersnaam_entry.pack()
    Label(screen2, text='email').pack()
    email_entry = Entry(screen2, textvariable = email)
    email_entry.pack()
    Label(screen2, text= '').pack()
    Button(screen2, text = 'inloggen', width = 10, height = 1, command = check_aanbieder).pack()

def check_aanbieder():
    bezoekers = open("gegevensbezoeker.txt", 'r')
    gegevens = bezoekers.readlines()
    testlist = []
    for item in gegevens:
        testlist.append(item.rstrip('\n'))
    print(gebruikersnaam_entry.get(), email_entry.get())
    if (gebruikersnaam_entry.get() in testlist) and (email_entry.get() in testlist):
        Label(screen2, text='login bezoeker succes', fg='green').pack()
        bezoekers.close()
    else:
        Label(screen2, text='login bezoeker onsuccesvol', fg='red').pack()
        bezoekers.close()

login()