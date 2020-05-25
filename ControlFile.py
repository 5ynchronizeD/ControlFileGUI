import tkinter as tk
from tkinter import filedialog, Text
import os

#The window itself
root = tk.Tk()

#Create Canvas
canvas = tk.Canvas(root, height=200, width=700, bg="#263D42")
canvas.pack() #Attach canvas to the root

frame = tk.Frame(root, bg="white")
frame.place(relheight= 0.8, relwidth = 0.8, relx=0.1, rely=0.1)



root.mainloop()