import asyncio
import datetime
from AnonXMusic import app
from AnonXMusic.utils.database import get_served_chats
from config import LOGGER_ID
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

AUTO_GCASTS = True
AUTO_GCAST = True
START_IMG_URLS = "https://graph.org/file/58e9ada3e0cbae2268306.jpg"

MESSAGES = f"""➜ α мυѕιᴄ ρℓαуєʀ вσт ωιтн ѕσмє α∂ναиᴄє∂ fєαтυʀєѕ

➻ ᴅɪsᴄᴏᴠᴇʀ ᴀ ᴡᴏʀʟᴅ ᴏғ ᴇɴᴅʟᴇss ᴍᴜsɪᴄ ᴘᴏssɪʙɪʟɪᴛɪᴇs ᴡɪᴛʜ ˹Yukki ꭙ ᴍᴜsɪᴄ˼ ᴛʜᴇ ᴜʟᴛɪᴍᴀᴛᴇ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴜsɪᴄ ʙᴏᴛ ᴡɪᴛʜ sᴏᴍᴇ ᴀᴡᴇsᴏᴍᴇ ғᴇᴀᴛᴜʀᴇs.

• ᴘʀᴏᴍᴏᴛɪᴏɴ / ᴀᴅs ғʀᴇᴇ ʙᴏᴛ.
• 24 ʜʀ ᴜᴘᴛɪᴍᴇ.
• ʟᴀɢ ғʀᴇᴇ sᴍᴏᴏᴛʜ ᴍᴜsɪᴄ ᴇxᴘᴇʀɪᴇɴᴄᴇ.

ᴀᴅᴅ @Yukkisongbot ɴᴏᴡ ᴀɴᴅ ʟᴇᴛ ᴛʜᴇ ᴍᴜsɪᴄ ᴛᴀᴋᴇ ᴏᴠᴇʀ ʏᴏᴜʀ ᴡᴏʀʟᴅ!"""


BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("𝙰𝚍𝚍 𝙼𝚎", url=f"https://t.me/YukkiSongBot?startgroup=true")
        ]
    ]
)



TEXT = """ᴀᴜᴛᴏ ɢᴄᴀsᴛ ɪs ᴇɴᴀʙʟᴇᴅ sᴏ ᴀᴜᴛᴏ ɢᴄᴀsᴛ/ʙʀᴏᴀᴅᴄᴀsᴛ ɪs ᴅᴏɪɴ ɪɴ ᴀʟʟ ᴄʜᴀᴛs ᴄᴏɴᴛɪɴᴜᴏᴜsʟʏ. \nɪᴛ ᴄᴀɴ ʙᴇ sᴛᴏᴘᴘᴇᴅ ʙʏ ᴘᴜᴛ ᴠᴀʀɪᴀʙʟᴇ [ᴀᴜᴛᴏ_ɢᴄᴀsᴛ = (ᴋᴇᴇᴘ ʙʟᴀɴᴋ & ᴅᴏɴᴛ ᴡʀɪᴛᴇ ᴀɴʏᴛʜɪɴɢ)]"""

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
            if isinstance(chat_id, int):  # Check if chat_id is an integer
                try:
                    await app.send_photo(chat_id, photo=START_IMG_URLS, caption=MESSAGES, reply_markup=BUTTONS)
                    await asyncio.sleep(20)  # Sleep for 100 second between sending messages
                except Exception as e:
                    pass  # Do nothing if an error occurs while sending message
    except Exception as e:
        pass  # Do nothing if an error occurs while fetching served chats

async def continuous_broadcast():
    await send_text_once()  # Send TEXT once when bot starts

    while True:
        if AUTO_GCAST:
            try:
                await send_message_to_chats()
            except Exception as e:
                pass

        # Wait for 100000 seconds before next broadcast
        await asyncio.sleep(100000)

# Start the continuous broadcast loop if AUTO_GCAST is True
if AUTO_GCAST:  
    asyncio.create_task(continuous_broadcast())
