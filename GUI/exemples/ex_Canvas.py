from tkinter import*

fen=Tk()

zone_dessin=Canvas(fen,width=200,height=200)
zone_dessin.pack()

zone_dessin.create_line(0,0,200,200,fill="violet",width=2)
zone_dessin.create_line(0,200,200,0,fill="violet",width=2)

rec=zone_dessin.create_rectangle(50,50,150,150,fill="red")

cercle=zone_dessin.create_oval(75,75,125,125,fill="yellow",outline="green",width=3)

texte=zone_dessin.create_text(100,100,text="Vive la\n  NSI",fill="blue")

fen.mainloop()



