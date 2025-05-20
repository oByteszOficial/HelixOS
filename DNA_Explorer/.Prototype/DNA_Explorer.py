#Code by Byt3z :3

import os as host
import tkinter as tk
from tkinter import filedialog, messagebox
import tkinter.ttk as ttk

class Main():
    # Create the main window
    root = tk.Tk()
    
    root.title("DNA Explorer")

    root.geometry("800x600")
    root.resizable(True, True)

    # --Sidebar--

    sidebar = tk.Frame(root, width=200, bg="lightgray")
    sidebar.pack(side=tk.LEFT, fill=tk.Y)

    # -Content-

    txt1 = tk.Label(sidebar, text="Home")

    txt1.grid(row=1, column=0, padx=15, pady=15)

    # --EndSidebar--

    # --Main--

    main = tk.Frame(root, bg="white")
    main.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # -Content-

    # --EndMain--
    root.mainloop()

Main()