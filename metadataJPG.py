from PIL import Image
from PIL.ExifTags import TAGS

# ouverture de l'image
image = Image.open("IMG_2884.JPG")

# extraction des metadonnées
exifdata = image.getexif()

# boucle pour chaque tag des metadonnées
for tagid in exifdata:
    # conversion du numéro de tag par le nom
    tagname = TAGS.get(tagid, tagid)
    # mettre chaque tag à sa valeur
    value = exifdata.get(tagid)
    # si aucune donnée alors écrire "..."
    if isinstance(value, bytes):
        value = " "
    # affichage du résultat
    print(f"{tagname:20}: {value}")