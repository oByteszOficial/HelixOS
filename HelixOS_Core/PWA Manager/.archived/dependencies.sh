#!/bin/bash/
# This script installs the dependencies for the PWA Manager.
# After the error that I had...
# This thing don't work to me, 'cause this is only for Debian-based systems
# I'm using Arch Linux, so I need to install the dependencies using pacman... shit

sudo apt update && sudo apt upgrade -y
sudo apt install -y \
    python3 \
    python3-pip \
    python3-venv \
    python3-tk \
    python3-pil \
    python3-pil.imagetk \
    python3-requests \
    python3-html5lib \
    python3-beautifulsoup4 \
    python3-lxml \
    python3-cssselect \
    python3-html2text \
    python3-html5lib \
    python3-requests-html \
    python3-urllib3 #ChatGPT suggested this but I don't know if it's needed, and this is a bit big...

pip install tkhtmlview
pip install tk
pip install tkinter