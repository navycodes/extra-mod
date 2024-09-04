# Ayiin - Userbot
# Copyright (C) 2022-2023 @AyiinXd
#
# This file is a part of < https://github.com/AyiinXd/Ayiin-Userbot >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/AyiinXd/Ayiin-Userbot/blob/main/LICENSE/>.
#
# FROM Ayiin-Userbot <https://github.com/AyiinXd/Ayiin-Userbot>
# t.me/AyiinXdSupport & t.me/AyiinSupport

import asyncio

from pyrogram import *
from Userbot import *


# Create by myself @AyiinXd


# Create by myself @AyiinXd


@ky.ubot("semangat")
async def _(c: nlx, m, _):
    uputt = await m.reply(
        "**Apapun Yang Terjadi...**", reply_to_message_id=ReplyCheck(m)
    )
    await asyncio.sleep(1.8)
    await uputt.edit("**Tetaplah Bernafas...**")
    await asyncio.sleep(1.8)
    return await uputt.edit("**Dan Bersyukur...**")


# Create by myself @AyiinXd


@ky.ubot("mengeluh")
async def _(c: nlx, m, _):
    uputt = await m.reply(
        "**Apapun Yang Terjadi...**", reply_to_message_id=ReplyCheck(m)
    )
    await asyncio.sleep(1.8)
    await uputt.edit("**Tetaplah Mengeluh...**")
    await asyncio.sleep(1.8)
    return await uputt.edit("**Dan Putus Asa...**")


# Create by myself @AyiinXd
