import asyncio
import datetime
from pyrogram.errors import FloodWait
from AnonXMusic import app
from AnonXMusic.utils.database import get_served_chats, get_served_users
from config import LOGGER_ID
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

AUTO_GCASTS = True
AUTO_GCAST = True
START_IMG_URLS = "https://graph.org/file/497d715b03115857db6d8.jpg"

MESSAGES = f"""‣  тнιѕ ιѕ {app.mention}

➜ α мυѕιᴄ ρℓαуєʀ вσт ωιтн ѕσмє α∂ναиᴄє∂ fєαтυʀєѕ."""


BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton("𝙰𝚍𝚍 𝙼𝚎", url=f"https://t.me/{app.mention}?startgroup=true")]])



TEXT = """ᴀᴜᴛᴏ ɢᴄᴀsᴛ ɪs ᴇɴᴀʙʟᴇᴅ sᴏ ᴀᴜᴛᴏ ɢᴄᴀsᴛ/ʙʀᴏᴀᴅᴄᴀsᴛ ɪs ᴅᴏɪɴ ɪɴ ᴀʟʟ ᴄʜᴀᴛs ᴄᴏɴᴛɪɴᴜᴏᴜsʟʏ."""

STICKER = "CAACAgUAAx0Ceb8wGwABAT6gZmjvohZ8mXC467d5eduIKVjcdqQAAlkFAAKPzQFXFqDoXf0tCBAeBA"
async def send_text_once():
    try:
        await app.send_message(LOGGER_ID, TEXT)
    except Exception as e:
        pass

async def send_message_to_chats():
    try:
        chats = await get_served_chats()

        for chat_info in chats:
            chat_id = chat_info.get('chat_id')
            if isinstance(chat_id, int): 
                try:
                    await app.send_sticker(chat_id, STICKER, reply_markup=BUTTONS)

                except FloodWait as e:
                    await asyncio.sleep(e.value)
                except Exception:
                    pass 
    except Exception:
        pass 

async def send_message_to_users():
    users = await get_served_users()
    served_users = [int(user["user_id"]) for user in users]
    try:
        for chat_id in served_users:
            try:
                await app.send_sticker(chat_id, STICKER, reply_markup=BUTTONS)
            except FloodWait as e:
                await asyncio.sleep(e.value)
            except Exception as e:
                pass
    except Exception as e:
        pass

async def continuous_broadcast():
    await send_text_once()

    while True:
        if AUTO_GCAST:
            try:
                await send_message_to_chats()
            except Exception:
                pass

            try:
                await send_message_to_users()
            except Exception:
                pass
        await asyncio.sleep(100000)

if AUTO_GCAST:  
    asyncio.create_task(continuous_broadcast())
