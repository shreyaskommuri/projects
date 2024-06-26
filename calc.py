import tkinter as tk

root = tk.Tk()
root.title("Shreyas's Calculator")
root.resizable(0,0)

hello = tk.Entry(root, width=35, bg="light grey", fg="black", borderwidth=5, justify="right", font=("Arial", 12))
hello.grid(row=0, column=0, columnspan=3, padx=12, pady=12)

def buttonClick(number):
    temp = hello.get()
    hello.delete(0, tk.END) 
    hello.insert(0, temp + number)  
    
def  buttonClear():
    hello.delete(0, tk.END)
    
def buttonGet(oper):
    global firstNum, math
    firstNum = hello.get()
    math = oper
    hello.insert(tk.END, math)
    try:
        firstNum = float(firstNum)
    except ValueError:
        buttonClear()
        
def buttonEqual():
    inp = hello.get()
    secondNum = float(inp[inp.index(math) + 1:])
    hello.delete(0, tk.END)
    if math == "+":
        hello.insert(0, str(firstNum + secondNum))
    elif math == "-":
        hello.insert(0, str(firstNum - secondNum))
    elif math == "x":
        hello.insert(0, str(firstNum * secondNum))
    elif math == "/":
        try:
            hello.insert(0, str(firstNum / secondNum))
        except ZeroDivisionError:
            hello.insert(0, "Underfined")
            
button1 = tk.Button(root, text="1", padx=40, pady=10, command=lambda: buttonClick("1"), font=("Arial", 12))

button2 = tk.Button(root, text="2", padx=40, pady=10, command=lambda: buttonClick("2"), font=("Arial", 12))

button3 = tk.Button(root, text="3", padx=40, pady=10, command=lambda: buttonClick("3"), font=("Arial", 12))

button4 = tk.Button(root, text="4", padx=40, pady=10, command=lambda: buttonClick("4"), font=("Arial", 12))

button5 = tk.Button(root, text="5", padx=40, pady=10, command=lambda: buttonClick("5"), font=("Arial", 12))

button6 = tk.Button(root, text="6", padx=40, pady=10, command=lambda: buttonClick("6"), font=("Arial", 12))

button7 = tk.Button(root, text="7", padx=40, pady=10, command=lambda: buttonClick("7"), font=("Arial", 12))

button8 = tk.Button(root, text="8", padx=40, pady=10, command=lambda: buttonClick("8"), font=("Arial", 12))

button9 = tk.Button(root, text="9", padx=40, pady=10, command=lambda: buttonClick("9"), font=("Arial", 12))

button0 = tk.Button(root, text="0", padx=40, pady=10, command=lambda: buttonClick("0"), font=("Arial", 12))

buttondot = tk.Button(root, text=".", padx=40, pady=10, command=lambda: buttonClick("."), font=("Arial", 12))

buttonadd = tk.Button(root, text="+", padx=40, pady=10, command=lambda: buttonGet("+"), font=("Arial", 12))

buttonsub = tk.Button(root, text="-", padx=40, pady=10, command=lambda: buttonGet("-"), font=("Arial", 12))

buttonmultiply = tk.Button(root, text="*", padx=40, pady=10, command=lambda: buttonGet("x"), font=("Arial", 12))

buttondivide = tk.Button(root, text="/", padx=40, pady=10, command=lambda: buttonGet("/"), font=("Arial", 12))

buttonclear = tk.Button(root, text="C", padx=40, pady=10, command= buttonClear, font=("Arial", 12))

buttonequal = tk.Button(root, text="=", padx=40, pady=10, command= buttonEqual, font=("Arial", 12))

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
buttonadd.grid(row=3, column=3)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
buttonmultiply.grid(row=2, column=3)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
buttondivide.grid(row=1, column=3)

button0.grid(row=4, column=0)
buttondot.grid(row=4, column=1)
buttonequal.grid(row=4, column=2)
buttonsub.grid(row=4, column=3)

buttonclear.grid(row=0, column=3)

root.mainloop()