import math
import plistlib
from textwrap import fill
from tkinter import *
from tkinter import font
import numpy as np
import matplotlib.pyplot as plt

from funciones_operaciones import sen
root = Tk()
#for font  in font.families():
#    print(font)
#root.title("Prueba Frames")
#root.resizable(1,1)
#root.iconbitmap('icons8-calculator-32.ico')
#root.config(bg='white')
#root.config(relief=RAISED)
#root.config(bd=10)

#frame = Frame(root, width=480, height=320)
#frame.pack()
#frame.config(bg = 'gray2')
#frame.config(cursor='')
#frame.config(relief="sunken")
#frame.config(bd=15)
#frame.pack(expand=1)

#root.mainloop()

x1 = np.linspace(-10,10,200)
y1 = np.sin(x1)

x2 = np.linspace(0, 10, 500)
y2 = np.cos(x2)

# Gráfico de líneas
fig, ax = plt.subplots()
ax.plot(x1, y1,)
ax.plot(x2, y2,)
#ax.legend()

plt.show()