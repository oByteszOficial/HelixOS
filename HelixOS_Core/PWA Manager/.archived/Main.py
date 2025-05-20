# HelixOS PWA Manager
# (this is an another name for "Navigator that runs PWA without have a big topbar")
# I don't know what this thing have to do, and how I have to call it
# I'm good with python, but I don't know how to made a "navigator" with it
# I'm trying to do this 'cause the newest version of HelixOS File Explorer (DNA Explorer) is a PWA
# And the navigator (currently Firefox Nightly) has a REALLY big topbar
# So I want to make a navigator that runs PWA without have a big topbar, like a "webview"
# Or like Google does this with ChromeOS, an operating system that is based on Linux but runs PWAs
# I want to do something similar to this in HelixOS

# I think I need a psychologist, I'm talking to myself inside a python code
# I DEFINITELY need a psychologist
# So here is the code

# Code by Byt3z :3
import sys
import os
import tkinter as tk
#from tkhtmlview import HTMLLabel # ChatGPT suggested this, but I don't know what this is

# I'm thinking that I will use ChatGPT to do this, so...

# Code by ChatGPT :3

if len(sys.argv) < 2:
    print("Uso: python PWAmanager.py arquivo.html")
    sys.exit(1)

arquivo_html = sys.argv[1]

if not os.path.exists(arquivo_html):
    print(f"Arquivo '{arquivo_html}' não encontrado.")
    sys.exit(1)

with open(arquivo_html, 'r', encoding='utf-8') as f:
    html_content = f.read()

root = tk.Tk()
root.title("HelixOS PWA Viewer")
root.geometry("800x600")

#html_label = HTMLLabel(root, html=html_content)
#html_label.pack(fill="both", expand=True)

root.mainloop()


# ChatGPT goes wrong...
# Running the code with the command: python Main.py Test.html
# The terminal returns "Traceback (most recent call last):
#  File "/run/media/byt3z_/HelixProject/HelixOS/HelixOS_Core/PWA Manager/Main.py", line 16, in <module>
#    import tkinter as tk
#  File "/usr/lib/python3.13/tkinter/__init__.py", line 38, in <module>
#    import _tkinter # If this fails your Python may not be configured for Tk
#    ^^^^^^^^^^^^^^^
#ImportError: libtk8.6.so: cannot open shared object file: No such file or directory"

# I don't know what this means, but I think this is not good

# 15 minutes later...
# That was a problem with my OS, I just needed to install the tk package, now the code is running
# I will create a dependencies.sh that installs this to avoid problems within my operating system