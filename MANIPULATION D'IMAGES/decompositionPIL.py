from PIL import Image

nom_fichier=input("Entrez le nom du fichier : ")
im=Image.open(nom_fichier)
taille=im.size


image1=Image.new("RGB",taille)
image2=Image.new("RGB",taille)
image3=Image.new("RGB",taille)

for i in range (0,taille[0]):
    for j in range (0,taille[1]):
        pixel=im.getpixel((i,j))
        if i==0:
            print(pixel)
        image1.putpixel((i,j),(pixel[0],0,0))
        image2.putpixel((i,j),(0,pixel[1],0))
        image3.putpixel((i,j),(0,0,pixel[2]))
                        
image1.save("image1.bmp")
image2.save("image2.bmp")
image3.save("image3.bmp")

        

