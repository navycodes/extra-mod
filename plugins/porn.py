from Userbot import *

__MODULES__ = "Porn"

flood = {}


def help_string(org):
    return h_s(org, "help_porn")


def flood_bokep(org):
    trial = udB.get_list_from_var(bot.me.id, "flood_bokep", "user")
    if org in trial:
        return True
    return False


@ky.ubot("pornhub|xnxx|xvideos")
async def _(c: nlx, m, _):
    em = Emojik(c)
    em.initialize()
    if len(m.command) < 2 and not m.reply_to_message:
        return await m.reply(
            f"{em.gagal} <b>Gunakan format contoh: `{m.text.split()[0]} big tits`"
        )
    floodga = flood_bokep(c.me.id)
    if floodga:
        return await m.reply_text(
            f"<b>{em.gagal} Limit mencapai batas!! Silahkan coba lagi besok atau hubungi @kenapanan untuk membuka limit</b>"
        )
    if int(c.me.id) in flood:
        flood[int(c.me.id)] += 1
    else:
        flood[int(c.me.id)] = 1
    if flood[int(c.me.id)] > 5:
        # del flood[int(c.me.id)]
        if c.me.id not in the_cegers:
            udB.add_to_var(c.me.id, "flood_bokep", c.me.id, "user")
            return await m.reply_text(
                f"<b>{em.gagal} Limit mencapai batas!! Silahkan coba lagi besok atau hubungi @kenapanan untuk membuka limit</b>"
            )
    xnxx = {"_id": c.me.id, "args": c.get_arg(m)}
    udB.set_var(c.me.id, "bokep", xnxx)
    cmd = m.command[0]
    x = await c.get_inline_bot_results(bot_username, f"bokep {cmd}")
    await m.reply_inline_bot_result(x.query_id, x.results[0].id)
