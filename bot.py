import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8085473705:AAHJCtBcL0M2VAmSr_cvwu6sk809zi5yvt0"

async def tgm_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message.reply_to_message:
        await update.message.reply_text("You must reply to a message that contains a file.")
        return

    message = update.message.reply_to_message

    # Get the file from the replied message
    file = None
    if message.document:
        file = message.document
    elif message.photo:
        file = message.photo[-1]
    elif message.video:
        file = message.video

    if not file:
        await update.message.reply_text("Unsupported file type.")
        return

    telegram_file = await file.get_file()
    file_data = await telegram_file.download_as_bytearray()
    file_name = getattr(file, 'file_name', 'file')

    # Upload to Catbox
    files = {'fileToUpload': (file_name, file_data)}
    response = requests.post("https://catbox.moe/user/api.php", data={"reqtype": "fileupload"}, files=files)

    if response.ok:
        await update.message.reply_text(f"Uploaded to Catbox:\n{response.text}")
    else:
        await update.message.reply_text("Upload failed.")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("tgm", tgm_handler))
    print("Bot is running...")
    app.rimport os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def tgm_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message.reply_to_message:
        await update.message.reply_text("You must reply to a message that contains a file.")
        return

    message = update.message.reply_to_message

    file = None
    if message.document:
        file = message.document
    elif message.photo:
        file = message.photo[-1]
    elif message.video:
        file = message.video

    if not file:
        await update.message.reply_text("Unsupported file type.")
        return

    telegram_file = await file.get_file()
    file_data = await telegram_file.download_as_bytearray()
    file_name = getattr(file, 'file_name', 'file')

    files = {'fileToUpload': (file_name, file_data)}
    response = requests.post("https://catbox.moe/user/api.php", data={"reqtype": "fileupload"}, files=files)

    if response.ok:
        await update.message.reply_text(f"Uploaded to Catbox:\n{response.text}")
    else:
        await update.message.reply_text("Upload failed.")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("tgm", tgm_handler))
    print("Bot is running...")
    app.run_polling()un_polling()
