from tkinter import *
import keyboard
import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

canvas_width = 500
canvas_height = 500

pts = []
def paint(event):
    if keyboard.is_pressed('q'):
        master.destroy()
        plot(pts)
    python_green = "#476042"
    x1, y1 = ( event.x - 1 ), ( event.y - 1 )
    x2, y2 = ( event.x + 1 ), ( event.y + 1 )
    w.create_oval( x1, y1, x2, y2, fill = python_green )
    pts.append([event.x, event.y])

def plot(pts):
    print(str(pts))
    pad = 3
    pts = np.pad(pts, [(pad,pad), (0,0)], mode='wrap')
    x, y = pts.T
    i = np.arange(0, len(pts))

    interp_i = np.linspace(pad, i.max() - pad + 1, 5 * (i.size - 2*pad))

    xi = interp1d(i, x, kind='cubic')(interp_i)
    yi = interp1d(i, y, kind='cubic')(interp_i)

    fig, ax = plt.subplots()
    ax.plot(xi, yi)
    ax.plot(x, y, 'ko')
    plt.show()


master = Tk()
master.title( "test - getting down the points" )
w = Canvas(master,
           width=canvas_width,
           height=canvas_height)
w.pack(expand = YES, fill = BOTH)
w.bind( "<B1-Motion>", paint)

mainloop()
