from Userbot import *

__MODULES__ = "Font"


def help_string(org):
    return h_s(org, "help_font")


@ky.ubot("font")
async def _(client: nlx, message, _):
    em = Emojik(client)
    em.initialize()
    if message.reply_to_message:
        if message.reply_to_message.text:
            query = message.reply_to_message.text
            udB.set_var(client.me.id, "gens_font", query)
        else:
            return await message.reply(f"{em.gagal} Please reply to text")
    else:
        if len(message.command) < 2:
            return await message.reply(f"{message.text} [reply/teks]")
        else:
            query = client.get_arg(message)
            udB.set_var(client.me.id, "gens_font", query)
    try:
        x = await client.get_inline_bot_results(bot_username, f"get_font {query}")
        return await message.reply_inline_bot_result(x.query_id, x.results[0].id)
    except Exception as error:
        return await message.reply(str(error))
