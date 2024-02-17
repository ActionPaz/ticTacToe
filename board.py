import collections
from tkinter import Tk, Button, Label


class GameBoard:

    def __init__(self):

        self.turn = 1
        self.winning_combinations = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]
        self.x_list = []
        self.o_list = []
        self.game_over = False
        self.buttons = []

        self.window = Tk()
        self.window.title("Tic Tac Toe")
        self.window.minsize(width=500, height=300)

        self.label1 = Label(height=10, width=25, borderwidth=2, relief="solid")
        self.label1.grid(row=0, column=0)
        self.button1 = Button(height=10, width=25, command=lambda: self.click(self.button1, self.label1, 1))
        self.button1.grid(row=0, column=0)
        self.buttons.append(self.button1)

        self.label2 = Label(height=10, width=25, borderwidth=2, relief="solid")
        self.label2.grid(row=0, column=1)
        self.button2 = Button(height=10, width=25, command=lambda: self.click(self.button2, self.label2, 2))
        self.button2.grid(row=0, column=1)
        self.buttons.append(self.button2)

        self.label3 = Label(height=10, width=25, borderwidth=2, relief="solid")
        self.label3.grid(row=0, column=2)
        self.button3 = Button(height=10, width=25, command=lambda: self.click(self.button3, self.label3, 3))
        self.button3.grid(row=0, column=2)
        self.buttons.append(self.button3)

        self.label4 = Label(height=10, width=25, borderwidth=2, relief="solid")
        self.label4.grid(row=1, column=0)
        self.button4 = Button(height=10, width=25, command=lambda: self.click(self.button4, self.label4, 4))
        self.button4.grid(row=1, column=0)
        self.buttons.append(self.button4)

        self.label5 = Label(height=10, width=25, borderwidth=2, relief="solid")
        self.label5.grid(row=1, column=1)
        self.button5 = Button(height=10, width=25, command=lambda: self.click(self.button5, self.label5, 5))
        self.button5.grid(row=1, column=1)
        self.buttons.append(self.button5)

        self.label6 = Label(height=10, width=25, borderwidth=2, relief="solid")
        self.label6.grid(row=1, column=2)
        self.button6 = Button(height=10, width=25, command=lambda: self.click(self.button6, self.label6, 6))
        self.button6.grid(row=1, column=2)
        self.buttons.append(self.button6)

        self.label7 = Label(height=10, width=25, borderwidth=2, relief="solid")
        self.label7.grid(row=2, column=0)
        self.button7 = Button(height=10, width=25, command=lambda: self.click(self.button7, self.label7, 7))
        self.button7.grid(row=2, column=0)
        self.buttons.append(self.button7)

        self.label8 = Label(height=10, width=25, borderwidth=2, relief="solid")
        self.label8.grid(row=2, column=1)
        self.button8 = Button(height=10, width=25, command=lambda: self.click(self.button8, self.label8, 8))
        self.button8.grid(row=2, column=1)
        self.buttons.append(self.button8)

        self.label9 = Label(height=10, width=25, borderwidth=2, relief="solid")
        self.label9.grid(row=2, column=2)
        self.button9 = Button(height=10, width=25, command=lambda: self.click(self.button9, self.label9, 9))
        self.button9.grid(row=2, column=2)
        self.buttons.append(self.button9)

        self.turn_label = Label(height=10, width=25, text=f"Turn: {self.check_turn()}")
        self.turn_label.grid(row=3, column=0)

        self.restart_button = Button(text="Restart")
        self.restart_button.grid(row=3, column=1)

        self.window.mainloop()

    def click(self, button, label, index):
        button.grid_forget()
        self.buttons.remove(button)
        label.config(text=self.check_turn())
        self.update_status(self.check_turn(), index)
        if self.game_over:
            for button in self.buttons:
                button.config(state="disabled")
        else:
            self.turn += 1
            if self.turn > 9:
                self.turn_label.config(text=f"Game Over! It's a draw.")
            else:
                self.turn_label.config(text=f"Turn: {self.check_turn()}")

    def check_turn(self):
        if self.turn % 2 == 0:
            return "⭕"
        else:
            return "❌"

    def update_status(self, player, index):
        if player == "❌":
            self.x_list.append(index)
            self.x_list.sort()
            if self.x_list in self.winning_combinations:
                self.turn_label.config(text=f"Game Over! ❌ wins!")
                self.game_over = True
                return
        else:
            self.o_list.append(index)
            self.o_list.sort()
            if self.o_list in self.winning_combinations:
                self.turn_label.config(text=f"Game Over! ⭕ wins!")
                self.game_over = True
                return
