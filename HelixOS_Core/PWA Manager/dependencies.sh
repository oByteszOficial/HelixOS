#!/bin/bash/
# This script installs the dependencies for the PWA Manager.
# PWA Manager: Electron with another name (cause i'm lazy to create my own PWA runner)
# Why am I using Electron? This is a good question, and it's cause Electron is the best way that I know to run a PWA
# But just in linux enviroments, also this shell script works only in Debian-based systems
# And the HelixOS is based in Ubuntu, so it's ok
# ok... I REALLY need to stop talking with a CODE and start coding
# search for a psycologist
# and teach VS code to spell "psychologist"

# Code by Byt3z :3

apt-get update && apt-get upgrade -y
apt-get install python3-pip python3-dev libssl-dev libffi-dev build-essential -y
apt-get install electron -y
apt-get install python3-tk -y