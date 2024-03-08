import tkinter as tk
import time

class DigitalClock:
    def __init__(self, master):
        self.master = master
        self.velocity = 1000  # milliseconds, equivalent to 1 second
        self.hour = (int)(time.strftime("%H"))
        self.minute = (int)(time.strftime("%M"))
        self.second = (int)(time.strftime("%S"))
        self.text = f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"
        self.initialize_ui()

    def update_time(self):
        self.second += 1
        if self.second >= 60:
            self.second = 0
            self.minute += 1
            if self.minute >= 60:
                self.minute = 0
                self.hour += 1
                if self.hour >= 24:
                    self.hour = 0
        self.text = f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"


    def initialize_ui(self):
        self.master.title('Relógio Digital')
        self.master.geometry('400x300')

        # Always keep the components centered
        self.master.columnconfigure(0, weight=1, minsize=100)
        self.master.rowconfigure([0, 1], weight=1, minsize=100)

        # Create a button
        self.botao = tk.Button(self.master, text='Acelerar o tempo', command=self.update_velocity)
        print(self.velocity)
        self.botao.grid(row=1, column=0)

        self.hora = tk.Label(self.master, text="", font='Arial 50 bold')
        self.hora.grid(row=0, column=0)
        self.update_time_text()

    def update_velocity(self):
        self.velocity = self.velocity // 2  # Increase speed
        self.master.after_cancel(self.update_time_text)
        
    def update_time_text(self):
        self.hora.config(text=(self.text))
        self.update_time() 
        self.master.after(self.velocity, self.update_time_text)  # Schedule next update
        

if __name__ == '__main__':
    root = tk.Tk()
    clock = DigitalClock(root)
    root.mainloop()