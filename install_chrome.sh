#!/bin/bash
echo "🔽 Installazione di Google Chrome su Render..."

# Aggiungiamo le fonti di Google Chrome
wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add -
sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'

# Aggiorniamo il sistema e installiamo Chrome
apt-get update && apt-get install -y google-chrome-stable

# Verifichiamo che Chrome sia installato correttamente
if command -v google-chrome; then
    echo "✅ Google Chrome installato con successo!"
else
    echo "❌ Errore: Chrome non è stato installato correttamente!"
    exit 1
fi

