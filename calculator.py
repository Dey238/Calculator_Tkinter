import tkinter as tk
from tkinter import messagebox

class calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("300x350")
        self.resizable(0,0)
        self.title("Calculator")
        self.iconbitmap("calculator.ico")
        self.expresion = ""
        self.text_entry = tk.StringVar()
        self._components_creations()

    def _components_creations(self):
        entry_frame = tk.Frame(self, width=400, height=50, bg="black")
        entry_frame.pack(side=tk.TOP, fill="x")

        entry = tk.Entry(entry_frame, font=("arial", 18, "bold"),
                         textvariable=self.text_entry, justify=tk.RIGHT)
        entry.pack(fill="x", ipady=10)

        buttons_frame = tk.Frame(self, width=400, height=450, bg="black")
        buttons_frame.pack(expand=True, fill="both")

        for i in range(4):
            buttons_frame.columnconfigure(i, weight=1)
        for i in range(5):
            buttons_frame.rowconfigure(i, weight=1)

        clean_button= tk.Button(buttons_frame, text="C", bd=0, bg="#6D94C5",
                  command=self._clean).grid(row=0, column=0, columnspan=3, padx=1, pady=1, sticky="nsew")
        divide_button= tk.Button(buttons_frame, text="/", bd=0, bg="#6D94C5",
                  command=lambda: self._event_click("/")).grid(row=0, column=3, padx=1, pady=1, sticky="nsew")

        seven_button= tk.Button(buttons_frame, text="7", bd=0, bg="#DCDCDC",
                  command=lambda: self._event_click(7)).grid(row=1, column=0, padx=1, pady=1, sticky="nsew")
        eight_button= tk.Button(buttons_frame, text="8", bd=0, bg="#DCDCDC",
                  command=lambda: self._event_click(8)).grid(row=1, column=1, padx=1, pady=1, sticky="nsew")
        nine_button= tk.Button(buttons_frame, text="9", bd=0, bg="#DCDCDC",
                  command=lambda: self._event_click(9)).grid(row=1, column=2, padx=1, pady=1, sticky="nsew")
        multiply_button= tk.Button(buttons_frame, text="*", bd=0, bg="#6D94C5",
                  command=lambda: self._event_click("*")).grid(row=1, column=3, padx=1, pady=1, sticky="nsew")

        four_button= tk.Button(buttons_frame, text="4", bd=0, bg="#DCDCDC",
                  command=lambda: self._event_click(4)).grid(row=2, column=0, padx=1, pady=1, sticky="nsew")
        five_button= tk.Button(buttons_frame, text="5", bd=0, bg="#DCDCDC",
                  command=lambda: self._event_click(5)).grid(row=2, column=1, padx=1, pady=1, sticky="nsew")
        six_button= tk.Button(buttons_frame, text="6", bd=0, bg="#DCDCDC",
                  command=lambda: self._event_click(6)).grid(row=2, column=2, padx=1, pady=1, sticky="nsew")
        rest_button= tk.Button(buttons_frame, text="-", bd=0, bg="#6D94C5",
                  command=lambda: self._event_click("-")).grid(row=2, column=3, padx=1, pady=1, sticky="nsew")

        one_button= tk.Button(buttons_frame, text="1", bd=0, bg="#DCDCDC",
                  command=lambda: self._event_click(1)).grid(row=3, column=0, padx=1, pady=1, sticky="nsew")
        two_button= tk.Button(buttons_frame, text="2", bd=0, bg="#DCDCDC",
                  command=lambda: self._event_click(2)).grid(row=3, column=1, padx=1, pady=1, sticky="nsew")
        three_button= tk.Button(buttons_frame, text="3", bd=0, bg="#DCDCDC",
                  command=lambda: self._event_click(3)).grid(row=3, column=2, padx=1, pady=1, sticky="nsew")
        sum_button= tk.Button(buttons_frame, text="+", bd=0, bg="#6D94C5",
                  command=lambda: self._event_click("+")).grid(row=3, column=3, padx=1, pady=1, sticky="nsew")

        cero_button= tk.Button(buttons_frame, text="0", bd=0, bg="#DCDCDC",
                  command=lambda: self._event_click(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=1, sticky="nsew")
        point_button= tk.Button(buttons_frame, text=".", bd=0, bg="#DCDCDC",
                  command=lambda: self._event_click(".")).grid(row=4, column=2, padx=1, pady=1, sticky="nsew")
        iqual_button= tk.Button(buttons_frame, text="=", bd=0, bg="#6D94C5",
                  command=self._operation).grid(row=4, column=3, padx=1, pady=1, sticky="nsew")

    def _operation(self):
        try:
            if self.expresion:
                result = str(eval(self.expresion))
                self.text_entry.set(result)
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")
            self.text_entry.set("")
        finally:
            self.expresion = "" 

    def _clean(self):
        self.expresion = ""
        self.text_entry.set(self.expresion)
        
    def _event_click(self, element):
        self.expresion = f"{self.expresion}{element}"
        self.text_entry.set(self.expresion)


if __name__ == "__main__":
    calculator = calculator()
    calculator.mainloop()
