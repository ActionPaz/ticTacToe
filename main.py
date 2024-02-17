from tkinter import Tk, Button

window = Tk()
window.title("Tic Tac Toe")
window.minsize(width=500, height=300)

button1 = Button(height=10, width=25)
button1.grid(row=0, column=0)

button2 = Button(height=10, width=25)
button2.grid(row=0, column=1)

button3 = Button(height=10, width=25)
button3.grid(row=0, column=2)

button4 = Button(height=10, width=25)
button4.grid(row=1, column=0)

button5 = Button(height=10, width=25)
button5.grid(row=1, column=1)

button6 = Button(height=10, width=25)
button6.grid(row=1, column=2)

button7 = Button(height=10, width=25)
button7.grid(row=2, column=0)

button8 = Button(height=10, width=25)
button8.grid(row=2, column=1)

button9 = Button(height=10, width=25)
button9.grid(row=2, column=2)

restart_button = Button(text="Restart")
restart_button.grid(row=3, column=1)


window.mainloop()