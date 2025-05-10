import os
import tkinter as tk
from tkinter import ttk
from tkinter import *

password = "1234"

def login ():

    Lgin = tk.Tk()
    Lgin.title("Login - DNA Secret Folder")
    Lgin.geometry("300x100")
    Lgin.resizable(False, False)
    Lgin.configure(bg="#f4f7ff")
    
    TPass = tk.Label(Lgin, text="Password:", font=("Arial", 12))
    TPass.grid(row=0, column=0, padx=8, pady=15)

    Pass = tk.Text(Lgin, height=1, width=20, bg="#ffffff", fg="#000000", font=("Arial", 12))
    Pass.grid(row=0, column=1, padx=10, pady=15)

    def Verify():
        global PassValue
        PassValue = Pass.get("1.0", "end-1c")

    BtnLogn = tk.Button(Lgin, text="Login", command=Verify, bg="#96a9ff", fg="#e8f3ff", font=("Arial", 12), width=10)
    BtnLogn.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

    Lgin.mainloop()

def main():

    Root = tk.Tk()
    Root.title("DNA Secret Folder")
    Root.geometry("800x600")
    Root.resizable(True, True)

    # --Sidebar--

    Sidebar = tk.Frame(Root, width=200, bg="#f4f7ff")
    Sidebar.pack(side=tk.LEFT, fill=tk.Y)

    # -Sidebar content-

    Desk = ttk.Button(Sidebar, text="🗂 Desktop")
    Docs = ttk.Button(Sidebar, text="🗎 Documents")
    Music = ttk.Button(Sidebar, text="🎵 Music")
    Colors = ttk.Button(Sidebar, text="🎨 Colors")

    # --Folder Render--

    Content = tk.Frame(Root, bg="#ffffff")
    Content.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    # -Folder content-

    Root.mainloop()

def passCheck():
    if PassValue == password:
        print("Correct Password")
        main()
