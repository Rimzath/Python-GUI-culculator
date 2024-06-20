import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Rimzath's Calculator")
        self.geometry("400x600")
        self.configure(bg="#2E2E2E")

        self.expression = ""
        self.result_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        result_frame = tk.Frame(self, bg="#2E2E2E")
        result_frame.pack(expand=True, fill="both")

        result_label = tk.Label(result_frame, textvariable=self.result_var, font=("Arial", 24), anchor="e", bg="#1C1C1C", fg="#F7F7F7")
        result_label.pack(expand=True, fill="both", padx=10, pady=10)

        button_frame = tk.Frame(self, bg="#2E2E2E")
        button_frame.pack(expand=True, fill="both")

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C', '<-', 'CE'
        ]

        button_colors = {
            '/': "#FF9500", '*': "#FF9500", '-': "#FF9500", '+': "#FF9500", '=': "#FF9500",
            'C': "#FF3B30", '<-': "#FF3B30", 'CE': "#FF3B30"
        }

        row = 0
        col = 0

        for button in buttons:
            action = lambda x=button: self.on_button_click(x)
            color = button_colors.get(button, "#505050")
            b = tk.Button(button_frame, text=button, font=("Arial", 18), fg="#F7F7F7", bg=color, bd=0, command=action)
            b.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

            col += 1
            if col > 3:
                col = 0
                row += 1

        for i in range(4):
            button_frame.grid_columnconfigure(i, weight=1)
        for i in range((len(buttons) + 3) // 4):
            button_frame.grid_rowconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == "=":
            try:
                self.expression = str(eval(self.expression))
            except Exception as e:
                self.expression = "Error"
        elif char in ["C", "CE"]:
            self.expression = ""
        elif char == "<-":
            self.expression = self.expression[:-1]
        else:
            self.expression += str(char)
        
        self.result_var.set(self.expression)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
