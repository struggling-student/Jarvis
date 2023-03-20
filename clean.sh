#!/bin/bash

# Eseguire chmod +x clean.sh per rendere lo script eseguibile.

# Eliminiare la directory Data con le domande degli esami
rm -rf ./Data
# Eliminare il file output.txt
rm -f ./output.txt
# Eliminare i file risposta_{}.png
rm -f ./risposta*
# Eliminare il pycache
rm -rf ./scarica/__pycache__   
rm -rf ./cerca/__pycache__   