#!/bin/bash
echo "🔽 Scaricamento di Chromium portatile su Render..."

# Creiamo una cartella nella home dell'utente per Chromium
mkdir -p $HOME/chromium

# Scarichiamo Chromium portatile
wget -O $HOME/chromium/chromium.tar.xz https://download-chromium.appspot.com/dl/Linux_x64?type=snapshots

# Controlliamo se il download è andato a buon fine
if [ ! -f "$HOME/chromium/chromium.tar.xz" ]; then
    echo "❌ Errore: Il download di Chromium è fallito!"
    exit 1
fi

echo "✅ Chromium scaricato! Ora lo estraiamo..."

# Estraiamo Chromium
tar -xf $HOME/chromium/chromium.tar.xz -C $HOME/chromium/ || echo "❌ Errore: estrazione fallita"

# Controlliamo se Chromium è stato installato
if [ ! -f "$HOME/chromium/chrome" ]; then
    echo "❌ Errore: Chromium non è stato installato correttamente!"
    exit 1
fi

echo "✅ Chromium installato in $HOME/chromium/"


