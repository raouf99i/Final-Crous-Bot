import requests
from bs4 import BeautifulSoup
import time

TOKEN = "7840863675:AAETQXyAkyJv4JgqsNbhMyDnDpAQ6B7lrVM"
CHAT_ID = "902064209"
URL = "https://trouverunlogement.lescrous.fr/tools/search/logement?type[]=1&location=Clermont-Ferrand"

dernier = ""

def send_msg(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": text})

print("🤖 Bot CROUS démarré avec Telegram API.")

while True:
    try:
        res = requests.get(URL, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")
        annonces = soup.select("h2.search-logement-title")
        if annonces:
            titre = annonces[0].get_text(strip=True)
            if titre != dernier:
                dernier = titre
                msg = f"🏠 Nouveau logement : {titre}"
                send_msg(msg)
                print("✅ Message envoyé :", msg)
            else:
                print("🔁 Rien de nouveau.")
        else:
            print("📭 Aucune annonce.")
    except Exception as e:
        print("❗ Erreur check :", e)

    time.sleep(300)
