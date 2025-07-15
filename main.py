import os
import random
from telegram import Bot
from telegram.error import TelegramError
from apscheduler.schedulers.blocking import BlockingScheduler

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHANNEL = os.getenv("TELEGRAM_CHANNEL")
AMAZON_TAG = os.getenv("AMAZON_TAG")

bot = Bot(token=TELEGRAM_BOT_TOKEN)
scheduler = BlockingScheduler(timezone="Europe/Rome")

OFFERS = [
    {
        "title": "Cuffie Sony WH-1000XM5",
        "price": "289,00€",
        "discount": "18%",
        "link": f"https://www.amazon.it/dp/B09XM4TJ4L?tag={AMAZON_TAG}"
    },
    {
        "title": "Nintendo Switch OLED",
        "price": "309,00€",
        "discount": "20%",
        "link": f"https://www.amazon.it/dp/B098RKWHHZ?tag={AMAZON_TAG}"
    },
    {
        "title": "Robot Aspirapolvere iRobot Roomba",
        "price": "199,00€",
        "discount": "33%",
        "link": f"https://www.amazon.it/dp/B09HXD9C55?tag={AMAZON_TAG}"
    }
]

def send_test():
    offer = random.choice(OFFERS)
    text = (
        f"🧪 TEST: *{offer['title']}*\n"
        f"💸 Prezzo: {offer['price']}\n"
        f"📉 Sconto: {offer['discount']}\n"
        f"🛒 [Prendila ora]({offer['link']})"
    )
    try:
        bot.send_message(chat_id=TELEGRAM_CHANNEL, text=text, parse_mode="Markdown")
        print("Messaggio inviato!")
    except TelegramError as e:
        print("Errore Telegram:", e)

def schedule_job():
    scheduler.add_job(send_test, 'date')
    scheduler.start()

if __name__ == "__main__":
    send_test()
