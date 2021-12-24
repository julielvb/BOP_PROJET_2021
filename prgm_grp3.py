# importation des fonctionnalités de TKINTER
from tkinter import *
from tkinter import messagebox          # module de fenêtre popup
from tkinter import font as tkFont      # module des polices d'écriture
from tkinter.filedialog import *        # module de récupération d'une image
# importation des fonctionnalités de PIL
from PIL import ImageTk, Image
import piexif
# importation des fonctionnalités de STEGANO
from stegano import lsb
from stegano import exifHeader as aaa
import os
from subprocess import Popen
from argparse import FileType
from hachoir.parser import createParser
from hachoir.metadata import extractMetadata

# fonction pour encoder un message dans une image
def encode():
    main.destroy()
    enc = Tk()
    enc.title('ENCODAGE DU MESSAGE')
    enc.geometry('1000x1000')
    enc.resizable(width=True, height=True)
    fontl = tkFont.Font(family='Arial', size=32)
    label1 = Label(enc)
    label1.pack()
    LabelTitle = Label(text="ENCODER", bg="black", fg="white", width=20)
    LabelTitle['font'] = fontl
    LabelTitle.place(relx=0.3, rely=0.1)

    # fonction pour ouvrir un fichier à encoder
    def openfile():
        global fileopen
        global imagee

        fileopen = StringVar()
        fileopen = askopenfilename(initialdir="/Desktop", title="sélectionner un fichier",
                                   filetypes=(("jpeg,png files", "*jpg *png"), ("all files", "*.*")))
        imagee = ImageTk.PhotoImage(Image.open(fileopen))
        Labelpath = Label(text=fileopen, bg='ivory')
        Labelpath.place(relx=0.3, rely=0.25, height=21, width=450)
        Labelimg = Label(image=imagee)
        Labelimg.place(relx=0.3, rely=0.3, height=200, width=200)

    Button2 = Button(text="Ouvrir un fichier", command=openfile)
    Button2.place(relx=0.3, rely=0.2, height=31, width=94)

    Label1 = Label(text="Entrer un message")
    Label1.place(relx=0.3, rely=0.55, height=21)
    entrysecmes = Entry()
    entrysecmes.place(relx=0.45, rely=0.55, relheight=0.05, relwidth=0.200)

    Label2 = Label(text="Nouveau nom du fichier")
    Label2.place(relx=0.3, rely=0.65, height=21, width=134)
    entrysave = Entry()
    entrysave.place(relx=0.45, rely=0.65, relheight=0.05, relwidth=0.200)

    # BOUTON DE SELECTION ENTRE JPEG (RADIO1) ET PNG (RADIO2) POUR CONVERTIR LE FICHIER ENCODE
    secimg = StringVar()
    radio1 = Radiobutton(text='jpeg', value='jpeg', variable=secimg)
    radio1.place(relx=0.3, rely=0.73)

    radio2 = Radiobutton(text='png', value='png', variable=secimg)
    radio2.place(relx=0.5, rely=0.73)

    # MESSAGE POPUP POUR L'ENCODAGE
    def encode():
        # SI UTILISATEUR COCHE JPEG
        if secimg.get() == "jpeg":
            inimage = fileopen
            response = messagebox.askyesno("popup", "Voulez-vous encoder ce message ?")
            if response == 1:
                aaa.hide(inimage, entrysave.get() + '.jpg', entrysecmes.get())
                messagebox.showinfo("popup", "Encodage réalisé avec succès comme " + entrysave.get() + ".jpeg")
            else:
                messagebox.showwarning("popup", "Erreur")
    # SI UTILISATEUR COCHE PNG
        if secimg.get() == "png":
            inimage = fileopen
            response = messagebox.askyesno("popup", "Voulez-vous encoder ce message ?")
            if response == 1:
                lsb.hide(inimage, message=entrysecmes.get()).save(entrysave.get() + '.png')
                messagebox.showinfo("popup", "Encodage réalisé avec succès comme " + entrysave.get() + ".png")
            else:
                messagebox.showwarning("popup", "Erreur")

    def back():
        enc.destroy()
        # execfile('image steganography using lsb.py')
        # os.system('python imagesteganographyusinglsb.py')
        Popen('python steganography.py')

    Button2 = Button(text="ENCODER", command=encode)
    Button2.place(relx=0.3, rely=0.8, height=31, width=94)

    Buttonback = Button(text="QUITTER", command=back)
    Buttonback.place(relx=0.3, rely=0.85, height=31, width=94)

    enc.mainloop()

