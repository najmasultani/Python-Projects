# Title: Simple Calculator
# Description: This program creates a simple calculator using the tkinter library.

from tkinter import *

# Function to handle button click
def button_click(num):
    global equation_text
    equation_text += str(num)
    equation_label.set(equation_text)

# Function to handle equal button click
def button_equal():
    global equation_text
    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except ZeroDivisionError:
        equation_label.set('Error')
        equation_text = ''
    except SyntaxError:
        equation_label.set('Error')
        equation_text = ''

# Function to clear the calculator
def button_clear():
    global equation_text
    equation_label.set('')
    equation_text = ''

# Function to change the sign of the number
def button_sign():
    global equation_text
    equation_text = str(int(equation_text) * -1)
    equation_label.set(equation_text)

# Function to calculate the percentage of the number
def button_percent():
    global equation_text
    equation_text = str(int(equation_text) / 100)
    equation_label.set(equation_text)

# Create the main window
root = Tk()
root.title('Simple Calculator')

equation_text = ""
equation_label = StringVar()

# Create the equation label
label = Label(
    root,
    textvariable=equation_label,
    font=('Arial', 20),
    bg='#CCE3F5',
    fg='black',
    bd=4,
    width=40,
    height=2,
    cursor='arrow',
    relief='ridge'
)
label.pack(padx=20, pady=10)

frame = Frame(root)
frame.pack()

# Create the buttons
b1 = Button(frame, text='1', command=lambda: button_click(1), padx=40, pady=20)
b2 = Button(frame, text='2', command=lambda: button_click(2), padx=40, pady=20)
b3 = Button(frame, text='3', command=lambda: button_click(3), padx=40, pady=20)
b4 = Button(frame, text='4', command=lambda: button_click(4), padx=40, pady=20)
b5 = Button(frame, text='5', command=lambda: button_click(5), padx=40, pady=20)
b6 = Button(frame, text='6', command=lambda: button_click(6), padx=40, pady=20)
b7 = Button(frame, text='7', command=lambda: button_click(7), padx=40, pady=20)
b8 = Button(frame, text='8', command=lambda: button_click(8), padx=40, pady=20)
b9 = Button(frame, text='9', command=lambda: button_click(9), padx=40, pady=20)
b0 = Button(frame, text='0', command=lambda: button_click(0), padx=100, pady=20)
b_add = Button(frame, text='+', command=lambda: button_click('+'), padx=40, pady=20)
b_equal = Button(frame, text='=', command=button_equal, padx=40, pady=20)
b_clear = Button(frame, text='C', command=button_clear, padx=40, pady=20)
b_subtract = Button(frame, text='-', command=lambda: button_click('-'), padx=40, pady=20)
b_multiply = Button(frame, text='*', command=lambda: button_click('*'), padx=40, pady=20)
b_divide = Button(frame, text='/', command=lambda: button_click('/'), padx=42, pady=20)
b_decimal = Button(frame, text='.', command=lambda: button_click('.'), padx=43, pady=20)
b_percent = Button(frame, text='%', command=button_percent, padx=38, pady=20)
b_signChange = Button(frame, text='+/-', command=button_sign, padx=35, pady=20)

# Grid layout for buttons
b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)

b4.grid(row=3, column=0)
b5.grid(row=3, column=1)
b6.grid(row=3, column=2)

b1.grid(row=4, column=0)
b2.grid(row=4, column=1)
b3.grid(row=4, column=2)

b0.grid(row=5, column=0, columnspan=2)
b_add.grid(row=4, column=3)
b_equal.grid(row=5, column=3)
b_clear.grid(row=1, column=0)
b_subtract.grid(row=3, column=3)
b_multiply.grid(row=2, column=3)
b_divide.grid(row=1, column=3)
b_decimal.grid(row=5, column=2)
b_percent.grid(row=1, column=2)
b_signChange.grid(row=1, column=1)

root.mainloop()
