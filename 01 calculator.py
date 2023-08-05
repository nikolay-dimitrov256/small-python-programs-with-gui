import tkinter as tk
from math import sqrt


class Calculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Calculator')

        self.entry = tk.Entry(self.root, width=50, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=4)

        self.buttons = []
        self.first_num = 0
        self.second_num = 0
        self.operation = ''
        self.floating_point = False
        self.calculated = False
        self.result = 0

        self.create_buttons()
        self.position_buttons()

    def create_buttons(self):
        button_text = [
            '%', '√', 'C', '←',
            '7', '8', '9', '/',
            '4', '5', '6', '×',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        for index, text in enumerate(button_text):
            # Here I'm trying to even out the buttons.
            pad_x = 30
            if index % 4 == 0 and text.isdigit():
                pad_x = 32
            elif index % 4 == 1 and text.isdigit():
                pad_x = 32
            elif index % 2 == 0 and text.isdigit():
                pad_x = 31
            elif text in '/-':
                pad_x = 32
            elif text == '.':
                pad_x = 34
            elif text == '√':
                pad_x = 31

            # Set the button color
            if index < 4:
                color = 'white'
            elif index < 8:
                color = 'green'
            elif index < 12:
                color = 'red'
            elif index < 16:
                color = 'blue'
            else:
                color = 'yellow'

            button = tk.Button(self.root, text=text, padx=pad_x, pady=20,
                               command=lambda t=text: self.button_click(t), bg=color)
            self.buttons.append(button)

    def position_buttons(self):
        row = 1
        col = 0

        for button in self.buttons:
            button.grid(row=row, column=col, padx=1, pady=1)
            col += 1

            if col > 3:
                col = 0
                row += 1

    def button_click(self, text):
        if self.entry.get() == 'Cannot divide by zero!':
            self.clear_field()

        if text == 'C':
            self.clear_field()

        elif text.isdigit():
            if self.calculated:
                self.entry.delete(0, tk.END)
                self.calculated = False

            self.entry.insert(tk.END, text)

        elif text == '.':
            if self.calculated:
                self.entry.delete(0, tk.END)
                self.calculated = False

            if not self.floating_point:
                if not self.entry.get():
                    self.entry.insert(tk.END, '0.')
                else:
                    self.entry.insert(tk.END, text)
                self.floating_point = True

        elif text in '/×-+':
            if self.operation and not self.calculated:
                if not self.entry.get():
                    self.second_num = 0.00
                else:
                    self.second_num = float(self.entry.get())
                self.result = self.calculate(self.first_num, self.second_num, self.operation)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, self.result)
                self.operation = text
                self.first_num = self.result
                self.calculated = True

            elif self.operation and self.calculated:
                self.operation = text

            else:
                self.operation = text
                if not self.entry.get():
                    self.first_num = 0.0
                else:
                    self.first_num = float(self.entry.get())
                self.entry.delete(0, tk.END)

            self.floating_point = False

        elif text == '%':
            self.second_num = float(self.entry.get()) if self.entry.get() else 0.0
            if self.operation:
                if self.operation in '+-':
                    self.second_num = self.first_num * self.second_num / 100
                elif self.operation in '/×':
                    self.second_num = self.second_num / 100

            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(self.second_num))

        elif text == '√':
            self.first_num = float(self.entry.get())
            self.result = sqrt(self.first_num)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(self.result))

        elif text == '←':
            index = len(self.entry.get()) - 1
            self.entry.delete(index, tk.END)

        elif text == '=':
            if not self.entry.get() and not self.calculated:
                self.second_num = 0.0
            elif self.entry.get() and not self.calculated:
                self.second_num = float(self.entry.get())

            if not self.operation:
                self.result = self.second_num
            else:
                self.result = self.calculate(self.first_num, self.second_num, self.operation)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, self.result)
            self.first_num = self.result
            self.calculated = True

    def clear_field(self):
        self.entry.delete(0, tk.END)
        self.first_num = 0
        self.second_num = 0
        self.operation = ''
        self.floating_point = False
        self.calculated = False
        self.result = 0

    def calculate(self, first_num, second_num, operation):
        result = ''
        if operation == '/':
            if second_num == 0.0:
                result = 'Cannot divide by zero!'
            else:
                result = first_num / second_num
        elif operation == '×':
            result = first_num * second_num
        elif operation == '-':
            result = first_num - second_num
        elif operation == '+':
            result = first_num + second_num

        return result

    def run(self):
        self.root.mainloop()


calculator = Calculator()
calculator.run()
