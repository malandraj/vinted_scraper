#!/bin/bash
echo "🔽 Scaricamento di Chromium portatile su Render..."

# Creiamo una cartella per Chromium
mkdir -p $HOME/chromium

# Scarichiamo Chromium precompilato
wget -O $HOME/chromium/chrome-linux.zip https://download-chromium.appspot.com/dl/Linux_x64?type=snapshots

# Controlliamo se il download è andato a buon fine
if [ ! -f "$HOME/chromium/chrome-linux.zip" ]; then
    echo "❌ Errore: Il download di Chromium è fallito!"
    exit 1
fi

echo "✅ Chromium scaricato! Ora lo estraiamo..."

# Estraiamo Chromium nella stessa cartella
unzip $HOME/chromium/chrome-linux.zip -d $HOME/chromium/ || echo "❌ Errore: estrazione fallita"

# Controlliamo se Chromium è stato installato
if [ ! -f "$HOME/chromium/chrome-linux/chrome" ]; then
    echo "❌ Errore: Chromium non è stato installato correttamente!"
    exit 1
fi

echo "✅ Chromium installato in $HOME/chromium/chrome-linux/"

# Scarichiamo la versione corretta di ChromeDriver per Chromium 136
echo "🔽 Scaricamento di ChromeDriver compatibile..."
wget -O $HOME/chromedriver.zip https://storage.googleapis.com/chrome-for-testing-public/136.0.7059.0/linux64/chromedriver-linux64.zip

# Estraiamo ChromeDriver
unzip $HOME/chromedriver.zip -d $HOME/chromium/
mv $HOME/chromium/chromedriver-linux64/chromedriver $HOME/chromium/chromedriver

# Controlliamo se ChromeDriver è stato installato
if [ ! -f "$HOME/chromium/chromedriver" ]; then
    echo "❌ Errore: ChromeDriver non è stato installato correttamente!"
    exit 1
fi

echo "✅ ChromeDriver installato in $HOME/chromium/chromedriver"


