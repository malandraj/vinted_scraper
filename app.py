from playwright.sync_api import sync_playwright
from flask import Flask, request, jsonify
from urllib.parse import quote

app = Flask(__name__)

def search_vinted(query, page=1):
    """ Scraper con Playwright per estrarre gli annunci da Vinted """
    
    query_encoded = quote(query)
    url = f"https://www.vinted.it/catalog?search_text={query_encoded}&page={page}"

    print(f"🔎 [DEBUG] Apertura URL: {url}")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # Avvia Chromium in modalità headless
        page = browser.new_page()
        page.goto(url, timeout=60000)  # Timeout di 60 secondi per caricare la pagina

        # Selettore per gli annunci su Vinted
        items = page.query_selector_all(".feed-grid__item")

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
    app.run(host='0.0.0.0', port=5000, debug=True)
