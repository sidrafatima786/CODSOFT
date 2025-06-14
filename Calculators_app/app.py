import tkinter as tk
from tkinter import ttk, messagebox

class SimpleCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        
        self.num1_var = tk.StringVar()
        self.num2_var = tk.StringVar()
        self.result_var = tk.StringVar(value="Ready to calculate!")
        
        self.create_widgets()
    
    def create_widgets(self):
        frame = ttk.Frame(self.root, padding=15)
        frame.grid()

        ttk.Label(frame, text="Number 1:").grid(row=0, column=0, sticky="w")
        ttk.Entry(frame, textvariable=self.num1_var, width=15).grid(row=0, column=1)

        ttk.Label(frame, text="Number 2:").grid(row=1, column=0, sticky="w")
        ttk.Entry(frame, textvariable=self.num2_var, width=15).grid(row=1, column=1)

        ttk.Label(frame, text="Operation:").grid(row=2, column=0, sticky="w")
        self.op_var = tk.StringVar(value="Add")
        ops = ["Add", "Subtract", "Multiply", "Divide"]
        op_menu = ttk.Combobox(frame, values=ops, textvariable=self.op_var, state="readonly")
        op_menu.grid(row=2, column=1)
        op_menu.current(0)

        ttk.Button(frame, text="Compute", command=self.compute).grid(row=3, column=0, columnspan=2, pady=10)

        ttk.Label(frame, textvariable=self.result_var, font=("Arial", 11, "bold")).grid(row=4, column=0, columnspan=2)

    def compute(self):
        try:
            x = float(self.num1_var.get())
            y = float(self.num2_var.get())
            op = self.op_var.get().lower()
            
            if op == "add":
                result = x + y
            elif op == "subtract":
                result = x - y
            elif op == "multiply":
                result = x * y
            elif op == "divide":
                if y == 0:
                    raise ZeroDivisionError
                result = x / y
            else:
                self.result_var.set("Select an operation.")
                return
            
            self.result_var.set(f"Result: {result}")
        except ZeroDivisionError:
            self.result_var.set("Error: Cannot divide by zero.")
            messagebox.showerror("Math Error", "Cannot divide by zero.")
        except ValueError:
            self.result_var.set("Error: Invalid input.")
            messagebox.showerror("Input Error", "Please enter valid numbers.")

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleCalculator(root)
    root.mainloop()