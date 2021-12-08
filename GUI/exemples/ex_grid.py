from tkinter import*

#Programme principal
fen=Tk()

label1=Label(text="Label 1",width=20)
label1.grid(column=0,row=0)

zone=Entry(width=5)
zone.grid(column=0,row=1,sticky="W")

label2=Label(text="Label 2",bd=2,relief=SOLID)
label2.grid(column=1,row=1)

bouton=Button(text="Bouton")
bouton.grid(column=0,row=2,columnspan=2,pady=8)

fen.mainloop()

