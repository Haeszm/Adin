import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from AnonXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonXMusic import app
from random import  choice, randint


                

@app.on_message(filters.command(["ايدن","المطور"]), group=703) 
async def yas(client, message):
    usr = await client.get_chat("B_U_P")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**\n\n☠️ ¦𝙺𝙸𝙽𝙶 :{name}\n🥰 ¦𝚄𝚂𝙴𝚁 :@{usr.username}\n😎 ¦𝙸𝙳 :{usr.id}\n💕 ¦𝙱𝙸𝙾 :{usr.bio}\n\n**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )