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


RRR = Button = [[
 InlineKeyboardButton(" RRR movie", url="https://new.gdtot.pm/file/3529341865")
]]

START_TEXT = [[
 InlineKeyboardButton("🤖 Help", callback_data="🤖 Help 🤖")
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
        text=f"""𝙷𝚎𝚕𝚕𝚘 ! {message.from_user.mention}\n""",
        reply_markup=InlineKeyboardMarkup(START_TEXT)
    )
        
@Siva.on_message(filters.command("buttons"))
async def buttons_keyboard(client, message):
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
        text="Opening...... Keyboard",
        reply_markup=ReplyKeyboardMarkup(
            [[
                "RRR movie"
            ]],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    )

@Siva.on_message(filters.regex("RRR movie"))
async def start_keyboard(client, message):
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
        photo="https://telegra.ph/file/f4f3e83867591af7fa692.jpg",
        caption="☞︎︎︎ Move : RRR\n☞︎︎︎ Language : multi audios\n☞︎︎︎ Type : inline \n☞︎︎︎ Upload by : @Sivatheking_1",
        reply_markup=InlineKeyboardMarkup(RRR),
    )

       





@Siva.on_message(filters.command("info"))
async def info_cmd(client, msg):
    info = f"""
➪ First Name - {msg.from_user.first_name}
➪ Last Name - {msg.from_user.last_name}
➪ User name - @{msg.chat.username}
➪ Id - {msg.chat.id}
➪ Mention - {msg.from_user.mention}"""

    await msg.reply_text(text=info)

@Siva.on_message(filters.command("id"))
async def id_cmd(client, msg):
    Id = f"""
☞︎︎︎ Your id : `{msg.from_user.id}`"""

    
    await msg.reply_text(text=Id)

@Siva.on_message(filters.command("video"))
async def video(client, msg):
    await msg.reply_video(
        video="https://mdisk.me/convertor/16x9/98Jbhk",
        caption="test"
    )


@Siva.on_callback_query()
async def callback(client, msg: CallbackQuery):
    if msg.data == "🤖 Help 🤖":
        await msg.message.edit(
            text="☞︎︎︎ /id :- ɢᴇᴛ ʏᴏᴜʀ ɪᴅ\n☞︎︎︎ /info :- ɢᴇᴛ ʏᴏᴜʀ ɪɴғᴏʀᴍᴀʀɪᴏɴ\n☞︎︎︎ /buttons :- 𝙾𝚙𝚎𝚗𝚒𝚗𝚐 𝙺𝚎𝚢𝚋𝚘𝚊𝚛𝚍\n☞︎︎︎ /repo :- ᴍʏ sᴏᴜʀᴇ ᴄᴏᴅᴇ\nDᴇᴘʟᴏʏ ʏᴏᴜʀ ᴏᴡɴ ᴍʏ ᴄʟᴏɴᴇ"
        )

    elif msg.data == "repo":
        await msg.message.edit(
            text="our 𝚛𝚎𝚙𝚘 𝚞𝚗𝚍𝚎𝚛 𝚋𝚞𝚝𝚝𝚘𝚗",
            reply_markup=InlineKeyboardMarkup(Source_code)
        )

@Siva.on_message(filters.command("repo"))
async def repo_cmd(client, msg):
    await msg.reply_text(
        text=f"""𝙷𝚎𝚕𝚕𝚘,{msg.from_user.mention}\n𝙼𝚢 𝚛𝚎𝚙𝚘""",
        reply_markup=InlineKeyboardMarkup(repo_data)
    )


Source_code = [[
 InlineKeyboardButton("💻 repo", url="https://github.com/Sivatheking/pyrogram")
]]

repo_data = [[
 InlineKeyboardButton("💻 repo", callback_data="repo_data")
]]      





Siva.run()

def main():

    if SUPPORT_CHAT is not None and isinstance(SUPPORT_CHAT, str):
        try:
            dispatcher.bot.send_message(f"@pyrogram_support", f"[𝙸'𝚊𝚖 𝚛𝚎𝚊𝚍𝚢 𝚝𝚘 𝚋𝚊𝚝𝚝𝚕𝚎]({MIKU_DISPACHER_PIC})", parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(
                [
                  [                  
                       InlineKeyboardButton(
                             text="[► Add me◄]",
                             url="https://t.me/aigarrobot?startgroup=true")
                     ] 
                ]
            ),
        ) 
