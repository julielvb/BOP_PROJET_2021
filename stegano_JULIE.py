# importation des fonctionnalités de TKINTER
from tkinter import *
from tkinter import messagebox          # module de fenêtre popup
from tkinter import font as tkFont      # module des polices d'écriture
from tkinter.filedialog import *        # module de récupération d'une image
# importation des fonctionnalités de PIL
from PIL import ImageTk, Image
# importation des fonctionnalités de STEGANO
from stegano import lsb
from stegano import exifHeader as aaa
import os
from subprocess import Popen
from argparse import FileType

# fonction pour encoder un message dans une image
def encode():
    main.destroy()
    enc = Tk()
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

        Labelimg = Label(image=imagee)
        Labelimg.place(relx=0.3, rely=0.3, height=200, width=200)

    Button2 = Button(text="Ouvrir un fichier", command=openfile)
    Button2.place(relx=0.3, rely=0.2, height=31, width=94)

    # BOUTON DE SELECTION ENTRE JPEG (RADIO1) ET PNG (RADIO2) POUR CONVERTIR LE FICHIER ENCODE
    secimg = StringVar()
    radio1 = Radiobutton(text='jpeg', value='jpeg', variable=secimg)
    radio1.place(relx=0.3, rely=0.57)

    radio2 = Radiobutton(text='png', value='png', variable=secimg)
    radio2.place(relx=0.5, rely=0.57)

    Label1 = Label(text="Entrer un message")
    Label1.place(relx=0.3, rely=0.6, height=21)
    entrysecmes = Entry()
    entrysecmes.place(relx=0.45, rely=0.6, relheight=0.05, relwidth=0.200)

    Label2 = Label(text="Nouveau nom du fichier")
    Label2.place(relx=0.3, rely=0.70, height=21, width=134)
    entrysave = Entry()
    entrysave.place(relx=0.45, rely=0.70, relheight=0.05, relwidth=0.200)

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

# FONCTION PUR DECODER
def decode():
    main.destroy()
    dec = Tk()
    dec.geometry('1000x1000')
    dec.resizable(width=True, height=True)
    dec.wm_attributes('-transparentcolor')
    fontl = tkFont.Font(family='Arial', size=32)
    label1 = Label(dec)
    label1.pack()

    LabelTitle = Label(text="DECODER", bg="black", fg="white", width=20)
    LabelTitle['font'] = fontl
    LabelTitle.place(relx=0.3, rely=0.1)

    secimg = StringVar()
    radio1 = Radiobutton(text='jpeg', value='jpeg', variable=secimg)
    radio1.place(relx=0.3, rely=0.57)

    radio2 = Radiobutton(text='png', value='png', variable=secimg)
    radio2.place(relx=0.4, rely=0.57)

    def openfile():
        global fileopen
        global imagee
        fileopen = StringVar()
        fileopen = askopenfilename(initialdir="/Desktop", title="select file",
                                   filetypes=(("jpeg files, png file", "*jpg *png"), ("all files", "*.*")))

        imagee = ImageTk.PhotoImage(Image.open(fileopen))
        Labelpath = Label(text=fileopen)
        Labelpath.place(relx=0.6, rely=0.25, height=21, width=450)

        Labelimg = Label(image=imagee)
        Labelimg.place(relx=0.3, rely=0.3, height=200, width=200)

    def deimg():
        if secimg.get() == "png":
            messag = lsb.reveal(fileopen)

        if secimg.get() == "jpeg":
            messag = aaa.reveal(fileopen)

        Label2 = Label(text=messag)
        Label2.place(relx=0.7, rely=0.7, height=21, width=204)

    Button2 = Button(text="Ouvrir un fichier", command=openfile)
    Button2.place(relx=0.3, rely=0.2, height=31, width=94)

    Button2 = Button(text="DECODER", command=deimg)
    Button2.place(relx=0.3, rely=0.8, height=31, width=94)

    def back():
        dec.destroy()
        # execfile('image steganography using lsb.py')
        # os.system('python imagesteganographyusinglsb.py')
        Popen('python steganography.py')

    Buttonback = Button(text="QUITTER", command=back)
    Buttonback.place(relx=0.3, rely=0.85, height=31, width=94)

    dec.mainloop()


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
encbutton.place(relx=0.3, rely=0.2)

decbutton = Button(text='REVELER UN MESSAGE', fg="white", bg="black", width=25, command=decode)
decbutton['font'] = fontl
decbutton.place(relx=0.3, rely=0.4)


def exit():
    main.destroy()


closebutton = Button(text='QUITTER', fg="white", bg="red", width=25, command=exit)
closebutton['font'] = fontl
closebutton.place(relx=0.3, rely=0.7)
main.mainloop()
