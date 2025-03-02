from flask import Flask, request, jsonify
from vinted_scraper import VintedScraper

app = Flask(__name__)

# Inizializziamo lo scraper con il sito di Vinted Italia
scraper = VintedScraper(
    baseurl='https://www.vinted.it',
    agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    session_cookie="fake_cookie_value"  # Forziamo un valore per bypassare il problema
)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    if not query:
        return jsonify({'error': 'Missing query parameter'}), 400

    results = scraper.search(query)
    
    # Convertiamo gli oggetti in un formato JSON leggibile
    formatted_results = [
        {
            "id": item.id,
            "title": item.title,
            "price": item.price,
            "currency": item.currency,
            "brand": item.brand.title if item.brand else "Unknown",
            "url": f"https://www.vinted.it/items/{item.id}"
        }
        for item in results
    ]

    return jsonify(formatted_results)

@app.route('/')
def home():
    return jsonify({"message": "Vinted Scraper API is running!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
