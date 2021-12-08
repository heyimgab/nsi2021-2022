from tkinter import *

fen=Tk()

photo=PhotoImage(file="andromede2.gif")

fen.geometry("800x600")
fen.title("800x600")

fond=Canvas(fen, bg='blue',width=600,height=300)
fond.pack()

for i in range(1,6):
	fond.create_line(i*100,0,i*100,300) 
for i in range(1,3):
	fond.create_line(0,i*100,600,i*100) 
	
img=fond.create_image(400,100,image=photo)

fen.mainloop()

