from tkinter import*

fen=Tk()

########### EXERCICE 1 ############
#fen.geometry("200x50")
#label=Label(fen,text="Bonjour tout le monde",fg="red")
#label.pack()
#bouton=Button(fen,text="Quitter",command=quit)
#bouton.pack()

########### EXERCICE 2 ############

def rayon():
    ch=zone.get()
    label.config(text=ch)
    zone.delete(0,len(ch))
        

fen.mainloop()