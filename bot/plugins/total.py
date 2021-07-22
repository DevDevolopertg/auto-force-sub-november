import logging
logger = logging.getLogger(__name__)

import asyncio
import aiofiles
import aiofiles.os
import datetime
import traceback
import random
import string
import time
import os
from random import choice
from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import FloodWait, InputUserDeactivated, UserIsBlocked, PeerIdInvalid
from bot import OWNER_ID
from bot.database import Database

db = Database() 


@Client.on_message(filters.private & filters.command(["users"]))
async def sts(c, m):
    if m.from_user.id not in OWNER_ID:
        await c.delete_messages(
            chat_id=m.chat.id,
            message_ids=m.message_id,
            revoke=True
        )
        return
    total_users = await db.total_users_count()
    await m.reply_text(text=f"**Total Users in DB:** `{total_users}`", parse_mode="Markdown", quote=True)

