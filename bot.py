
import os
import asyncio
from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# ==============================
# SEDOSKI PREDICTION BOT
# ==============================

TOKEN = os.environ.get("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN n'est pas configuré.")

# Flask pour le Web Service
app = Flask(__name__)

# Application Telegram
telegram_app = Application.builder().token(TOKEN).build()


# ==============================
# COMMANDES TELEGRAM
# ==============================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "⚽ Bienvenue sur SEDOSKI PREDICTIONS !\n\n"
        "🤖 Bot de prédictions football.\n\n"
        "Utilise /predict pour commencer.\n"
        "Utilise /today pour voir les matchs du jour.\n"
        "Utilise /help pour voir les commandes."
    )


async def predict(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔮 SEDOSKI PREDICTIONS\n\n"
        "Envoie-moi le match sous cette forme :\n\n"
        "PSG vs Marseille\n\n"
        "📊 Une analyse pourra ensuite être effectuée."
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
# AJOUT DES COMMANDES
# ==============================

telegram_app.add_handler(CommandHandler("start", start))
telegram_app.add_handler(CommandHandler("predict", predict))
telegram_app.add_handler(CommandHandler("today", today))
telegram_app.add_handler(CommandHandler("help", help_command))


# ==============================
# ROUTE WEB
# ==============================

@app.route("/")
def home():
    return "SEDOSKI Predictions Bot is running!"


# ==============================
# DEMARRAGE DU BOT
# ==============================

async def run_bot():
    await telegram_app.initialize()
    await telegram_app.start()
    await telegram_app.updater.start_polling()

    print("🤖 SEDOSKI PREDICTIONS BOT démarré !")

    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(run_bot())