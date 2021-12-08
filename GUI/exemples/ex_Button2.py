from tkinter import*

#Fonction 
def plus():
    nb.set(nb.get()+1)
#Programme principal
fen=Tk()
nb=IntVar()
nb.set(0)
label=Label(fen,textvariable=nb)
label.pack()
bouton=Button(fen,text="Incrémenter",command=plus)
bouton.pack()
fen.mainloop()

