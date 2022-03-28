from PIL import Image

nom_fichier=input("Entrez le nom du fichier : ")
im=Image.open(nom_fichier)
taille=im.size
image1=Image.new("L", taille)

for i in range(0, taille[0]):
    for j in range(0, taille[1]):
        pixel = im.getpixel((i, j))
        if i == 0:
            print(pixel)
        image1.putpixel((i, j), (int(round(0.299 * pixel[0] + 0.587 * pixel[1] + O.114 * pixel[2]))))

image1.save("image1.bmp")

# gris = int(round(0.299 * red + 0.587 * green + 0.114 * blue)