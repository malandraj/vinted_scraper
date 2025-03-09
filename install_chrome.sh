#!/bin/bash
echo "🔽 Scaricamento di Google Chrome portatile per Render..."

mkdir -p /opt/chrome
wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -O /opt/chrome/google-chrome.deb

echo "✅ Chrome scaricato! Ora lo estraiamo..."

dpkg -x /opt/chrome/google-chrome.deb /opt/chrome/
mv /opt/chrome/opt/google/chrome /opt/chrome/
rm -rf /opt/chrome/opt

echo "✅ Google Chrome portatile installato con successo!"


