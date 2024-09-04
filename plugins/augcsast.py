import asyncio
import random

from pyrogram.enums import ChatType
from pyrogram.errors import FloodWait
from Userbot import *
from Userbot.plugins.limit import spam_bot

__MODULES__ = "AutoGcast"


def help_string(org):
    return h_s(org, "help_augcs")


AG = []
LT = []


def extract_type_and_text(m):
    args = m.text.split(None, 2)
    if len(args) < 2:
        return None, None

    type = args[1]
    msg = (
        m.reply_to_message.text
        if m.reply_to_message
        else args[2] if len(args) > 2 else None
    )
    return type, msg


@ky.ubot("autogcast")
async def _(c, m, _):
    em = Emojik(c)
    em.initialize()
    """
    CREATE BY: NORSODIKIN.T.ME
    REQUEST BY: MYMASKY.T.ME
    """
    msg = await m.reply(_("proses").format(em.proses))
    type, value = extract_type_and_text(m)
    auto_text_vars = dB.get_var(c.me.id, "AUTO_TEXT")
    if type == "on":
        if not auto_text_vars:
            return await msg.edit(_("augcs_1").format(em.gagal))
        if c.me.id not in AG:
            await msg.edit(_("augcs_2").format(em.sukses))
            AG.append(c.me.id)
            done = 0
            while c.me.id in AG:
                delay = dB.get_var(c.me.id, "DELAY_GCAST") or 1
                blacklist = dB.get_chat(c.me.id)
                txt = random.choice(auto_text_vars)

                group = 0
                async for dialog in c.get_dialogs():
                    if (
                        dialog.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP)
                        and dialog.chat.id not in blacklist
                        and dialog.chat.id not in NO_GCAST
                    ):
                        try:
                            await asyncio.sleep(1)
                            await c.send_message(
                                dialog.chat.id, f"{txt} {random.choice(range(999))}"
                            )
                            group += 1
                        except FloodWait as e:
                            await asyncio.sleep(e.value)
                            await c.send_message(
                                dialog.chat.id, f"{txt} {random.choice(range(999))}"
                            )
                            group += 1
                        except Exception:
                            pass

                if c.me.id not in AG:
                    return

                done += 1
                await msg.reply(_("augcs_3").format(em.sukses, done, group, delay))
                await asyncio.sleep(int(60 * int(delay)))
        else:
            return await msg.delete()

    elif type == "off":
        if c.me.id in AG:
            AG.remove(c.me.id)
            return await msg.edit(_("augcs_4").format(em.gagal))
        else:
            return await msg.delete()

    elif type == "add":
        if not value:
            return await msg.edit(
                f"{em.gagal} <b>Minimal kasih teks Tolol, buat pesan nya.</b>"
            )
        await add_auto_text(c, value)
        return await msg.edit(
            f"{em.sukses} <b>Teks :\n\n<code>{value}</code>\n\nDisimpan untuk pesan Auto Gcast.</b>"
        )

    elif type == "delay":
        dB.set_var(c.me.id, "DELAY_GCAST", value)
        return await msg.edit(
            f"{em.sukses} <b>Delay Auto Gcast diatur ke : <code>{value}</code></b>"
        )

    elif type == "del":
        if not value:
            return await msg.edit(
                f"{em.gagal} <b>Minimal kasih angka Tolol, teks keberapa perlu dihapus.</b>"
            )
        if value == "all":
            dB.set_var(c.me.id, "AUTO_TEXT", [])
            return await msg.edit(
                f"{em.sukses} <b>Yosh semua teks alay lo udah dihapus.</b>"
            )
        try:
            value = int(value) - 1
            auto_text_vars.pop(value)
            dB.set_var(c.me.id, "AUTO_TEXT", auto_text_vars)
            return await msg.edit(
                f"{em.sukses} <b>Teks ke : <code>{value+1}</code> dihapus.</b>"
            )
        except Exception as error:
            return await msg.edit(str(error))

    elif type == "get":
        if not auto_text_vars:
            return await msg.edit(f"{em.gagal} <b>Teks Auto Gcast lo kosong bego.</b>")
        txt = "<b>Teks Gcast Alay Lo</b>\n\n"
        for num, x in enumerate(auto_text_vars, 1):
            txt += f"{num}: {x}\n\n"

        return await msg.edit(txt)

    elif type == "limit":
        if value == "off":
            if c.me.id in LT:
                LT.remove(c.me.id)
                return await msg.edit(f"{em.gagal} <b>Auto Limit dimatikan.</b>")
            else:
                return await msg.delete()

        elif value == "on":
            if c.me.id not in LT:
                LT.append(c.me.id)
                await msg.edit(f"{em.sukses} <b>Auto Limit dihidupkan.</b>")
                while c.me.id in LT:
                    for x in range(2):
                        await spam_bot(c, m, _)
                        await asyncio.sleep(5)
                    await asyncio.sleep(1200)
            else:
                return await msg.delete()
        else:
            return await msg.edit(
                f"{em.gagal} <b>Salah Goblok!! Minimal baca perintah bantuan lah.</b>"
            )
    else:
        return await msg.edit(
            f"{em.gagal} <b>Salah Goblok!! Minimal baca perintah bantuan lah.</b>"
        )
    return


async def add_auto_text(c, text):
    auto_text = dB.get_var(c.me.id, "AUTO_TEXT") or []
    auto_text.append(text)
    dB.set_var(c.me.id, "AUTO_TEXT", auto_text)
