import tkinter as tk
from tkinter import font


class SimpleCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        # Display
        self.display_var = tk.StringVar()
        self.display_var.set("0")

        display_font = font.Font(family="Arial", size=20, weight="bold")
        self.display = tk.Entry(
            root,
            textvar=self.display_var,
            font=display_font,
            borderwidth=2,
            relief="solid",
            justify="right",
            state="readonly",
        )
        self.display.pack(fill="both", padx=10, pady=20, ipady=10)

        # Buttons layout
        buttons_frame = tk.Frame(root)
        buttons_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Button layout
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"],
            ["C", "DEL"],
        ]

        button_font = font.Font(family="Arial", size=16, weight="bold")

        for row_index, row in enumerate(buttons):
            row_frame = tk.Frame(buttons_frame)
            row_frame.pack(fill="both", expand=True)

            for col_index, button_text in enumerate(row):
                btn = tk.Button(
                    row_frame,
                    text=button_text,
                    font=button_font,
                    command=lambda text=button_text: self.on_button_click(text),
                )
                btn.pack(side="left", fill="both", expand=True, padx=2, pady=2)

                if button_text in ["/", "*", "-", "+"]:
                    btn.config(bg="#FF9500", fg="white")
                elif button_text == "=":
                    btn.config(bg="#4CAF50", fg="white")
                elif button_text in ["C", "DEL"]:
                    btn.config(bg="#f44336", fg="white")
                else:
                    btn.config(bg="#e0e0e0", fg="black")

    def on_button_click(self, char):
        current_display = self.display_var.get()

        if char == "C":
            self.display_var.set("0")

        elif char == "DEL":
            if len(current_display) > 1:
                self.display_var.set(current_display[:-1])
            else:
                self.display_var.set("0")

        elif char == "=":
            try:
                result = eval(current_display)
                self.display_var.set(str(result))
            except Exception as e:
                self.display_var.set("Error")

        else:
            if current_display == "0":
                if char == ".":
                    self.display_var.set(current_display + char)
                elif char not in ["+", "-", "*", "/"]:
                    self.display_var.set(char)
                else:
                    self.display_var.set(current_display + char)
            else:
                self.display_var.set(current_display + char)


def main():
    root = tk.Tk()
    calculator = SimpleCalculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()
