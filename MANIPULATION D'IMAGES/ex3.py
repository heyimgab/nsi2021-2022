from PIL import Image

nom_fichier=input("Entrez le nom du fichier : ")
im=Image.open(nom_fichier)
taille=im.size
l=taille[0]
h=taille[1]

imageHorizontal=Image.new("RGB",taille)
imageVertical=Image.new("RGB",taille)
ImageRetournementComplet=Image.new("RGB", taille)

for i in range (0, taille[0]):
    for j in range (0,taille[1]):
        pixel=im.getpixel((i,j))
        imageHorizontal.putpixel((l-1-i,j),pixel)
        imageVertical.putpixel((i,h-1-j),pixel)
        ImageRetournementComplet.putpixel((l-1-i,h-1-j),pixel)

imageHorizontal.save("ImageHorizotal.bmp")
imageVertical.save("ImageVertical.bmp")
ImageRetournementComplet.save("ImageRetournementComplet.bmp")