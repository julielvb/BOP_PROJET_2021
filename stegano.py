from stegano import lsb

secret = lsb.hide("kaiju.png", "Hello mama")
secret.save("kaiju_secret.png")
clear_message = lsb.reveal("kaiju_secret.png")

# mode terminal
# stegano-lsb hide -i [name].png -m "Secret Message" -o [newname].png
# stegano-lsb reveal -i [name].png
