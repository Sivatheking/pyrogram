from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.types import CallbackQuery, ReplyKeyboardMarkup
from pyrogram.errors import UserNotParticipant 
import os
import script 
import asyncio


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
 InlineKeyboardButton("💫 About", callback_data="about")
],[
 InlineKeyboardButton("🖥️ repo", callback_data="repoo")
],[
 InlineKeyboardButton("fun", callback_data="fun"),
]]

Hia = [[
 InlineKeyboardButton("fun", callback_data="fun"),
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
➪ Last Name - {msg.from_user.last_name} or "NONE"
➪ User name - @{msg.chat.username} or "NONE"
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


        reply1 = await msg.message.edit("`processing.....`")

        await msg.message.edit(
            text="☞︎︎︎ /id :- ɢᴇᴛ ʏᴏᴜʀ ɪᴅ\n☞︎︎︎ /info :- ɢᴇᴛ ʏᴏᴜʀ ɪɴғᴏʀᴍᴀʀɪᴏɴ\n☞︎︎︎ /buttons :- 𝙾𝚙𝚎𝚗𝚒𝚗𝚐 𝙺𝚎𝚢𝚋𝚘𝚊𝚛𝚍\n☞︎︎︎ /repo :- ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴍʏ ʀᴇᴘᴏ"
        )

    elif msg.data == "about":


        reply1 = await msg.message.edit("`processing.....`")
        await asyncio.sleep(5)

        await reply1.edit(
            text= f"""
                𝐇𝐞𝐥𝐥𝐨 {msg.from_user.mention}
                \n❍ 𝐌𝐲 𝐎𝐰𝐧𝐞𝐫 :- [꧁༒︎༒︎༆༆𝐒𝐢𝐯𝐚𝐭𝐡𝐞𝐛𝐨𝐬𝐬༆༆༒︎༒︎꧂](t.me/Sivatheking_1)
                \n❍ 𝐌𝐲 𝐬𝐮𝐩𝐩𝐨𝐫𝐭 :- [ᴘʏʀᴏɢʀᴀᴍ sᴜᴘᴘᴏʀᴛ](t.me/pyrogram_support)
                \n❍ 𝐌𝐲 𝐋𝐨𝐠𝐬 :- [ᴍʏ ʟᴏɢs ᴄʜᴀɴɴᴇʟ](t.me/lovelybot_logs)
                \n★ 𝙽𝚘𝚝𝚎 
                \n\nᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ ɪs [𝔾𝕚𝕥𝕙𝕦𝕓](githu.com/Sivatheking) . ᴄᴏᴅᴇ ᴡʀɪᴛᴇʀ ɪs [sɪᴠᴀᴛʜᴇᴋɪɴɢ](t.me/Sivatheking_1) . 
                \n\n★ 𝙸𝚖𝚙𝚘𝚛𝚝𝚊𝚗𝚝 𝙽𝚘𝚝𝚒𝚌𝚎
                \n𝙼𝚢 𝙾𝚠𝚗𝚎𝚛 𝚗𝚘𝚝 𝚠𝚛𝚒𝚝𝚎 𝚌𝚘𝚖𝚙𝚕𝚎𝚝𝚎 𝚌𝚘𝚍𝚎 𝚏𝚘𝚛  𝚐𝚛𝚘𝚞𝚙 𝚖𝚊𝚗𝚊𝚐𝚎 𝚜𝚘𝚘𝚗 𝚐𝚛𝚘𝚞𝚙 𝚖𝚊𝚗𝚐𝚎 𝚋𝚘𝚝 (𝚘𝚛) 𝚆𝚒𝚝𝚑𝚘𝚞𝚝 𝙶𝚛𝚘𝚞𝚙 𝙼𝚊𝚗𝚐𝚎 𝚊𝚌𝚌𝚎𝚜𝚜 𝚖𝚢 𝚜𝚘𝚞𝚛𝚌𝚎"""
        )

    elif msg.data == "repoo":
        await msg.message.edit(
            text=f""" ʜᴇʟʟᴏ {msg.from_user.mention}\n ᴍʏ ʀᴇᴘᴏ ɪs ᴘʀɪᴠᴀᴛᴇ"""
    )
    elif msg.data == "fun":
        reply1 = await msg.message.edit("☾︎")
        await asyncio.sleep(5)
        reply2 = await reply1.edit("☾︎       🌍")
        await asyncio.sleep(5)
        await reply2.edit("☾︎  🌍 ☀️  ")
        
  
@Siva.on_message(filters.command("fun"))     
async def fun_cmd(client, msg):
    await msg.reply_text(
        reply_markup=InlineKeyboardMarkup(Hia)
    )


Source_code = [[
 InlineKeyboardButton("fun", callback_data="fun")
]]

repo_data = [[
 InlineKeyboardButton("💻 repo", callback_data="repoᴏ")
]]      


print("Bot started")

Siva.run()
