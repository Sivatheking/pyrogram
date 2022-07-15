from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant 


API_ID="17795696"
API_HASH="afcbcd249c7d8728d9b213b10d39a649"
BOT_TOKEN="5324288989:AAEZNpMAf6DOHveFMOjm-Mxmeu_9TgVBsSg"

Siva = Client(
   name="PyrogramBot",
   api_id=API_ID,
   api_hash=API_HASH,
   bot_token=BOT_TOKEN
)
Forse_channel = "Pyrogram_updates"

Forse_group = "pyrogram_support"


Channel = [[
 InlineKeyboardButton("join here", url=f"t.me/{Forse_channel}")
]]

Group = [[
 InlineKeyboardButton("join here", url=f"t.me/{Forse_group}")
]]


Button = [[
 InlineKeyboardButton("join here", url="https://youtube.com/channel/UCTENtjruBCz3gJlXUfvdvZQ"),
 InlineKeyboardButton ("Add me", url="https://t.me/pyrogram66_bot?startgroup=true")
]]




@Siva.on_message(filters.command("start"))
async def start_cmd(client, message):
    if Forse_channel:
        try:
            user = await client.get_chat_member(Forse_channel, message.from_use.id)     
            if user.status == "kicked out"
                await message.reply_text("You are banned")
                return
        except UserNotParticipant:
            await message.reply_text(
                text="You are not sub... My channel",
                reply_markup=InlineKeyboardMarkup(Channel)
            )       
            returen 

    await message.reply_text(
        text=f"""Hello ! {message.from_user.mention}\nClick my youtube Channel""",
        reply_markup=InlineKeyboardMarkup(Button)
    )



@Siva.on_message(filters.command("movies"))
async def movies_cmd(client, message):
    await message.reply_photo(
        photo="https://telegra.ph/file/e3975e328fad64bd75b18.jpg",
        caption="<b> only telegram</b>",
        reply_markup=InlineKeyboardMarkup(Button),
        )












print("Bot started")

Siva.run()
