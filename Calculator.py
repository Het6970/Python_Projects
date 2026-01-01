import  tkinter as tk 
from tkinter import ttk
 
root =tk.Tk()
root.title("CALCULATOR")
root.geometry("500x600")
root.config(bg="lightgrey")

# input  1 : 
tk.Label(root,text="Enter the first number: ",font=("Courier New",15),bg="beige").pack(pady=1)
a_box =tk.Entry(root,width=30)
a_box.pack(pady=5)

#input  2 : 
tk.Label(root,text="Enter the second number: ",font=("Courier New",15),bg="pink").pack()
b_box =tk.Entry(root,width=30)
b_box.pack(pady=10)

# list  operation  list : 
operation = [
    "1. Addition",
    "2. Subtraction",
    "3. Multiplication",
    "4. Division",
    "5. Modulus",
    "6. Floor division"
    
]

tk.Label(root,text="Select any operation you want from below ",font=("Segoe UI",12),bg="lightgrey").pack(pady=8)
op_box =ttk.Combobox(root,values=operation,width=50)
op_box.current(0)   # index number  : add index =0 sub 1 
op_box.pack(pady=15)

result_label = tk.Label(root,text="you can see result here ",font=("Segoe UI",10))
result_label.pack(pady=10)

# match  operation  :
def calculator():
    a= int(a_box.get())
    b= int(b_box.get())
    
    choice = op_box.current() +1 
    match choice:
        case 1 :
            result =a+b
        case 2 :
            result =a-b
        case 3 :
            result =a*b
        case 4 :
            result =a/b
        case 5 :
            result =a%b
        case 6 :
            result =a//b
        case _:
            result ="invalid operation"
    result_label.config(text=result)

def Reset():
    a_box.delete(0,"end")
    b_box.delete(0,"end")
    op_box.current(0)
    result_label.config(text="Reset Done !")
    return

    
tk.Button(root,text="Calculate",font=("Arial",10),command=calculator).pack(pady=10)
tk.Button(root,text="Reset",font=("Arial",10),command=Reset).pack(pady=4)
root.mainloop()
