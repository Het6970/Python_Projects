import tkinter as tk

root = tk.Tk()
root.title("Royal")
root.geometry("500x500")
root.config(bg="lightblue")

label=tk.Label(root,text="Hello!,\nEnter Your First Name",font=("times",20),bg="yellow").pack(pady=20)
name_box = tk.Entry(root,width=60)
name_box.pack(pady=5)

def print_name():
    first_name=name_box.get()
    print("Your Name is : ",first_name)
    tk.Label(root,bg="Yellow",text=f"Welcome , {first_name} on Tkinter :) ").pack(pady=5)
Submit = tk.Button(root,text="Submit",command=print_name).pack(pady=10)
root.mainloop()
