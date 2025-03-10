#!/bin/bash
echo "🔽 Installazione di Playwright su Render..."

# Installa Playwright
pip install --upgrade pip
pip install playwright

# Installa Google Chrome per Playwright
python -m playwright install --with-deps chromium

echo "✅ Playwright installato con successo!"
