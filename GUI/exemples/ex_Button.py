from tkinter import*

#Fonction 
def plus():
    global nb
    nb=nb+1
    label.config(text=nb)

#Programme principal
fen=Tk()
fen.geometry("1280x720")

nb=0

label=Label(fen,text=nb)
label.pack()

bouton=Button(fen,text="Incrémenter",command=plus)
bouton.pack()

fen.mainloop()

