import time
import requests
from bs4 import BeautifulSoup
from telegram import Bot

TOKEN = "7840863675:AAETQXyAkyJv4JgqsNbhMyDnDpAQ6B7lrVM"
CHAT_ID = "902064209"
CHECK_INTERVAL = 300  # toutes les 5 minutes
URL = "https://trouverunlogement.lescrous.fr/tools/search/logement?type[]=1&location=Clermont-Ferrand"

bot = Bot(token=TOKEN)
dernier = ""

print("🤖 Bot CROUS démarré. Surveillance en cours.")

while True:
    try:
        resp = requests.get(URL, timeout=10)
        soup = BeautifulSoup(resp.text, "html.parser")
        annonces = soup.select("h2.search-logement-title")
        if annonces:
            titre = annonces[0].get_text(strip=True)
            if titre != dernier:
                dernier = titre
                bot.send_message(chat_id=CHAT_ID, text=f"🏠 Nouveau logement : {titre}")
                print(f"Nouveau logement détecté : {titre}")
            else:
                print("Pas de nouveau logement.")
        else:
            print("Aucune annonce trouvée.")
    except Exception as e:
        print("Erreur pendant scrapping :", e)
    time.sleep(CHECK_INTERVAL)
