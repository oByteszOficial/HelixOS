#!/bin/bash

msg="HelixOS commit"

if [ "$1" != "" ]; then
  msg="$1"
fi

echo "🔄 Fazendo commit com a mensagem: $msg"

git add .
git commit -m "$msg"
git push origin main
