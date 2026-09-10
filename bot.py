import os
import threading

from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# ==============================
# SEDOSKI PREDICTIONS BOT
# ==============================

TOKEN = os.environ.get("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN n'est pas configuré.")

# ==============================
# FLASK - SERVEUR WEB
# ==============================

app = Flask(__name__)


@app.route("/")
def home():
    return "SEDOSKI Predictions Bot is running!"


def run_flask():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


# ==============================
# COMMANDES TELEGRAM
# ==============================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "⚽ Bienvenue sur SEDOSKI PREDICTIONS !\n\n"
        "🤖 Bot de prédictions football.\n\n"
        "Utilise /predict pour commencer.\n"
        "Utilise /today pour les matchs du jour.\n"
        "Utilise /help pour voir les commandes."
    )


async def predict(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔮 SEDOSKI PREDICTIONS\n\n"
        "Envoie le match sous cette forme :\n\n"
        "PSG vs Marseille\n\n"
        "📊 L'analyse du match sera effectuée."
    )


async def today(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "⚽ MATCHS DU JOUR\n\n"
        "Les matchs du jour seront bientôt disponibles."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📚 SEDOSKI PREDICTIONS - AIDE\n\n"
        "/start - Démarrer le bot\n"
        "/predict - Prédire un match\n"
        "/today - Matchs du jour\n"
        "/help - Afficher l'aide\n\n"
        "⚠️ Les prédictions sont indicatives et ne garantissent "
        "pas le résultat d'un match."
    )


# ==============================
# APPLICATION TELEGRAM
# ==============================

telegram_app = Application.builder().token(TOKEN).build()

telegram_app.add_handler(CommandHandler("start", start))
telegram_app.add_handler(CommandHandler("predict", predict))
telegram_app.add_handler(CommandHandler("today", today))
telegram_app.add_handler(CommandHandler("help", help_command))


# ==============================
# DÉMARRAGE
# ==============================

if __name__ == "__main__":
    # Démarre Flask dans un autre thread
    threading.Thread(target=run_flask, daemon=True).start()

    print("🤖 SEDOSKI PREDICTIONS BOT démarré !")

    # Démarre Telegram
    telegram_app.run_polling()