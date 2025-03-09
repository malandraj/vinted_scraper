#!/bin/bash
echo "🔽 Installazione di Playwright su Render..."

# Installa Playwright
pip install playwright

# Installa i browser per Playwright
python -m playwright install

echo "✅ Playwright installato con successo!"

