#!/bin/bash
echo "🔽 Installazione di Google Chrome su Render..."

# Creiamo una cartella temporanea per Chrome
mkdir -p $HOME/chrome

# Scarichiamo Chrome stabile
wget -O $HOME/chrome/google-chrome.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

# Controlliamo se il download è andato a buon fine
if [ ! -f "$HOME/chrome/google-chrome.deb" ]; then
    echo "❌ Errore: Il download di Google Chrome è fallito!"
    exit 1
fi

echo "✅ Chrome scaricato! Ora lo estraiamo..."

# Estraiamo Chrome nella stessa cartella
dpkg -x $HOME/chrome/google-chrome.deb $HOME/chrome/

# Verifica se Chrome è stato installato
if [ ! -f "$HOME/chrome/opt/google/chrome/chrome" ]; then
    echo "❌ Errore: Google Chrome non è stato installato correttamente!"
    exit 1
fi

echo "✅ Google Chrome installato in $HOME/chrome/opt/google/chrome/"

