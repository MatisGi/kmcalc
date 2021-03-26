from tkinter import *
from tkinter import ttk


#Loome akna ja selle seaded
aken = Tk()
aken.title("Km-kalkulaator")
aken.geometry("400x200")
aken.resizable(0,0)

nr=0
käibemaksuga = 0

def teeMidagi():
    global nr
    nr=int(rbValue.get())/int(sisestus.get())*100 #võtab tekstikasti sisu ja radiobutton väärtuse
    käibemaksuga = int(sisestus.get())+nr
    tekstikast4_1.config(text=str(käibemaksuga)+"€")
    tekstikast3_1.config(text=str(nr)+"%") #lisab Tekstikastile uue sisu
#radiobutton
rbValue=IntVar()
vk1 = Radiobutton(aken, text="9%",variable=rbValue, value=9)
vk1.grid(row=1, column=1)
vk2 = Radiobutton(aken, text="20%", variable=rbValue, value=20)
vk2.grid(row=2, column=1)

#sisestusväli
sisestus = Entry(aken, width=20, font="Tahoma 12")
sisestus.grid(row=0, column=1)

#Kasutan sisu paigutamiseks grid() meetodit

tekstikast = Label(aken, text="Hind käibemaksuta:", width=20, font="Tahoma 12")
tekstikast.grid(row=0, column=0)
tekstikast2 = Label(aken, text="Käibemaksumäär:", width=20, font="Tahoma 12")
tekstikast2.grid(row=1, column=0)
tekstikast3 = Label(aken, text="Käibemaks:", width=20, font="Tahoma 12")
tekstikast3.grid(row=4, column=0)
tekstikast3_1 = Label(aken, text="0.00%", width=20, font="Tahoma 12")
tekstikast3_1.grid(row=4, column=1)
tekstikast4 = Label(aken, text="Hind käibemaksuga:", width=20, font="Tahoma 12")
tekstikast4.grid(row=5, column=0)
tekstikast4_1 = Label(aken, text="0.00€", width=20, font="Tahoma 12")
tekstikast4_1.grid(row=5, column=1)
#nupud
Button(aken, text="OK", width=10, font="Tahoma 12", command=teeMidagi).grid(row=6, column=1, padx=2, pady=2)

aken.mainloop()