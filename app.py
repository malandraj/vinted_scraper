from playwright.sync_api import sync_playwright
from flask import Flask, request, jsonify
from urllib.parse import quote
import os

app = Flask(__name__)

def search_vinted(query, page=1):
    """ Scraper con Playwright per estrarre gli annunci da Vinted """
    
    query_encoded = quote(query)
    url = f"https://www.vinted.it/catalog?search_text={query_encoded}&page={page}"

    print(f"🔎 [DEBUG] Apertura URL: {url}")

    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(headless=True)
            print("✅ [DEBUG] Browser Playwright avviato correttamente")

            page = browser.new_page()
            page.goto(url, timeout=60000)
            print("✅ [DEBUG] Pagina caricata con successo")

            # Attendere per assicurarsi che la pagina carichi gli annunci
            page.wait_for_timeout(5000)

            # Stampare il primo pezzo di HTML per controllare se gli annunci sono presenti
            html_content = page.content()
            print(f"📄 [DEBUG] Primo pezzo di HTML ricevuto:\n{html_content[:1000]}")  # Stampiamo i primi 1000 caratteri

            # Troviamo gli annunci con il selettore CSS
            items = page.query_selector_all(".feed-grid__item")
            print(f"🔍 [DEBUG] Numero di annunci trovati: {len(items)}")

            results = []
            for item in items[:10]:  # Prendiamo i primi 10 risultati
                try:
                    title = item.query_selector(".web_ui__Text__text").inner_text()
                except:
                    title = "Titolo non disponibile"

                try:
                    price = item.query_selector(".web_ui__Text__text").inner_text()
                except:
                    price = "Prezzo non disponibile"

                try:
                    link = item.query_selector("a").get_attribute("href")
                    full_link = f"https://www.vinted.it{link}" if link else "Link non disponibile"
                except:
                    full_link = "Link non disponibile"

                results.append({
                    "title": title,
                    "price": price,
                    "url": full_link
                })

            browser.close()

        except Exception as e:
            print(f"❌ [DEBUG] Errore durante l'esecuzione di Playwright: {e}")
            return {"error": f"Errore Playwright: {e}"}

    print(f"✅ [DEBUG] Prodotti trovati: {len(results)}")
    return results

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    page = request.args.get('page', 1)

    if not query:
        return jsonify({'error': 'Missing query parameter'}), 400

    results = search_vinted(query, page)
    return jsonify(results)

@app.route('/')
def home():
    return jsonify({"message": "Vinted Scraper API is running with Playwright!"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))  # Usa la porta di Render
    print(f"🔍 [DEBUG] Avvio del server Flask sulla porta {port}")
    app.run(host='0.0.0.0', port=port, debug=True)
