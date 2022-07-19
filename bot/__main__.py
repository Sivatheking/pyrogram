from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.types import CallbackQuery, ReplyKeyboardMarkup
from pyrogram.errors import UserNotParticipant 
import os
import script 


Siva = Client(
   name="PyrogramBot",
   bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
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
        
@Siva.on_message(filters.command("buttons"))
async buttons_keyboard(client, msg):
    await msg.reply_text(
        text="Opening...... Keyboard"
        reply_markup=ReplyKeyboardMarkup(
            [[
                "RRR movie"
            ]]
        )
    )

@Siva.on_message(filters.regex("RRR movie"))
async start_keyboard(client, message):
    await message.reply_photo(
        photo="https://telegra.ph/file/e3975e328fad64bd75b18.jpg",
        caption="Move : RRR\nLanguage : multi audios\nType : inline \nUpload by : @Sivatheboss",
        reply_markup=InlineKeyboardMarkup(Button),
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





@Siva.on_message(filters.command("info"))
async def info_cmd(client, msg):
    info = f"""
First Name - {msg.from_user.first_name}
Last Name - {msg.from_user.last_name}
User name - @{msg.from_user.username}
Id - {msg.from_user.id}
Mention - {msg.from_user.mention}"""

    await msg.reply_text(text=info)

@Siva.on_message(filters.command("id"))
async def id_cmd(client, msg):
    Id = f"""
Your id - `{msg.chat.id}`"""
    
    await msg.reply_text(text=Id)












print("Bot started")

Siva.run()
