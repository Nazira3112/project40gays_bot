from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "8784337580:AAHETBLcR7Gn25Yv-QEVlMHmcyxlzzXKmZM"
OWNER_ID = 6229829943

WELCOME = """
🕊️ <b>40 Days Without You</b>

Иногда есть слова, которые невозможно произнести вслух.

Иногда признание живёт годами и так и не находит своего адресата.

Здесь можно оставить то, что вы никогда никому не говорили.

Ваше сообщение станет частью художественного проекта.

Пожалуйста, не указывайте имена и другие личные данные, если хотите сохранить анонимность.

Когда будете готовы — просто отправьте сообщение.
"""

THANKS = """
Спасибо.

Ваш голос сохранён.

Возможно, однажды он станет частью произведения искусства.
"""


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_html(WELCOME)


async def message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    await context.bot.send_message(
        OWNER_ID,
        f"📝 Новое признание:\n\n{text}"
    )

    await update.message.reply_text(THANKS)


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message))

app.run_polling()
