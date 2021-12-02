from tkinter import *
from PIL import Image, ImageTk

# Création de la fenêtre graphique
fenetre = Tk()
fenetre.title("KAIJU")
fenetre.geometry('640x480')
fenetre.resizable(width=True,height=True)

# Création des widgets
label = Label(fenetre, text="Bonjour vous !")
bouton = Button(fenetre, text="Quitter", command=fenetre.destroy)

# Positionnement des widgets dans la fenêtre graphique avec la méthode pack()
label.pack()
bouton.pack()

# Canevas (toile)
canvas = Canvas(fenetre, width=500, height=500)
img = Image.open("IMG_2850.JPG")
ara = ImageTk.PhotoImage(Image.open("IMG_2850.JPG"))
canvas.create_image(500/2, 500/2, image=ara)
canvas.pack()

# Lancement du gestionnaire d’évènements
fenetre.mainloop()