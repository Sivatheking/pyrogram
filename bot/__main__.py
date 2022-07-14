from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API_ID="17795696"
API_HASH="afcbcd249c7d8728d9b213b10d39a649"
BOT_TOKEN="5324288989:AAEZNpMAf6DOHveFMOjm-Mxmeu_9TgVBsSg"

Siva = Client(
   name="PyrogramBot",
   api_id=API_ID,
   api_hash=API_HASH,
   bot_token=BOT_TOKEN
)

Button = [[
 InlineKeyboardButton("join here", url="my.telegram.org")
]]




@Siva.on_message(filters.command("start"))
async def start_cmd(client, message):
  

    await message.reply_text(
        text=f"""Hello ! {message.from_user.mention}\nClick my youtube Channel"""
        reply_markup=InlineKeyboardMarkup(Button)
    )



@Siva.on_message(filters.command("hi"))
async def hi_cmd(client, message):
    await message.reply_text("Hello! Iam pyrogram bot")












print("Bot started")

Siva.run()
