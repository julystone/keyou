import tkinter as tk

root = tk.Tk()
root.title("Gobang")
X_scale = 800
Y_scale = 800
root.geometry("{}x{}".format(X_scale, Y_scale))
X_begin = 0
X_end = 700
Y_begin = 0
Y_end = 700
grid_scale = (X_end - X_begin) / 14
X_Pianyi = (X_scale - X_end) / 2
Y_Pianyi = (Y_scale - Y_end) / 2
canvas = tk.Canvas(root, bg="#CDAA7D", width=X_scale, height=Y_scale)
canvas.grid(row=0, column=0, rowspan=6)
canvas.grid_configure()
for i in range(15):
    canvas.create_line(X_begin + X_Pianyi, (grid_scale * i + Y_begin) + Y_Pianyi, X_end + X_Pianyi,
                       (grid_scale * i + Y_begin) + Y_Pianyi)
    canvas.create_line((grid_scale * i + X_begin) + X_Pianyi, Y_begin + Y_Pianyi, (grid_scale * i + X_begin) + X_Pianyi,
                       Y_end + Y_Pianyi)

root.mainloop()
