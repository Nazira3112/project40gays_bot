from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

# ==========================
# НАСТРОЙКИ
# ==========================

BOT_TOKEN = "YOUR_NEW_BOT_TOKEN"
OWNER_ID = 6229829943

WELCOME_TEXT = """
🕊️ <b>40 Days Without You</b>

Иногда есть слова, которые невозможно произнести вслух.

Иногда признание живёт годами и так и не находит своего адресата.

Здесь можно оставить то, что вы никогда никому не говорили.

Ваше сообщение станет частью художественного проекта.

Пожалуйста, не указывайте имена, телефоны или другие личные данные, если хотите сохранить анонимность.

Когда будете готовы — просто отправьте сообщение.
"""

THANK_YOU = """
Спасибо.

Ваш голос сохранён.

Возможно, однажды он станет частью произведения искусства.
"""

# ==========================
# КОМАНДА /start
# ==========================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_html(WELCOME_TEXT)

# ==========================
# ПРИЁМ СООБЩЕНИЙ
# ==========================

async def receive_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text

    await context.bot.send_message(
        chat_id=OWNER_ID,
        text=f"📝 Новое признание:\n\n{text}"
    )

    await update.message.reply_text(THANK_YOU)

# ==========================
# ЗАПУСК
# ==========================

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, receive_message))

print("Bot is running...")

app.run_polling()
