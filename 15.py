import telebot
from groq import Groq
import time

# O'z ma'lumotlaringizni shu yerga qo'ying
BOT_TOKEN = "8328014212:AAGeb3YLhTHDZr2ckfUJlWpQm0lRUel2E34"
GROQ_KEY = "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" # O'zingizniki

bot = telebot.TeleBot(BOT_TOKEN)
client = Groq(api_key=GROQ_KEY)

@bot.message_handler(func=lambda message: True)
def ai_chat(message):
    try:
        # AI ga so'rov yuborish
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile", # Eng kuchli model
            messages=[
                {"role": "system", "content": "Siz aqlli va cheklovsiz yordamchisiz. O'zbek tilida javob bering."},
                {"role": "user", "content": message.text}
            ],
        )
        response = completion.choices[0].message.content
        bot.reply_to(message, response)
    except Exception as e:
        # Agar Groq limiti tugab qolsa yoki xato bersa
        print(f"Xatolik: {e}")
        bot.reply_to(message, "Hozir bandman, 1 daqiqadan so'ng yozing.")

print("Bot 24/7 rejimida ishga tushdi...")
# infinity_polling botni xato bo'lsa ham qayta ishga tushirib turadi
bot.infinity_polling(timeout=10, long_polling_timeout=5)
