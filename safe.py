import tkinter as tk
import subprocess
from tkinter import PhotoImage
root = tk.Tk()
root.geometry("1920x1080")
root.title("Execute Program")

headingfont=("ariel",70)
root.configure(bg="green")

label = tk.Label(root, text="Safe",font=headingfont,bg="green",fg="white")
label.pack(side="top", pady=300)

root.mainloop()