# FONCTION POUR DECODER
def decode():
    main.destroy()
    dec = Tk()
    dec.title('DECODAGE DU MESSAGE')
    dec.geometry('1000x1000')
    dec.resizable(width=True, height=True)
    dec.wm_attributes('-transparentcolor')
    fontl = tkFont.Font(family='Arial', size=32)
    label1 = Label(dec)
    label1.pack()

    LabelTitle = Label(text="DECODER", bg="black", fg="white", width=20)
    LabelTitle['font'] = fontl
    LabelTitle.place(relx=0.3, rely=0.1)

    def openfile():
        global fileopen
        global imagee
        fileopen = StringVar()
        fileopen = askopenfilename(initialdir="/Desktop", title="select file",
                                   filetypes=(("jpeg files, png file", "*jpg *png"), ("all files", "*.*")))

        imagee = ImageTk.PhotoImage(Image.open(fileopen))
        Labelpath = Label(text=fileopen, bg='ivory')
        Labelpath.place(relx=0.3, rely=0.25, height=21, width=450)
        Labelimg = Label(image=imagee)
        Labelimg.place(relx=0.3, rely=0.3, height=200, width=200)

    def deimg():
        messag = lsb.reveal(fileopen)
        Label2 = Label(text=messag, bg='ivory')
        Label2.place(relx=0.3, rely=0.6, height=21, width=200)

    Button2 = Button(text="Ouvrir un fichier", command=openfile)
    Button2.place(relx=0.3, rely=0.2, height=31, width=94)

    Button2 = Button(text="DECODER", command=deimg)
    Button2.place(relx=0.3, rely=0.7, height=31, width=94)

    def back():
        dec.destroy()
        # execfile('image steganography using lsb.py')
        # os.system('python imagesteganographyusinglsb.py')
        Popen('python steganography.py')

    Buttonback = Button(text="QUITTER", command=back)
    Buttonback.place(relx=0.3, rely=0.75, height=31, width=94)

    dec.mainloop()

#FONCTION METADATA
def metadata():
    main.destroy()
    mtdt = Tk()
    mtdt.title('AFFICHER LES METADONNEES')
    mtdt.geometry('1000x1000')
    mtdt.resizable(width=True, height=True)
    mtdt.wm_attributes('-transparentcolor')
    fontl = tkFont.Font(family='Arial', size=32)
    label1 = Label(mtdt)
    label1.pack()

    LabelTitle = Label(text="METADONNEES", bg="black", fg="white", width=20)
    LabelTitle['font'] = fontl
    LabelTitle.place(relx=0.3, rely=0.1)

    def openfile():
        global fileopen
        global imagee
        fileopen = StringVar()
        fileopen = askopenfilename(initialdir="/Desktop", title="select file",
                                   filetypes=(("jpeg files, png file", "*jpg *png"), ("all files", "*.*")))

        imagee = ImageTk.PhotoImage(Image.open(fileopen))
        Labelpath = Label(text=fileopen, bg='ivory')
        Labelpath.place(relx=0.3, rely=0.25, height=21, width=450)
        Labelimg = Label(image=imagee)
        Labelimg.place(relx=0.3, rely=0.3, height=200, width=200)
        parser = createParser(fileopen)
        # extraction des métadonnées
        metadata = extractMetadata(parser)
        # affichage des métadonnées
        Labelpath = Label(text=metadata, bg='ivory', justify=LEFT)
        Labelpath.place(relx=0.3, rely=0.6, height=250, width=250)

    Button2 = Button(text="Ouvrir un fichier", command=openfile)
    Button2.place(relx=0.3, rely=0.2, height=31, width=94)

    def back():
        mtdt.destroy()
        # execfile('image steganography using lsb.py')
        # os.system('python imagesteganographyusinglsb.py')
        Popen('python steganography.py')

    Buttonback = Button(text="QUITTER", command=back)
    Buttonback.place(relx=0.4, rely=0.2, height=31, width=94)

    mtdt.mainloop()

# PROGRAMME PRINCIPAL
main = Tk()
main.title('STEGANOGRAPHIE')
main.geometry('1000x1000')
main.resizable(width=True,height=True)
fontl = tkFont.Font(family='Arial', size=32)

label = Label(main)
label.pack()

encbutton = Button(text='CACHER UN MESSAGE', fg="white", bg="black", width=25, command=encode)
encbutton['font'] = fontl
encbutton.place(relx=0.3, rely=0.1)

decbutton = Button(text='DECODER UN MESSAGE', fg="white", bg="black", width=25, command=decode)
decbutton['font'] = fontl
decbutton.place(relx=0.3, rely=0.25)

metabutton = Button(text='AFFICHER METADONNEES', fg="white", bg="black", width=25, command=metadata)
metabutton['font'] = fontl
metabutton.place(relx=0.3, rely=0.4)

def exit():
    main.destroy()

closebutton = Button(text='QUITTER', fg="white", bg="red", width=25, command=exit)
closebutton['font'] = fontl
closebutton.place(relx=0.3, rely=0.7)
main.mainloop()
