from Userbot import *
from Userbot.assistant.spotify import download_spot

__MODULES__ = "Spotify"


def help_string(org):
    return h_s(org, "help_porn")


@ky.ubot("spotify|sptf")
async def _(c: nlx, m, _):
    em = Emojik(c)
    em.initialize()
    pros = await m.reply(_("proses").format(em.proses))
    if len(m.command) == 3:
        if m.command[1] == "-dl":
            query = m.command[2]
            if len(m.command) < 3 or not query.startswith("https"):
                await m.reply(
                    "{} Gunakan format `{}` -dl url".format(em.gagal, m.text.split()[0])
                )
                return await pros.delete()
            await download_spot(c, m, query)
            return await pros.delete()
        else:
            await m.reply(
                "{} Gunakan format `{}` -dl url".format(em.gagal, m.text.split()[0])
            )
            return await pros.delete()
    else:
        xk = {"_id": c.me.id, "args": c.get_arg(m)}
        udB.set_var(c.me.id, "spot", xk)
        cmd = m.command[1]
        if m.command[1] == "-dl":
            await m.reply(
                "{} Gunakan format `{}` Judul lagu".format(em.gagal, m.text.split()[0])
            )
            return await pros.delete()
        print(cmd)
        x = await c.get_inline_bot_results(bot_username, f"src_spot {cmd}")
        await m.reply_inline_bot_result(x.query_id, x.results[0].id)
        # return await pros.delete()
