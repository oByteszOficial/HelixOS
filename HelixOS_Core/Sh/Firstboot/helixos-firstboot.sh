#!/bin/bash

# Remove Calamares e arquivos relacionados
apt purge calamares -y
apt autoremove -y

# Remove o lançador da Área de Trabalho (caso tenha deixado um)
rm -f /home/*/Área\ de\ Trabalho/Install\ HelixOS.desktop

# Remove este serviço para não rodar de novo
rm -f /etc/xdg/autostart/helixos-firstboot.desktop

# (Opcional) mensagem para o usuário
notify-send "HelixOS" "Instalação concluída! Calamares removido com sucesso."

exit 0
