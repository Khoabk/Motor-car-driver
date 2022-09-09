from tkinter import *
from tkinter import messagebox
import serial, threading
import sys

class control_center:

    order_lb = []
    speed_entry = []
    feedback = []
    dir = []
    speed_var = []
    feedback_var = []
    dir_var = []

    is_listening = 0

    def __init__(self, gui):
        self.root = gui
        self.root.protocol("WM_DELETE_WINDOW", self.handler)
        self.createWidgets()
        self.start_listening()

    def handler(self):
        if self.is_listening == 1:
            self.listenEvent.set()

        self.serialPort.close()
        self.root.destroy()
        sys.exit()


    def listen_serial(self):

        try:
            self.serialPort = serial.Serial(port = "COM4", baudrate=115200,bytesize=8, timeout= 0.5, stopbits=serial.STOPBITS_ONE)
            serialString = ""
            while(1):

            #    print("in loop")
                try:

                    # if self.listenEvent.isSet() :
                    #
                    #     break

                    if self.serialPort.inWaiting() > 0:

                        if self.listenEvent.isSet() :

                            break

                        serialString = self.serialPort.read_until(expected = '#')

                        for i in range(4):
                            self.feedback_var[i].set(str(serialString[(i+1)*2]%100))
                            self.dir_var[i].set(str(int(serialString[(i+1)*2]/100)))

                        m1 = serialString[2]
                        m2 = serialString[4]
                        m3 = serialString[6]
                        m4 = serialString[8]

                        print(str(m1) + " " + str(m2) + " " + str(m3) + " " + str(m4))

                except:

                    break

        except:

            print("Coudn't open port")

    def start_listening(self):
        if self.is_listening == 0:
            t = threading.Thread(target = self.listen_serial)
            t.deamon = True
            t.start()
            self.listenEvent = threading.Event()
            self.listenEvent.clear()

            self.is_listening = 1
        else:
            print("Is listening")


    def click(self):

        #try:

        message = "!drv:"

        for i in range(4):
            sp = int(self.speed_var[i].get())%200
            message+="{0:0=3d}".format(sp)
            if i != 3:
                message+=":"
            else:
                message+="#"

        print(message)

        self.serialPort.write(message.encode())

    #

    #    return
    def createWidgets(self):
        self.root.title("Controller")
        self.root.geometry("320x180")

        self.speed_lb = Label(self.root, text = "Spd", font = ('calibre',10, 'bold'))
        self.feedback_lb = Label(self.root, text = "Fbk", font = ('calibre',10, 'bold'))
        self.dir_lb = Label(self.root, text = "Dir", font = ('calibre',10, 'bold'))
        self.send_button = Button(self.root, text = "Send", command = self.click, height = 0, width = 5, bg = "white", font = ('calibre',10, 'bold'))
    #    self.listen_button = Button(self.root, text = "Listen", command = self.start_listening, height = 0, width = 5, bg = "white", font = ('calibre',10, 'bold'))

        self.send_button.place(x = 260, y = 38)
    #    self.listen_button.place(x = 260, y = 88)
        self.speed_lb.place(x = 10, y = 20 + 20)
        self.feedback_lb.place(x = 10, y = 70 + 20)
        self.dir_lb.place(x = 10, y = 120 + 20)

        tab = 50

        for i in range(4):
            self.order_lb.append(Label(self.root, text = "M"+str(i+1), font = ('calibre',10,'bold')))
            self.speed_var.append(StringVar())
            self.feedback_var.append(StringVar())
            self.dir_var.append(StringVar())
            self.speed_var[i].set("0")
            self.feedback_var[i].set("0")
            self.dir_var[i].set("0")
            self.speed_entry.append(Entry(self.root, textvariable = self.speed_var[i], width = 4))
            self.feedback.append(Label(self.root, textvariable = self.feedback_var[i], font =('calibre',10), width = 3, bg = "white"))
            self.dir.append(Label(self.root, textvariable = self.dir_var[i], font =('calibre',10), width = 3, bg = "white"))
            self.order_lb[i].place(x = (i + 1)*tab + 20, y = 15)
            self.speed_entry[i].place(x = (i + 1)*tab + 20, y = 42)
            self.feedback[i].place(x = (i + 1)*tab + 20, y = 92)
            self.dir[i].place(x = (i + 1)*tab + 20, y = 142)
