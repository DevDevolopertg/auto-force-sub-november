#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from bot import Translation # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error
from pyrogram.errors import UserNotParticipant
from bot import FORCESUB_CHANNEL

db = Database()

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    if not await db.is_user_exist(update.from_user.id):
        await db.add_user(update.from_user.id)
    update_channel = -1001170149779
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    if file_uid:
        try:
            user = await bot.get_chat_member(update_channel, update.chat.id)
            if user.status == "kicked":
               await update.reply_text("🤭 Sorry Dude, You are B A N N E D 🤣🤣🤣")
               return
        except UserNotParticipant:
            try:
                file_uid = update.command[1]
            except IndexError:
                file_uid = False
            if file_uid:
                showbtns=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(text="📒 Join Our Channel 📒", url=f"https://t.me/joinchat/g09xn9Slq4Q2NmFl"),
                        ],
                        [
                            InlineKeyboardButton(text="♀️ Try Again ♀️", url= f"https://t.me/Cv_Filteritver3Bot?start={file_uid}")
                        ]

                    ]
                )
            else:
                showbtns=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(text="📒 Join Our Channel 📒", url=f"https://t.me/joinchat/g09xn9Slq4Q2NmFl")
                        ]
                    ]
                )
            #await update.reply_text(f"Join @{update_channel} To Use Me")
            await update.reply_text(
                text="⚠️ 𝑹𝑬𝑨𝑫 & 𝑭𝑶𝑳𝑳𝑶𝑾 𝑰𝑵𝑺𝑻𝑹𝑼𝑪𝑻𝑰𝑶𝑵\n\n<b>𝑯𝒆𝒚 𝑩𝒓𝒐 👋</b> <b>സിനിമവില്ല</b> <i>ഗ്രൂപ്പിൽ നിങ്ങൾ ചോദിക്കുന്ന സിനിമകൾ ലഭിക്കണം എന്നുണ്ടെങ്കിൽ നിങ്ങൾ താഴെ കൊടുത്തിട്ടുള്ള</b> <b>Join Our Channel</b> <i>എന്ന ബട്ടൺ മുഖേന ചാനലിൽ ജോയിൻ ചെയ്യണം. ജോയിൻ ചെയിത ശേഷം വീണ്ടും ഇവിടെ വന്ന്</i> <b>Try Again</b> <i>എന്ന ബട്ടണിൽ അമർത്തി താഴെ കാണുന്ന</i> <b>Start</b> <i>അമർത്തിയാൽ നിങ്ങൾക്ക് ഞാൻ ആ സിനിമ അയച്ചു തരുന്നതാണ്..!!💯</i>\n\n<i>🔊In Order To Get The Movie Requested By You in Our Groups, You Will Have To</i> <b>Join Our Official Channel</b> <i>First Through the Button . After That, Click on the</i> <b>Try Again</b> Button below. I'll Send You That Movie 🙈\n\n<b><a href=https://t.me/CinemaVilla_HD/20 >⚠️ മനസിലാകാത്തവർ ഇവിടെ ക്ലിക്ക് ചെയ്യുക❓</a></b>\n\n<b>👇 𝑱𝑶𝑰𝑵 𝑻𝑯𝑰𝑺 𝑪𝑯𝑨𝑵𝑵𝑬𝑳 & 𝑻𝑹𝒀 👇</b>",
                reply_markup=showbtns,
                disable_web_page_preview=True
            )
            return
    
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        
        caption = f"<b>{file_name}</b>\n\n<b>♻️ 𝙅𝙊𝙄𝙉 :- https://t.me/joinchat/IA_lkRsv0Z5jZjQ1</b>"
        
        if file_type == "document":
        
            await bot.send_document(
                chat_id=update.chat.id,
                document = file_id,
                caption = caption,
                parse_mode="html",
                reply_to_message_id=update.message_id,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '✅ Join Our Channel', url="https://t.me/joinchat/IA_lkRsv0Z5jZjQ1"
                                )
                        ]
                    ]
                )
            )

        elif file_type == "video":
        
            await bot.send_video(
                chat_id=update.chat.id,
                video = file_id,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '✅ Join Our Channel', url="https://t.me/joinchat/IA_lkRsv0Z5jZjQ1"
                                )
                        ]
                    ]
                )
            )
            
        elif file_type == "audio":
        
            await bot.send_audio(
                chat_id=update.chat.id,
                audio = file_id,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '✅ Join Our Channel', url="https://t.me/joinchat/IA_lkRsv0Z5jZjQ1"
                                )
                        ]
                    ]
                )
            )

        else:
            print(file_type)
        
        return

    buttons = [[
        InlineKeyboardButton('Main Group', url='https://t.me/cenimavilla1999'),
        InlineKeyboardButton('Main Channel', url ='https://t.me/joinchat/g09xn9Slq4Q2NmFl')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(
                update.from_user.first_name),
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('Home ', callback_data='start'),
        InlineKeyboardButton('About', callback_data='about')
    ],[
        InlineKeyboardButton('Close', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
        InlineKeyboardButton('Home ', callback_data='start'),
        InlineKeyboardButton('Close', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )
