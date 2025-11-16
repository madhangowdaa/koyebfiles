from bot import Bot
from pyrogram.types import Message
from pyrogram import filters
from config import ADMINS, BOT_STATS_TEXT, USER_REPLY_TEXT
from datetime import datetime
from helper_func import get_readable_time

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

@Bot.on_message(filters.command('join') & filters.private)
async def followus(bot: Bot, message: Message):
    reply_markup=InlineKeyboardMarkup(
                        [
                         [
                          InlineKeyboardButton('🎬 𝑴𝒐𝒗𝒊𝒆𝒔 𝒈𝒓𝒐𝒖𝒑', url="t.me/+BtIY_7IaFKgxYzQ1"),
                          InlineKeyboardButton('🥹 𝑼𝒑𝒅𝒂𝒕𝒆𝒔 𝑪𝒉𝒂𝒏𝒏𝒆𝒍', url="t.me/MoviezAddaKA")
                       ],[
                          InlineKeyboardButton("🧑‍💻 𝑩𝒐𝒕 𝑪𝒓𝒆𝒂𝒕𝒆𝒓", url="t.me/kmadminsbot")
                         ]
                        ]
                    )
    await message.reply(f"<b> ⭐ ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴs ᴛᴏ ᴊᴏɪɴ ᴜꜱ ⭐</b>\n\n", reply_markup=reply_markup, disable_web_page_preview = True)



@Bot.on_message(filters.command('stats') & filters.user(ADMINS))
async def stats(bot: Bot, message: Message):
    now = datetime.now()
    delta = now - bot.uptime
    time = get_readable_time(delta.seconds)
    await message.reply(BOT_STATS_TEXT.format(uptime=time))


@Bot.on_message(filters.private)
async def useless(_,message: Message):
    if USER_REPLY_TEXT:
        await message.reply(USER_REPLY_TEXT)
