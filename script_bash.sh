#!/bin/bash

while true; do
  echo "Ora și data curentă: $(date)"
  echo "Sistem de operare: $(uname -o)"
  echo "Informații despre procesor:"
  lscpu | grep "Model name" | sed 's/Model name: *//'
  echo "Memorie RAM totală și disponibilă:"
  free -h | grep -E "Mem|Total|available"
  echo "Spațiu pe disk:"
  df -h / | grep -E "Filesystem|/"
  echo "---------------------------------------"
  sleep 5  # modifică 5 cu numărul de secunde dorit
done

