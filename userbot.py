from telethon import TelegramClient, events

# API ma'lumotlari
API_ID = 21116146  # YOUR API_ID
API_HASH = "6bd0c7ed0b7bf43e8a335f08752016ed"  # YOUR API_HASH
SESSION_NAME = "userbot"

# Userbotni ishga tushirish
bot = TelegramClient(SESSION_NAME, API_ID, API_HASH)

# Har qanday xabarga avtomatik javob berish
@bot.on(events.NewMessage(incoming=True))
async def auto_reply(event):
    await event.reply("Assalomu alaykum! @ILHOMOVVV offline bo'lishi mumkin 📴, Vaqti bo'lganida albatta javob beradi. 😊")
# Botni ishga tushirish
print("Userbot ishga tushdi! ✅")
bot.start()
bot.run_until_disconnected()
