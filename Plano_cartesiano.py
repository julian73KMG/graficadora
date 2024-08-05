from tkinter import Frame
from matplotlib.dates import FR
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


def plot_graph(entrada,root,x,y,y1,y2):
    
    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.plot(x, y, linestyle='-')
    #ax.set_ylim(bottom = -10,top = 10 )
    #ax.set_xlim(left = -10,right = 10 )
    ax.set_title('Plano Cartesiano')
    ax.set_xlabel('Eje X')
    ax.set_ylabel('Eje Y')
    ax.grid(True)
    ax.axhline(0, color='gray', linewidth=1.2)
    ax.axvline(0, color='gray', linewidth=1.2)

    # Integrar el gráfico en la interfaz de Tkinter

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().place(x=325, y=2, width=570, height=450)
    canvas.get_tk_widget().configure(takefocus=0)
    entrada.focus_set()