import glob
import os

from PIL import Image
import matplotlib.pyplot as plt

bilder = glob.glob("./Bilder/*.png")
print(bilder)
for bild in bilder:
    print(bild)
    img = Image.open(bild)
    plt.imshow(img)
    plt.axis('off')  # Deaktivieren der Achsenbeschriftung
    plt.show()

    # Tastatureingabe abfragen
    user_input = input("Drücken Sie Enter, um fortzufahren, oder 'n', um das Bild zu löschen: ")

    if user_input.lower() == 'n':
        # Bild löschen
        os.remove(bild)
        print(f"Bild {bild} wurde gelöscht.")
