from pyrogram import Client, filters

API_ID="17795696"
API_HASH="afcbcd249c7d8728d9b213b10d39a649"
BOT_TOKEN="5324288989:AAEZNpMAf6DOHveFMOjm-Mxmeu_9TgVBsSg"

Siva = Client(
   name="PyrogramBot",
   api_id=API_ID,
   api_hash=API_HASH,
   bot_token=BOT_TOKEN
)
@Siva.on_message(filters.group & filters.command("start"))
async def start_cmd(client, message):
   await message.reply_text(
       text=f"""Hello! Iam pyrogram bot {message.from_user.mention}""",
   )


@Siva.on_message(filters.command("hi"))
async def hi_cmd(client, message):
    await message.reply_text("Hello! Iam pyrogram bot")












print("Bot started")

Siva.run()
