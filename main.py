import tkinter as tk
from PIL import Image, ImageTk

def count():
    result=0
    for i in range (len(lis)):
        a=lis[i].get()
        if a=="":
            a=0
        result+=int(a)*lis_num[i]
    ans.delete(0, tk.END)
    ans.insert(0, str(result))


win=tk.Tk()
win.geometry("1100x1300")
win.config(bg="pink")

lis_num=[10, 50, 100, 200, 500, 1000, 2000, 5000]

photo1=Image.open("10.jpg")
photo1=photo1.resize((250, 120))
photo1_new=ImageTk.PhotoImage(photo1)
photo1_label=tk.Label(win, image=photo1_new)
photo1_label.place(x=10, y=10)
photo1_ent=tk.Entry(win, width=15)
photo1_ent.place(x=85, y=150)

photo2=Image.open("50.jpeg")
photo2=photo2.resize((250, 120))
photo2_new=ImageTk.PhotoImage(photo2)
photo2_label=tk.Label(win, image=photo2_new)
photo2_label.place(x=270, y=10)
photo2_ent=tk.Entry(win, width=15)
photo2_ent.place(x=335, y=150)

photo3=Image.open("100.jpeg")
photo3=photo3.resize((250, 120))
photo3_new=ImageTk.PhotoImage(photo3)
photo3_label=tk.Label(win, image=photo3_new)
photo3_label.place(x=530, y=10)
photo3_ent=tk.Entry(win, width=15)
photo3_ent.place(x=595, y=150)

photo4=Image.open("200.jpeg")
photo4=photo4.resize((250, 120))
photo4_new=ImageTk.PhotoImage(photo4)
photo4_label=tk.Label(win, image=photo4_new)
photo4_label.place(x=790, y=10)
photo4_ent=tk.Entry(win, width=15)
photo4_ent.place(x=855, y=150)

photo5=Image.open("500.jpeg")
photo5=photo5.resize((250, 120))
photo5_new=ImageTk.PhotoImage(photo5)
photo5_label=tk.Label(win, image=photo5_new)
photo5_label.place(x=10, y=230)
photo5_ent=tk.Entry(win, width=15)
photo5_ent.place(x=85, y=370)

photo6=Image.open("1000.jpeg")
photo6=photo6.resize((250, 120))
photo6_new=ImageTk.PhotoImage(photo6)
photo6_label=tk.Label(win, image=photo6_new)
photo6_label.place(x=270, y=230)
photo6_ent=tk.Entry(win, width=15)
photo6_ent.place(x=335, y=370)

photo7=Image.open("2000.jpeg")
photo7=photo7.resize((250, 120))
photo7_new=ImageTk.PhotoImage(photo7)
photo7_label=tk.Label(win, image=photo7_new)
photo7_label.place(x=530, y=230)
photo7_ent=tk.Entry(win, width=15)
photo7_ent.place(x=595, y=370)

photo8=Image.open("5000.jpeg")
photo8=photo8.resize((250, 120))
photo8_new=ImageTk.PhotoImage(photo8)
photo8_label=tk.Label(win, image=photo8_new)
photo8_label.place(x=790, y=230)
photo8_ent=tk.Entry(win, width=15)
photo8_ent.place(x=855, y=370)

emoji = "\U0001F4B8"
text=tk.Label(win, text="Введите количество купюр и программа посчитает сумму", font=("Calibri", 20, "bold"), bg="pink", fg="black")
text.place(x=150, y=470)

text1=tk.Label(win, text=f"{emoji}", font=("Calibri", 30), bg="pink", fg="#26c406")
text1.place(x=835, y=465)


ans=tk.Entry(win, width=35)
ans.place(x=430, y=550)
pysk=tk.Button(win, text="Посчитать", font=("Calibri", 25, "bold"), command=count)
pysk.place(x=450, y=590)

lis=[photo1_ent, photo2_ent, photo3_ent, photo4_ent, photo5_ent, photo6_ent, photo7_ent, photo8_ent]


win.mainloop()