from tkinter import *
import matplotlib.pyplot as plt
import numpy as np

window = Tk()
window.minsize(300, 300)
window.maxsize(300, 300)
window.config(pady=25)

def plot_function(y_value):
    x = np.linspace(-500, 500, 1000)
    y = eval(y_value)

    plt.plot(x, y)
    plt.grid(True, linestyle='--', linewidth=0.8, color='gray', alpha=0.8)

    plt.title('Function Chart: y = ' + y_value)
    plt.xlabel('X-axis')
    plt.ylabel('Y axis')

    plt.show()

label_one = Label(text="Please enter your function(write in parentheses) \n \n Denote the absolute value function as abs(function)")
label_one.pack(pady=10)

entry_one = Entry()
entry_one.pack()

def funactii():
    y_value = entry_one.get()
    plot_function(y_value)

button = Button(text="show chart", command=funactii)
button.pack(pady=20)

window.mainloop()