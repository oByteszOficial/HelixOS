#!/bin/bash

echo "🔧 Atualizando pacotes..."
apt-get update && apt-get upgrade -y

echo "📦 Resolving Dependencies..."
apt install -y nemo python3 python3-pyqt5 python3-tk gnome-terminal wget ppa snapd

echo "🔥 Removing Firefox"
apt remove -y firefox ubuntu-terminal-badge
apt autoremove -y

echo "🌐 Instaling Firefox Nightly..."
sudo add-apt-repository ppa:ubuntu-mozilla-daily/ppa
sudo apt-get update
sudo apt-get install firefox-trunk

echo "✅ Finished"
