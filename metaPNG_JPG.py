from hachoir.parser import createParser
from hachoir.metadata import extractMetadata

#Attribution du chemin de l'image à une variable
filename = input("donner le chemin du fichier:")

parser = createParser(filename)
#extraction des métadonnées
metadata = extractMetadata(parser)
#affichage des métadonnées
print(metadata)