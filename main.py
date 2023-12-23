import tkinter as tk

def update_position():
    x = root.winfo_x()
    y = root.winfo_y()
    position_label.config(text=f"X-Position: {x}, Y-Position: {y}")
    root.after(100, update_position)

root = tk.Tk()
root.title("Fensterposition")
root.geometry("220x25")

position_label = tk.Label(root, text="")
position_label.pack()

update_position()

root.mainloop()