#!/bin/bash
echo "🔽 Installazione di Chromium su Render..."

# Installiamo Chromium, che è più leggero di Chrome
apt-get update && apt-get install -y chromium-browser

# Controlliamo se Chromium è stato installato
if command -v chromium-browser; then
    echo "✅ Chromium installato con successo!"
else
    echo "❌ Errore: Chromium non è stato installato correttamente!"
    exit 1
fi


