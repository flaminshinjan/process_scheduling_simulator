# File: main.py
import tkinter as tk
from gui.interface import SchedulingSimulator

def main():
    root = tk.Tk()
    app = SchedulingSimulator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
