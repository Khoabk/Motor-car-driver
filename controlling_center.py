from tkinter import *
from tkinter import messagebox

root = Tk()



dir = []


for i in range(4):
    dir.append(StringVar())
    dir[i].set("0")






sp1 = StringVar()
sp2 = StringVar()
sp3 = StringVar()
sp4 = StringVar()


sp1.set("0")
sp2.set("0")
sp3.set("0")
sp4.set("0")


sp1_val = Label(root, textvariable = sp1, font =('calibre',10), width = 3, bg = "white")
sp2_val = Label(root, textvariable = sp2, font =('calibre',10), width = 3, bg = "white")
sp3_val = Label(root, textvariable = sp3, font =('calibre',10), width = 3, bg = "white")
sp4_val = Label(root, textvariable = sp4, font =('calibre',10), width = 3, bg = "white")


sp1_lb = Label(root, text = 'sp1', font =('calibre',10, 'bold'))
sp2_lb = Label(root, text = 'sp2', font =('calibre',10, 'bold'))
sp3_lb = Label(root, text = 'sp3', font =('calibre',10, 'bold'))
sp4_lb = Label(root, text = 'sp4', font =('calibre',10, 'bold'))





m1_var = StringVar()
m2_var = StringVar()
m3_var = StringVar()
m4_var = StringVar()

m1_var.set("0")
m2_var.set("0")
m3_var.set("0")
m4_var.set("0")


M1 = Entry(root, textvariable = m1_var, width = 3)
M2 = Entry(root, textvariable = m2_var,width = 3)
M3 = Entry(root, textvariable = m3_var,width = 3)
M4 = Entry(root, textvariable = m4_var,width = 3)


M1_lb = Label(root, text = 'M1', font =('calibre',10, 'bold'))
M2_lb = Label(root, text = 'M2', font =('calibre',10, 'bold'))
M3_lb = Label(root, text = 'M3', font =('calibre',10, 'bold'))
M4_lb = Label(root, text = 'M4', font =('calibre',10, 'bold'))


root.title("Controller")

root.geometry("322x200")


def click():

    try:

        m1_speed = int(m1_var.get())%200

        m2_speed = int(m2_var.get())%200

        m3_speed = int(m3_var.get())%200

        m4_speed = int(m4_var.get())%200

        print("M1:","{0:0=3d}".format(m1_speed)," M2:","{0:0=3d}".format(m2_speed)," M3:","{0:0=3d}".format(m3_speed)," M4:","{0:0=3d}".format(m4_speed))

        sp1.set("{0:0=3d}".format(m1_speed))

        sp2.set("{0:0=3d}".format(m2_speed))

        sp3.set("{0:0=3d}".format(m3_speed))

        sp4.set("{0:0=3d}".format(m4_speed))



    except:

        messagebox.showinfo("warning","please insert a number")


button = Button(root, text = "Click me", command = click, height = 2, width = 10)

button.place(x=220, y = 140)



sp1_val.place(x = 20 - 3, y =  30)
sp2_val.place(x = 70 - 3, y =  30)
sp3_val.place(x = 120 - 3, y = 30)
sp4_val.place(x = 170 - 3, y = 30)


sp1_lb.place(x = 20 - 3, y =  8)
sp2_lb.place(x = 70 - 3, y =  8)
sp3_lb.place(x = 120 - 3, y = 8)
sp4_lb.place(x = 170 - 3, y = 8)


M1.place(x = 20, y =  150)
M2.place(x = 70, y =  150)
M3.place(x = 120, y =  150)
M4.place(x = 170, y =  150)

M1_lb.place(x = 20 - 3, y = 130)
M2_lb.place(x = 70 - 3, y = 130)
M3_lb.place(x = 120 - 3, y = 130)
M4_lb.place(x = 170 - 3, y = 130)

root.mainloop()
