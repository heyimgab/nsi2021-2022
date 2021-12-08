from tkinter import*
# Création de la fenêtre

fen=Tk()
fen.geometry("1280x720")

# Création d'un label
# obj1=Label({fenetre},text="Test",bg="{Couleur de fond}",fg="{Couleur de premier plan}",bd="{Taille des bordures}")

obj1=Label(fen,text="Zone de texte",bg="blue",fg="yellow",bd=100)
obj1.pack()

obj2=Label(fen,bitmap="question",bg="red",fg="grey",bd=11,relief=GROOVE)
obj2.pack()

fen.mainloop()

