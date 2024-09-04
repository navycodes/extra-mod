################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################

import asyncio

from config import NO_GCAST
from pyrogram.errors import *
from Userbot import *

dispam = []

berenti = False

__MODULES__ = "Spam"


def help_string(org):
    return h_s(org, "help_spam")


@ky.ubot("spam")
async def _(c: nlx, m, _):
    em = Emojik(c)
    em.initialize()
    global berenti
    if m.chat.id in NO_GCAST:
        return await m.reply("ANAK KONTOL MALAH MAU SPAM DIGC SUPPORT GOBLOK")
    reply = m.reply_to_message
    berenti = True

    if reply:
        try:
            count_message = int(m.command[1])
            for i in range(count_message):
                if not berenti:
                    break
                await reply.copy(m.chat.id)
                await asyncio.sleep(0.1)
        except Exception as error:
            return await m.reply(str(error))
    else:
        if len(m.command) < 2:
            return await m.reply(_("spm_1").format(em.gagal, m.text.split()[1]))
        else:
            try:
                count_message = int(m.command[1])
                for i in range(count_message):
                    if not berenti:
                        break
                    await m.reply(
                        m.text.split(None, 2)[2],
                    )
                    await asyncio.sleep(0.1)
            except Exception as error:
                return await m.reply(str(error))
    berenti = False
    return await m.delete()


@ky.ubot("dspam")
async def _(c: nlx, m, _):
    em = Emojik(c)
    em.initialize()
    global berenti

    reply = m.reply_to_message
    if m.chat.id in NO_GCAST:

        return await m.reply("ANAK KONTOL MALAH MAU SPAM DIGC SUPPORT GOBLOK")
    berenti = True
    if reply:
        try:
            count_message = int(m.command[1])
            count_delay = int(m.command[2])
        except Exception as error:
            return await m.reply(str(error))
        for i in range(count_message):
            if not berenti:
                break
            try:
                await reply.copy(m.chat.id)
                await asyncio.sleep(count_delay)
            except SlowmodeWait as e:
                await asyncio.sleep(e.value)
                await reply.copy(m.chat.id)
                await asyncio.sleep(count_delay)
            except FloodWait as e:
                await asyncio.sleep(e.value)
                await reply.copy(m.chat.id)
                await asyncio.sleep(count_delay)
    else:
        if len(m.command) < 4:
            return await m.reply(_("spm_2").format(em.gagal, m.text.split()[1]))
        else:
            try:
                count_message = int(m.command[1])
                count_delay = int(m.command[2])
            except Exception as error:
                return await m.reply(str(error))
            for i in range(count_message):
                if not berenti:
                    break
                try:
                    await m.reply(m.text.split(None, 3)[3])
                    await asyncio.sleep(count_delay)
                except SlowmodeWait as e:
                    await asyncio.sleep(e.value)
                    await m.reply(m.text.split(None, 3)[3])
                    await asyncio.sleep(count_delay)
                except FloodWait as e:
                    await asyncio.sleep(e.value)
                    await m.reply(m.text.split(None, 3)[3])
                    await asyncio.sleep(count_delay)
    berenti = False
    return await m.delete()


@ky.ubot("cspam")
async def _(c: nlx, m, _):
    em = Emojik(c)
    em.initialize()
    global berenti
    if not berenti:
        return await m.reply(_("spm_3").format(em.gagal))
    berenti = False
    return await m.reply(_("spm_4").format(em.sukses))


@ky.ubot("bcfw")
async def _(c: nlx, message, _):
    em = Emojik(c)
    em.initialize()
    global berenti
    list_gc = udB.get_list_from_var(c.me.id, "db_spam", "grup")
    if not list_gc:
        return await message.reply(
            f"{em.gagal} ANAK KONTOL MAU SPAM TAPI LIST GC KOSONG!!"
        )
    proses = await message.reply(_("proses").format(em.proses))
    berenti = True

    try:
        ani, count_str, delay_str, link = message.text.split(maxsplit=3)
        count = int(count_str)
        delay = int(delay_str)
    except ValueError:
        return await proses.edit(_("spm_5").format(em.gagal, message.text.split()[1]))
    chat_id, message_id = link.split("/")[-2:]
    try:
        chat_id = int(chat_id)
    except ValueError:
        pass

    message_id = int(message_id)

    for ani in range(count):
        for gc in list_gc:
            try:
                if not berenti:
                    break
                await c.get_messages(chat_id, message_id)
                await c.forward_messages(gc, chat_id, message_ids=message_id)
                await asyncio.sleep(delay)
            except Exception as e:
                if (
                    "CHAT_SEND_PHOTOS_FORBIDDEN" in str(e)
                    or "CHAT_SEND_MEDIA_FORBIDDEN" in str(e)
                    or "USER_RESTRICTED" in str(e)
                ):
                    await message.reply(_("spm_6").format(em.gagal))
                else:
                    await message.reply(_("err").format(em.gagal, e))
                break
    berenti = False
    await message.delete()
    return await proses.delete()


