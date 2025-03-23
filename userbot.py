from pyrogram import Client, filters
import asyncio

# API ma'lumotlari
API_ID = 21116146  # YOUR API_ID
API_HASH = "6bd0c7ed0b7bf43e8a335f08752016ed"  # YOUR API_HASH
SESSION_NAME = "userbot"

# Userbotni ishga tushirish
app = Client(SESSION_NAME, api_id=API_ID, api_hash=API_HASH)

# Animatsiyalar ro‘yxati (200+)
animations = {
    "apple_animate": "🍏🍎🍏",
    "fire_animate": "🔥🔥🔥🔥🔥",
    "wave_animate": "👋👋👋👋👋",
    "love_animate": "❤️🧡💛💚💙💜",
    "smile_animate": "😊😁😂🤣😃😄😆",
    "star_animate": "⭐✨💫🌟",
    "moon_animate": "🌕🌖🌗🌘🌑🌒🌓🌔",
    "earth_animate": "🌍🌎🌏",
    "clock_animate": "🕛🕐🕑🕒🕓🕔🕕🕖🕗🕘🕙🕚",
    "flag_animate": "🏴🚩🏳️🏴‍☠️🏁",
    "rainbow_animate": "🌈🌈🌈🌈🌈",
    "dance_animate": "💃🕺💃🕺💃🕺",
    "sleep_animate": "😴💤💤💤",
    "ghost_animate": "👻👻👻👻👻",
    "money_animate": "💵💰💳💸💷💶💴",
    "rocket_animate": "🚀🚀🚀🚀🚀",
    "bulb_animate": "💡🔆🔅💡",
    "music_animate": "🎵🎶🎼🎤🎧🎹",
    "coffee_animate": "☕🍵🥤",
    "pizza_animate": "🍕🍕🍕🍕🍕",
    "cake_animate": "🎂🍰🧁🎂",
    "gift_animate": "🎁🎀🎁🎀",
    "fireworks_animate": "🎇🎆🎇🎆🎇",
    "medal_animate": "🏅🥇🥈🥉🏆",
    "soccer_animate": "⚽🏀🏈⚾🎾🏐🏉",
    "car_animate": "🚗🚕🚙🚌🚎🏎️🚓",
    "train_animate": "🚂🚆🚇🚊🚉",
    "plane_animate": "✈️🛫🛬🛩",
    "ship_animate": "🚢⛵🛥️🛶",
    "flower_animate": "🌹🌻🌼🌷💐",
    "heart_animate": "💓💗💖💘💝",
    "angel_animate": "😇👼😇",
    "alien_animate": "👽🛸👾",
    "robot_animate": "🤖🤖🤖",
    "cool_animate": "😎🕶️😎",
    "bomb_animate": "💣💥💣💥",
    "hourglass_animate": "⏳⌛",
    "sun_animate": "☀️🌤️🌞",
    "cloud_animate": "☁️🌥️⛅",
    "snowflake_animate": "❄️⛄❄️",
    "thunder_animate": "⚡⚡⚡",
}

# Animatsiya yuborish funksiyasi
@app.on_message(filters.command("animate", prefixes=".") & filters.me)
async def animate_emoji(client, message):
    args = message.text.split()
    if len(args) < 2:
        await message.reply("Foydalanish: `.animate <animatsiya nomi>`\nMasalan: `.animate fire_animate`")
        return
    
    key = args[1]
    if key in animations:
        await message.reply(animations[key])
    else:
        await message.reply("Bunday animatsiya topilmadi!")

# Komandalar ro'yxatini Telegram kanaliga yuborish
async def send_command_list():
    CHANNEL_ID = "1002670527707"  # O'z kanal IDingizni kiriting
    commands_text = "**Userbot komandalar ro‘yxati:**\n\n"
    for key in animations.keys():
        commands_text += f"🔹 `.animate {key}`\n"

    await app.send_message(CHANNEL_ID, commands_text)

# Botni ishga tushirganda komandalarni yuborish
@app.on_message(filters.command("send_commands", prefixes=".") & filters.me)
async def send_commands(client, message):
    await send_command_list()
    await message.reply("Komandalar Telegram kanalga yuborildi!")

print("Userbot ishga tushdi!")
app.run()