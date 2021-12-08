from tkinter import*

#Fonction
def jouer():
    zoneJeu.config(text="Jouons")
    
#Programme principal
fen=Tk()

stat=Frame(fen,relief=SOLID,bd=2,bg="red")
labelVie=Label(stat,text="Nombre de vies")
labelVie.grid(row=0,column=0)
labelScore=Label(stat,text="Score")
labelScore.grid(row=0,column=1)
stat.grid(row=0,column=0,columnspan=2)

zoneJeu=Label(fen,text="Zone de jeu")
zoneJeu.grid(row=1,column=0)

commandes=Frame(fen,relief=SOLID,bd=1)
b1=Button(commandes,text="Jouer",command=jouer)
b1.pack()
b2=Button(commandes,text="Quitter",command=fen.destroy)
b2.pack()
commandes.grid(row=1,column=1)

fen.mainloop()

