import os as host
import tkinter as tk
from tkinter import filedialog, messagebox
import tkinter.ttk as ttk

def Main():
    # Create the main window
    root = tk.Tk()
    
    root.title("DNA Explorer")

    root.geometry("800x600")
    root.resizable(True, True)

    # --Sidebar--

    sidebar = tk.Frame(root, width=200, bg="lightgray")
    sidebar.pack(side=tk.LEFT, fill=tk.Y)

    # -Content-

    # --EndSidebar--

    # --Main--

    main_frame = tk.Frame(root, bg="white")
    main_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # -Content-

    # --EndMain--
    root.mainloop()

Main()