from telethon import events
from userbot import bot

# Har qanday xabarga avtomatik javob berish
@bot.on(events.NewMessage(incoming=True))
async def auto_reply(event):
    await event.reply("Assalomu alaykum! @ILHOMOVVV offline bo'lishi mumkin 📴, Vaqti bo'lganida albatta javob beradi. 😊")
