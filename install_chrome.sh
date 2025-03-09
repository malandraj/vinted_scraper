#!/bin/bash
echo "🔽 Scaricamento di Google Chrome su Render..."

# Creiamo una cartella temporanea per Chrome
mkdir -p $HOME/chrome

# Scarichiamo Chrome con verifica
wget -O $HOME/chrome/google-chrome.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

# Controlliamo se il download è andato a buon fine
if [ ! -f "$HOME/chrome/google-chrome.deb" ]; then
    echo "❌ Errore: Il download di Chrome è fallito!"
    exit 1
fi

echo "✅ Chrome scaricato! Ora lo estraiamo..."

# Estraiamo Chrome in una cartella accessibile
dpkg -x $HOME/chrome/google-chrome.deb $HOME/chrome/ || echo "❌ Errore: estrazione fallita"
mv $HOME/chrome/opt/google/chrome $HOME/chrome/ || echo "❌ Errore: spostamento fallito"
rm -rf $HOME/chrome/opt

# Controlliamo se Chrome è stato installato
if [ ! -f "$HOME/chrome/chrome" ]; then
    echo "❌ Errore: Chrome non è stato installato correttamente!"
    exit 1
fi

echo "✅ Google Chrome installato in $HOME/chrome/"


