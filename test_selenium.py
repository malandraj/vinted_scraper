from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# Configura il WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Rimuovi questa linea se vuoi vedere il browser
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Apriamo la pagina di Vinted
url = "https://www.vinted.it/catalog?search_text=cappotto%20armani&page=1"
print(f"🔎 [DEBUG] Apertura URL: {url}")
driver.get(url)

time.sleep(5)  # Aspettiamo che la pagina carichi gli annunci

# Stampiamo il titolo della pagina per conferma
print(f"📄 [DEBUG] Titolo della pagina: {driver.title}")

# Troviamo tutti gli annunci con il nuovo selettore
items = driver.find_elements(By.CLASS_NAME, "new-item-box__container")

print(f"🔍 [DEBUG] Numero di annunci trovati: {len(items)}")

# Stampiamo i dettagli dei primi 5 annunci
for item in items[:5]:
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

    print(f"🛍️ [ANNUNCIO] {title} - {price} - {link}")

driver.quit()

