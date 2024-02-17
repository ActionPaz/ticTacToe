from tkinter import Tk, Button, Label

window = Tk()
window.title("Tic Tac Toe")
window.minsize(width=500, height=300)


def set_board():
    label1 = Label(height=10, width=25, text="X")
    label1.grid(row=0, column=0)
    button1 = Button(height=10, width=25, command=lambda: click(button1))
    button1.grid(row=0, column=0)

    label2 = Label(height=10, width=25, text="X")
    label2.grid(row=0, column=1)
    button2 = Button(height=10, width=25, command=lambda: click(button2))
    button2.grid(row=0, column=1)

    label3 = Label(height=10, width=25, text="X")
    label3.grid(row=0, column=2)
    button3 = Button(height=10, width=25, command=lambda: click(button3))
    button3.grid(row=0, column=2)

    label4 = Label(height=10, width=25, text="X")
    label4.grid(row=1, column=0)
    button4 = Button(height=10, width=25, command=lambda: click(button4))
    button4.grid(row=1, column=0)

    label5 = Label(height=10, width=25, text="X")
    label5.grid(row=1, column=1)
    button5 = Button(height=10, width=25, command=lambda: click(button5))
    button5.grid(row=1, column=1)

    label6 = Label(height=10, width=25, text="X")
    label6.grid(row=1, column=2)
    button6 = Button(height=10, width=25, command=lambda: click(button6))
    button6.grid(row=1, column=2)

    label7 = Label(height=10, width=25, text="X")
    label7.grid(row=2, column=0)
    button7 = Button(height=10, width=25, command=lambda: click(button7))
    button7.grid(row=2, column=0)

    label8 = Label(height=10, width=25, text="X")
    label8.grid(row=2, column=1)
    button8 = Button(height=10, width=25, command=lambda: click(button8))
    button8.grid(row=2, column=1)

    label9 = Label(height=10, width=25, text="X")
    label9.grid(row=2, column=2)
    button9 = Button(height=10, width=25, command=lambda: click(button9))
    button9.grid(row=2, column=2)

    restart_button = Button(text="Restart")
    restart_button.grid(row=3, column=1)

    window.mainloop()


def click(button):
    button.grid_forget()


if __name__ == "__main__":
    set_board()