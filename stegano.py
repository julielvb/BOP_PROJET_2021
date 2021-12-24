from stegano import lsb
from stegano import exifHeader

filename = input("Nom ou chemin du fichier : ")
secmes = input("Message secret : ")
format = input("Format du fichier : ")
newname = input("Nouveau nom du fichier : ")

if format == "png":
    secret = lsb.hide(filename, secmes)
    secret.save(newname)
    clear_message = lsb.reveal(newname)
    print("Message caché avec succès.\n",clear_message)

if format == "jpg":
    secret = exifHeader.hide(filename, newname, secret_message=secmes)
    print("Message caché avec succès.\n",exifHeader.reveal(newname))


# mode terminal
# stegano-lsb hide -i [name].png -m "Secret Message" -o [newname].png
# stegano-lsb reveal -i [name].png
