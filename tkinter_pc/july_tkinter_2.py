import tkinter as tk

root = tk.Tk()
# root.grid()
root.geometry("500x500")
canvas = tk.Canvas(root, bg = "#FFEEAA", width = '500', height = '500')
canvas.grid(row = 6, column = 6, rowspan = 1 )
canvas.grid_configure()

root.mainloop()