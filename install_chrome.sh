#!/bin/bash
echo "🔽 Scaricamento di Google Chrome su Render..."

# Creiamo una cartella nella home dell'utente, che ha più permessi
mkdir -p $HOME/chrome

# Scarichiamo la versione portatile di Google Chrome
wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -O $HOME/chrome/google-chrome.deb

echo "✅ Chrome scaricato! Ora lo estraiamo..."

# Estraiamo Chrome nella stessa cartella
dpkg -x $HOME/chrome/google-chrome.deb $HOME/chrome/
mv $HOME/chrome/opt/google/chrome $HOME/chrome/
rm -rf $HOME/chrome/opt

echo "✅ Google Chrome installato in $HOME/chrome/"


