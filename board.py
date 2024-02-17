from tkinter import Tk, Button, Label


def click(button):
    button.grid_forget()


class GameBoard:

    def __init__(self):

        self.window = Tk()
        self.window.title("Tic Tac Toe")
        self.window.minsize(width=500, height=300)

        self.label1 = Label(height=10, width=25, text="X")
        self.label1.grid(row=0, column=0)
        self.button1 = Button(height=10, width=25, command=lambda: click(self.button1))
        self.button1.grid(row=0, column=0)

        self.label2 = Label(height=10, width=25, text="X")
        self.label2.grid(row=0, column=1)
        self.button2 = Button(height=10, width=25, command=lambda: click(self.button2))
        self.button2.grid(row=0, column=1)

        self.label3 = Label(height=10, width=25, text="X")
        self.label3.grid(row=0, column=2)
        self.button3 = Button(height=10, width=25, command=lambda: click(self.button3))
        self.button3.grid(row=0, column=2)

        self.label4 = Label(height=10, width=25, text="X")
        self.label4.grid(row=1, column=0)
        self.button4 = Button(height=10, width=25, command=lambda: click(self.button4))
        self.button4.grid(row=1, column=0)

        self.label5 = Label(height=10, width=25, text="X")
        self.label5.grid(row=1, column=1)
        self.button5 = Button(height=10, width=25, command=lambda: click(self.button5))
        self.button5.grid(row=1, column=1)

        self.label6 = Label(height=10, width=25, text="X")
        self.label6.grid(row=1, column=2)
        self.button6 = Button(height=10, width=25, command=lambda: click(self.button6))
        self.button6.grid(row=1, column=2)

        self.label7 = Label(height=10, width=25, text="X")
        self.label7.grid(row=2, column=0)
        self.button7 = Button(height=10, width=25, command=lambda: click(self.button7))
        self.button7.grid(row=2, column=0)

        self.label8 = Label(height=10, width=25, text="X")
        self.label8.grid(row=2, column=1)
        self.button8 = Button(height=10, width=25, command=lambda: click(self.button8))
        self.button8.grid(row=2, column=1)

        self.label9 = Label(height=10, width=25, text="X")
        self.label9.grid(row=2, column=2)
        self.button9 = Button(height=10, width=25, command=lambda: click(self.button9))
        self.button9.grid(row=2, column=2)

        self.turn_label = Label(height=10, width=25, text="Turn:")

        self.restart_button = Button(text="Restart")
        self.restart_button.grid(row=3, column=1)

        self.window.mainloop()

