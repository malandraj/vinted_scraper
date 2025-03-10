#!/bin/bash
echo "🔽 Installazione di Playwright su Render..."

# Assicuriamoci di avere l'ultima versione di Playwright
pip install --upgrade pip
pip install --upgrade playwright

# Verifica se Playwright è installato
if ! command -v playwright &> /dev/null
then
    echo "❌ Errore: Playwright non è installato!"
    exit 1
fi

echo "✅ Playwright installato correttamente!"

# Creiamo una cartella locale per i browser Playwright
export PLAYWRIGHT_BROWSERS_PATH="$HOME/.cache/ms-playwright"

# Controlliamo se i browser sono già installati
if [ -d "$PLAYWRIGHT_BROWSERS_PATH" ]; then
    echo "✅ I browser di Playwright sono già installati!"
else
    echo "🔽 Installazione dei browser Playwright..."
    playwright install --with-deps chromium
fi

echo "✅ Installazione completata!"
