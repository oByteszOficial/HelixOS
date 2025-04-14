#!/bin/bash

echo "🔧 Atualizando pacotes..."
apt update && apt upgrade -y

echo "📦 Instalando pacotes necessários..."
apt install -y nemo python3 python3-pyqt5 python3-tk gnome-terminal wget ppa snapd

echo "🔥 Removendo o Firefox padrão e terminal do Ubuntu..."
apt remove -y firefox ubuntu-terminal-badge
apt autoremove -y

echo "🌐 Instalando Firefox Nightly..."
sudo add-apt-repository ppa:ubuntu-mozilla-daily/ppa
sudo apt-get update
sudo apt-get install firefox-trunk

echo "📂 Definindo Nemo como gerenciador de arquivos padrão..."
xdg-mime default nemo.desktop inode/directory application/x-gnome-saved-search
gio mime inode/directory nemo.desktop

echo "🎯 Substituindo atalho do Nautilus pelo do Nemo..."
cp /usr/share/applications/nemo.desktop /usr/share/applications/nautilus.desktop
sed -i 's/^Name=.*/Name=Files/' /usr/share/applications/nautilus.desktop
sed -i 's/^Exec=.*/Exec=nemo %U/' /usr/share/applications/nautilus.desktop
sed -i 's/^Icon=.*/Icon=folder/' /usr/share/applications/nautilus.desktop

echo "✅ Finalizado com sucesso! Sistema pronto com Nemo, Firefox Nightly e Python pronto para desenvolvimento."
