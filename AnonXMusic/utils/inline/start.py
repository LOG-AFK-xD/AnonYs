from pyrogram.types import InlineKeyboardButton

import config
from AnonXMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="✚ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ ✚",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="🗒 Hᴇʟᴘ 🔧", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="📨 Cʜᴀɴɴᴇʟ", url=config.SUPPORT_CHANNEL
            ),
            InlineKeyboardButton(
                text="Mᴀɪɴᴛᴀɪɴᴇʀ 👤", user_id=config.OWNER_ID
            )
        ],
        [
            InlineKeyboardButton(
                text="💁‍♀ Cʜᴀᴛᴛɪɴɢ Hᴜʙ 👨‍🎨", url=config.SUPPORT_GROUP
            )
        ],
     ]
    return buttons
