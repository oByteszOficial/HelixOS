import tkinter as tk
from tkinter import ttk
from tkinter import *

def open_dir(path):
    print(f"Abrindo: {path}")  # Substitua pela lógica real

# --- Configuração da Janela ---
root = tk.Tk()
root.title("DNA Explorer")
root.grid("800x600")

# --- Sidebar ---
sidebar = tk.Frame(root, bg="#2F3542", width=200)
sidebar.pack(side="left", fill="y")

# Botões (alinhados verticalmente)
btndesk = ttk.Button(sidebar, text="🖥️ Desktop", command=lambda: open_dir("~/Desktop"))

btndocs = ttk.Button(sidebar, text="📂 Documents", command=lambda: open_dir("~/Documents"))
btndocs.pack(pady=5, fill="x")

btnimg = ttk.Button(sidebar, text="🖼️ Pictures", command=lambda: open_dir("~/Pictures"))
btnimg.pack(pady=5, fill="x")

btnmusic = ttk.Button(sidebar, text="🎵 Music", command=lambda: open_dir("~/Music"))
btnmusic.pack(pady=5, fill="x")

# --- Área de Conteúdo ---
content = tk.Frame(root, bg="white")
content.pack(side="right", fill="both", expand=True)

root.mainloop()