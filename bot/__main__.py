from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
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

Info = """
First Name - {msg.from_user.first_name}
Last Name - {msg.from_user.last_name}
User name - @{msg.from_user.user_name}
Id - {msg.from_user.id}
"""



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
            user = await client.get_chat_member(Forse_channel, message.from_user.id)     
            if user.status == "kicked out":
                await message.reply_text("You are banned")
                return
        except UserNotParticipant:
            await message.reply_text(
                text="You are not sub... My channel",
                reply_markup=InlineKeyboardMarkup(Channel)
            )       
            return 

    if Forse_group:
        try:
            user = await client.get_chat_member(Forse_group, message.from_user.id)     
            if user.status == "kicked out":
                await message.reply_text("You are banned")
                return
        except UserNotParticipant:
            await message.reply_text(
                text="You are not sub... My group",
                reply_markup=InlineKeyboardMarkup(Group)
            )       
            return 

    await message.reply_text(
        text=f"""Hello ! {message.from_user.mention}\nClick my youtube Channel""",
        reply_markup=InlineKeyboardMarkup(Button)
    )



@Siva.on_message(filters.command("movies"))
async def movies_cmd(client, message):
    if Forse_channel:
        try:
            user = await client.get_chat_member(Forse_channel, message.from_user.id)     
            if user.status == "kicked out":
                await message.reply_text("You are banned")
                return
        except UserNotParticipant:
            await message.reply_text(
                text="You are not sub... My channel",
                reply_markup=InlineKeyboardMarkup(Channel)
            )       
            return 

    if Forse_group:
        try:
            user = await client.get_chat_member(Forse_group, message.from_user.id)     
            if user.status == "kicked out":
                await message.reply_text("You are banned")
                return
        except UserNotParticipant:
            await message.reply_text(
                text="You are not sub... My group",
                reply_markup=InlineKeyboardMarkup(Group)
            )       
            return 



    await message.reply_photo(
        photo="https://telegra.ph/file/e3975e328fad64bd75b18.jpg",
        caption="<b> only telegram</b>",
        reply_markup=InlineKeyboardMarkup(Button),
        )












print("Bot started")

Siva.run()
