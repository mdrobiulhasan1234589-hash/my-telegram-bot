import telebot
import os

API_TOKEN = os.environ.get('TELEGRAM_TOKEN')

bot = telebot.TeleBot(API_TOKEN)

AUTO_REPLY_TEXT = """🌟 আসসালামু আলাইকুম!
আপনার কোনো সমস্যা বা সাহায্যের প্রয়োজন হলে বিস্তারিতভাবে আমাকে জানাবেন। 😊
আপনার মেসেজটি দেখার পর যত দ্রুত সম্ভব আপনাকে রিপ্লাই দেওয়ার চেষ্টা করব। 🤝
👨‍💻 Developer Robiul 🚀"""

@bot.message_handler(func=lambda message: True)
def send_auto_reply(message):
    bot.reply_to(message, AUTO_REPLY_TEXT)

if __name__ == "__main__":
    print("বট চালু হয়েছে...")
    bot.infinity_polling()
