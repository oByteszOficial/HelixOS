#!/bin/bash

sudo su
apt-get update && apt-get upgrade -y
apt-get install python3-pip python3-dev libssl-dev libffi-dev build-essential -y
apt-get install nemo