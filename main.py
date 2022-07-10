from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, Update

API_ID="17795696"
API_HASH="afcbcd249c7d8728d9b213b10d39a649"
BOT_TOKEN="5324288989:AAEZNpMAf6DOHveFMOjm-Mxmeu_9TgVBsSg"

Siva = Client(
   name="PyrogramBot",
   api_id=API_ID,
   api_hash=API_HASH,
   bot_token=BOT_TOKEN
)

@Siva.on_message(filters.command("start")),
    await message.reply_text(
        text="*hello welcome to our bot.*"
        reply_markup=InlineKeyboardMarkup([[
        InlineKeyboardButton("demo button", url="https://github.com/Sivatheking/pyrogram")
        ],
    ]
               
          





button = [
    [         
             InlineKeyboardButton(
                  text=" hi",
                  url="https://github.com/Sivatheking/pyrogram")
              ],
    ]



   





print("Bot strarted")

Siva.run()
