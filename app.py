from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from flask import Flask, request, jsonify
from urllib.parse import quote

app = Flask(__name__)

def search_vinted(query, page=1):
    """ Scraper con Selenium per estrarre gli annunci da Vinted """
    
    query_encoded = quote(query)
    url = f"https://www.vinted.it/catalog?search_text={query_encoded}&page={page}"
    
    print(f"🔎 [DEBUG] Apertura URL: {url}")

    # Configura il WebDriver di Chrome
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Se vuoi vedere il browser, rimuovi questa linea
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    # Apri la pagina di Vinted
    driver.get(url)
    time.sleep(5)  # Aspettiamo che la pagina carichi gli annunci

    # Troviamo tutti gli annunci
    items = driver.find_elements(By.CLASS_NAME, "new-item-box__container")

    print(f"🔍 [DEBUG] Numero di annunci trovati: {len(items)}")

    results = []
    for item in items:
        try:
            title = item.find_element(By.CLASS_NAME, "web_ui__Text__text").text
        except:
            title = "Titolo non disponibile"

        try:
            price = item.find_element(By.CLASS_NAME, "web_ui__Text__text").text
        except:
            price = "Prezzo non disponibile"

        try:
            link = item.find_element(By.CLASS_NAME, "new-item-box__overlay").get_attribute("href")
        except:
            link = "Link non disponibile"

        results.append({
            "title": title,
            "price": price,
            "url": link
        })

    driver.quit()  # Chiudi il browser

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
    return jsonify({"message": "Vinted Scraper API is running!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
