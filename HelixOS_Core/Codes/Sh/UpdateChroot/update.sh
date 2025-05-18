#!/bin/bash

cd ~/.HelixDev
git clone https://github.com/oByteszOficial/HelixOS/

cd HelixOS
cd Bootanim

rm -rf /usr/share/plymouth/themes/spinner/

mv Helix /usr/share/plymouth/themes/spinner

cd ~/.HelixDev/HelixOS/HelixOS_Core/Sh
cp Firstboot /home/