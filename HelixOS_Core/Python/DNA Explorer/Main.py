import os
import tkinter as tk
from tkinter import ttk
from tkinter import *

def main():

    Root = tk.Tk()
    Root.title("DNA Explorer")
    Root.geometry("800x600")
    Root.resizable(True, True)

    # --Sidebar--

    Sidebar = tk.Frame(Root, width=200, bg="#f4f7ff")
    Sidebar.pack(side=tk.LEFT, fill=tk.Y)

    # -Sidebar content-

    SLibs = tk.Label(Sidebar, text="📂 Libraries")
    Desk = ttk.Button(Sidebar, text="🗂 Desktop")
    Docs = ttk.Button(Sidebar, text="🗎 Documents")
    Music = ttk.Button(Sidebar, text="🎵 Music")
    SColors = tk.Label(Sidebar, text="🎨 Colors")

    SLibs.grid(row=0, column=0, padx=10, pady=15, sticky="ew")
    Desk.grid(row=1, column=0, padx=10, pady=5, sticky="ew")
    Docs.grid(row=2, column=0, padx=10, pady=5, sticky="ew")
    Music.grid(row=3, column=0, padx=10, pady=5, sticky="ew")
    SColors.grid(row=4, column=0, padx=10, pady=25, sticky="ew")

    # -Color Folders-

    Colors = ttk.Button(Sidebar, text="🎨 Undefined")
    white = ttk.Button(Sidebar, text="⚪ White")
    Red = ttk.Button(Sidebar, text="🔴 Red")
    Purple = ttk.Button(Sidebar, text="🟣 Purple")
    Blue = ttk.Button(Sidebar, text="🔵 Blue")
    Green = ttk.Button(Sidebar, text="🟢 Green")
    Black = ttk.Button(Sidebar, text="⚫ Black")

    Colors.grid(row=5, column=0, padx=10, pady=0, sticky="ew")
    white.grid(row=6, column=0, padx=10, pady=5, sticky="ew")
    Red.grid(row=7, column=0, padx=10, pady=5, sticky="ew")
    Purple.grid(row=8, column=0, padx=10, pady=5, sticky="ew")
    Blue.grid(row=9, column=0, padx=10, pady=5, sticky="ew")
    Green.grid(row=10, column=0, padx=10, pady=5, sticky="ew")
    Black.grid(row=11, column=0, padx=10, pady=5, sticky="ew")


    # --Folder Render--

    Content = tk.Frame(Root, bg="#ffffff")
    Content.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    # -Folder content-

    Root.mainloop()