@ky.ubot("addfw")
async def _(c: nlx, m, _):
    em = Emojik(c)
    em.initialize()
    pp = await m.reply(_("proses").format(em.proses))
    chat_id = m.command[1] if len(m.command) > 1 else m.chat.id
    if "/+" in str(chat_id):
        gid = await client.get_chat(str(chat_id))
        chat_id = int(gid.id)
    elif "t.me/" in str(chat_id) or "@" in str(chat_id):
        chat_id = chat_id.replace("https://t.me/", "")
        gid = await client.get_chat(str(chat_id))
        chat_id = int(gid.id)
    else:
        chat_id = int(chat_id)
    if chat_id in NO_GCAST:
        return await m.delete()
    blacklist = udB.get_list_from_var(c.me.id, "db_spam", "grup")
    try:
        chat = await c.get_chat(chat_id)
    except:
        chat = "Private "
    if chat_id in blacklist:
        return await pp.edit(_("gcs_4").format(em.sukses))
    udB.add_to_var(c.me.id, "db_spam", chat_id, "grup")
    return await pp.edit(_("gcs_5").format(em.sukses, chat_id, chat.title))


@ky.ubot("delfw")
async def _(c: nlx, m, _):
    em = Emojik(c)
    em.initialize()
    pp = await m.reply(_("proses").format(em.proses))
    try:
        if not c.get_arg(m):
            chat_id = m.chat.id
        else:
            chat_id = int(m.command[1])
        blacklist = udB.get_list_from_var(c.me.id, "db_spam", "grup")
        if chat_id not in blacklist:
            return await pp.edit(_("gcs_7").format(em.gagal, chat_id))
        udB.remove_from_var(c.me.id, "db_spam", chat_id, "grup")
        return await pp.edit(_("gcs_8").format(em.sukses, chat_id))

    except Exception as error:
        return await pp.edit(str(error))


@ky.ubot("listfw")
async def _(c: nlx, m, _):
    em = Emojik(c)
    em.initialize()
    pp = await m.reply(_("proses").format(em.proses))

    msg = "<b>{} List Group Spam FW</b>\n\n".format(em.sukses)
    listbc = udB.get_list_from_var(c.me.id, "db_spam", "grup")
    for x in listbc:
        try:
            get = await c.get_chat(x)
            msg += _("gcs_11").format(get.title, get.id)
        except:
            msg += _("gcs_12").format(x)
    await pp.delete()
    return await m.reply(msg)


@ky.ubot("clearfw")
async def _(c: nlx, m, _):
    em = Emojik(c)
    em.initialize()
    msg = await m.reply(_("proses").format(em.proses))
    get_bls = udB.get_list_from_var(c.me.id, "db_spam", "grup")
    if not get_bls:
        # if len(get_bls) == 0:
        return await msg.edit(_("gcs_13").format(em.gagal))
    for x in get_bls:
        udB.remove_from_var(c.me.id, "db_spam", x, "grup")
    return await msg.edit(_("gcs_14").format(em.sukses))


@ky.ubot("dspamfw")
async def _(c: nlx, message, _):
    em = Emojik(c)
    em.initialize()
    global berenti
    if message.chat.id in NO_GCAST:
        for x in the_cegers:
            if c.me.id == x:
                continue
            else:
                return await message.reply(
                    "ANAK KONTOL MALAH MAU SPAM DIGC SUPPORT GOBLOK"
                )

    proses = await message.reply(_("proses").format(em.proses))
    berenti = True

    try:
        _, count_str, delay_str, link = message.text.split(maxsplit=3)
        count = int(count_str)
        delay = int(delay_str)
    except ValueError:
        return await proses.edit(_("spm_5").format(em.gagal, message.command))

    chat_id, message_id = link.split("/")[-2:]

    try:
        chat_id = int(chat_id)
    except ValueError:
        pass

    message_id = int(message_id)

    for _ in range(count):
        try:
            if not berenti:
                break
            await c.get_messages(chat_id, message_id)
            await c.forward_messages(message.chat.id, chat_id, message_ids=message_id)
            await asyncio.sleep(delay)
        except Exception as e:
            if (
                "CHAT_SEND_PHOTOS_FORBIDDEN" in str(e)
                or "CHAT_SEND_MEDIA_FORBIDDEN" in str(e)
                or "USER_RESTRICTED" in str(e)
            ):
                await message.reply(_("spm_6").format(em.gagal))
            else:
                await proses.reply(_("err").format(em.gagal, e))
            break
    berenti = False
    await message.delete()
    return await proses.delete()
