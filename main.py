pyTelegramBotAPI
import telebot
from flask import Flask
import threading
8964094842:AAG19kj7LA5-45Q4qhqe4YxeeVv_AiPt2Q8

TOKEN = "YOUR_BOT_TOKEN_HERE" 
bot = telebot.TeleBot(8964094842:AAG19kj7LA5-45Q4qhqe4YxeeVv_AiPt2Q8)
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك! البوت شغال تمام.")

def run_bot():
    bot.polling(non_stop=True)

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    app.run(host="0.0.0.0", port=8080)