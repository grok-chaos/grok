import asyncio
import socket
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "7804091459:AAGavealZz_Mtp6DJ8SkU94cmscjpqOZC9g"
MY_ID = 5214204414  # <--- აქ ჩაწერე შენი ID, რომელიც @userinfobot-მა მოგცა

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != MY_ID:
        return # უცხოებს არ პასუხობს

    await update.message.reply_text("ბოტი მზად არის! გამოიყენე /info")

async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != MY_ID:
        return

    # IP-ს გაგების უსაფრთხო მეთოდი
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = "ვერ დაუკავშირდა"
    finally:
        s.close()

    await update.message.reply_text(f"ჩემი ლოკალური IP არის: {ip}")

def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("info", info))
    print("ბოტი ჩაირთო...")
    application.run_polling()

if __name__ == '__main__':
    main()

