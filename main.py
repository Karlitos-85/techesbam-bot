import os
import time
import random
from telegram import Bot

# Variabili da ambiente
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
AFFILIATE_TAG = os.getenv("AMAZON_TAG")
CHANNEL = os.getenv("TELEGRAM_CHANNEL")

bot = Bot(token=TOKEN)

# Frasi ironiche da usare nei messaggi
intro = [
    "📦 Amazon ci vizia oggi... come se avesse sensi di colpa.",
    "🔌 Offerta tech o provocazione personale? Decidi tu.",
    "🎮 Sconto pazzo — ma solo se lo meriti. Tu lo meriti.",
    "⚠️ Offerta che non puoi ignorare (ma puoi far finta di sì)",
    "🥲 Hai detto 'non spendo più'? Mi dispiace."
]

# Prodotti placeholder (da sostituire con scraping/API)
prodotti = [
    {"titolo": "🎧 Cuffie Gaming HyperX", "link": "https://www.amazon.it/dp/B07ABC456"},
    {"titolo": "🔋 Powerbank 20000mAh", "link": "https://www.amazon.it/dp/B08XYZ123"},
    {"titolo": "🖥️ Monitor 27'' 144Hz", "link": "https://www.amazon.it/dp/B09GAMING99"}
]

def crea_link_affiliato(link):
    return f"{link}?tag={AFFILIATE_TAG}"

def genera_messaggio(prodotto):
    frase = random.choice(intro)
    hashtag = "#TechSbamDelGiorno"
    return f"{frase}\n\n🛒 {prodotto['titolo']}\n➡️ {crea_link_affiliato(prodotto['link'])}\n\n{hashtag}"

# Messaggio di benvenuto al primo avvio
bot.send_message(chat_id=CHANNEL, text="Benvenuti su Tech & Sbam 💥 — dove le offerte Amazon sono più puntuali di me alla pausa pranzo.")

# Ciclo orario di pubblicazione
while True:
    prodotto = random.choice(prodotti)
    messaggio = genera_messaggio(prodotto)
    bot.send_message(chat_id=CHANNEL, text=messaggio)
    time.sleep(3600)  # Pubblica ogni ora
