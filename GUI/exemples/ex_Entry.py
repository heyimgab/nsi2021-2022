from tkinter import*

#Fonction
def affichage():
    ch=zone.get()
    label.config(text=ch)
    zone.delete(0,len(ch))

#Programme principal
fen=Tk()

label=Label(fen,text="Entrer un texte")
label.pack()

zone=Entry(fen,bg="white",fg="blue",width=55)
zone.pack()

bouton=Button(fen,text="Valider",command=affichage)
bouton.pack()

fen.mainloop()

