import asyncio
import os

from pyrogram.errors import *
from pyrogram.file_id import *
from pyrogram.raw.functions.messages import *
from pyrogram.raw.functions.stickers import *
from pyrogram.raw.types import *

from Userbot import *

__MODULES__ = "Sticker"


def help_string(org):
    return h_s(org, "help_sticker")


@ky.ubot("gstik|getstiker|getsticker")
async def _(c: nlx, m, _):
    em = Emojik(c)
    em.initialize()
    rep = m.reply_to_message
    stick = rep.sticker
    if not rep:
        await m.reply(_("st_1").format(em.gagal))
        return
    else:
        if stick.is_video == True:
            pat = await c.download_media(stick, file_name=f"{stick.set_name}.mp4")
            await rep.reply_document(
                document=pat,
                caption=_("st_2").format(
                    em.sukses, stick.emoji, em.alive, stick.file_id
                ),
            )
        elif stick.is_animated == True:
            await m.reply(_("st_1").format(em.gagal))
            return

        else:
            pat = await c.download_media(stick, file_name=f"{stick.set_name}.png")
            await rep.reply_document(
                document=pat,
                caption=_("st_2").format(
                    em.sukses, stick.emoji, em.alive, stick.file_id
                ),
            )
        return
    os.remove(pat)
    return


@ky.ubot("unkang")
async def _(self: nlx, m, _):
    em = Emojik(self)
    em.initialize()
    rep = m.reply_to_message
    await self.unblock_user(bot_username)
    if not rep:
        await m.reply(_("st_3").format(em.gagal))
        return
    if rep.sticker:
        pros = await m.reply(_("proses").format(em.proses))
        ai = await self.forward_messages(bot_username, m.chat.id, message_ids=rep.id)
        await self.send_message(bot_username, "/unkang", reply_to_message_id=ai.id)
        await asyncio.sleep(0.5)
        if await resleting(self, m) == "Stiker berhasil dihapus dari paket Anda.":
            await pros.edit(_("st_4").format(em.sukses))
            return
        else:
            await pros.edit(_("st_5").format(em.gagal))
            return
    else:
        return await m.reply(_("st_6").format(em.gagal))


@ky.ubot("kang")
async def _(self: nlx, m, _):
    em = Emojik(self)
    em.initialize()
    rep = m.reply_to_message
    cekemo = self.get_arg(m)
    await self.unblock_user(bot_username)
    if not rep:
        await m.reply(_("st_7").format(em.gagal))
        return
    await self.send_message(bot_username, "/kang")
    pros = await m.reply(_("proses").format(em.proses))
    if len(m.command) == 2:
        ai = await self.forward_messages(bot_username, m.chat.id, message_ids=rep.id)
        await self.send_message(
            bot_username, f"/kang {cekemo}", reply_to_message_id=ai.id
        )
        await asyncio.sleep(5)
        async for tai in self.search_messages(
            bot_username, query="Sticker Anda Berhasil Dibuat!", limit=1
        ):
            await asyncio.sleep(5)
            await tai.copy(m.chat.id)
    else:
        ai = await self.forward_messages(bot_username, m.chat.id, message_ids=rep.id)
        await self.send_message(bot_username, "/kang", reply_to_message_id=ai.id)
        await asyncio.sleep(5)
        async for tai in self.search_messages(
            bot_username, query="Sticker Anda Berhasil Dibuat!", limit=1
        ):
            await asyncio.sleep(5)
            await tai.copy(m.chat.id)
        await ai.delete()
        await pros.delete()
        ulat = await self.resolve_peer(bot_username)
        await self.invoke(DeleteHistory(peer=ulat, max_id=0, revoke=False))
        return


async def resleting(self, m):
    return [x async for x in self.get_chat_history(bot_username, limit=1)][0].text
