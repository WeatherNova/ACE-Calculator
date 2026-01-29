from tkinter import *
import tkinter as tk

class ACECalculator:
    def __init__(self):
        self.initialize_window()
        self.window.mainloop()
    def initialize_window(self):
        self.window = Tk()
        self.window.title("ACE Calculator")
        self.window.resizable(width=False, height=False)
        self.window.geometry("400x400")
        # Some initial values
        self.values = tk.BooleanVar()
        self.value = tk.StringVar()
        self.prevval = 0

        # Entry for winds
        self.label = tk.Label(self.window, text='Windspeed (kt)')
        self.label.pack()
        self.entry = tk.Entry(self.window, textvariable=self.value, relief='groove')
        self.entry.pack()

        # Buttons
        self.submit = tk.Button(self.window, text='Calculate', command=lambda:self.ace_calculate(int(self.entry.get())))
        self.submit.pack()
        self.clear = tk.Button(self.window, text='Clear', command=lambda:self.clearfunc())
        self.clear.pack()

        # Output textbox
        self.textlabel = tk.Label(self.window, text='Total ACE')
        self.textlabel.pack()
        self.textbox = tk.Text(self.window, height=17, width=30, state='disabled', relief='groove')
        self.textbox.pack()

    def ace_calculate(self, value):
        if value < 34:
            if self.prevval == 0:
                summation = 0
            else:
                summation = self.prevval
            summation_raw = 0
        else:
            summation = round(10**-4 * sum(value**2 for i in range(1, 1 + 1)), 4)
            summation_raw = summation
            if self.prevval != 0:
                summation = summation + self.prevval
                self.prevval = summation
            else:
                self.prevval = summation

        self.textbox.config(state='normal')
        self.textbox.insert(tk.END, f'{value}kt | {round(summation,4)} (+{summation_raw})\n')
        self.textbox.config(state='disabled')
    def clearfunc(self):
        self.value.set('')
        self.prevval = 0
        self.textbox.config(state='normal')
        self.textbox.delete(1.0, tk.END)
        self.textbox.config(state='disabled')
ACECalculator()