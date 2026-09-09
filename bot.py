import os

from flask import Flask

from telegram import Update

from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.environ["BOT_TOKEN"]

app = Flask(__name__)

telegram_app = Application.builder().token(TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(

        "⚽ Bienvenue sur Sedoski Predictions !\n\n"

        "Utilise /predict pour commencer."

    )

async def predict(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(

        "🔮 Envoie le match comme ceci :\n\n"

        "PSG vs Marseille"

    )

async def today(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(

        "⚽ Les matchs du jour seront bientôt disponibles."

    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(

        "/start - Demarrer le bot\n"

        "/predict - Predire un match\n"

        "/today - Matchs du jour\n"

        "/help - Aide"

    )

telegram_app.add_handler(CommandHandler("start", start))

telegram_app.add_handler(CommandHandler("predict", predict))

telegram_app.add_handler(CommandHandler("today", today))

telegram_app.add_handler(CommandHandler("help", help_command))

@app.route("/")

def home():

    return "Sedoski Predictions Bot is running!"

if __name__ == "__main__":

    import asyncio

    async def main():

        await telegram_app.initialize()

        await telegram_app.start()

        print("Bot Sedoski demarre...")

        await telegram_app.updater.start_polling()

        await asyncio.Event().wait() asyncio.run(main())
