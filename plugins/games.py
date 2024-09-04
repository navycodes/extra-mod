from Userbot import *

__MODULES__ = "Games"


def help_string(org):
    return h_s(org, "help_games")


@ky.ubot("catur")
async def _(c, m, _):
    try:
        x = await c.get_inline_bot_results("GameFactoryBot")
        msg = m.reply_to_message or m
        return await c.send_inline_bot_result(
            m.chat.id, x.query_id, x.results[0].id, reply_to_message_id=msg.id
        )

    except Exception as error:
        return await m.reply(error)


@ky.ubot("dice")
async def _(c, m, _):
    await c.send_dice(m.chat.id, "🎲")
    return await m.delete()


@ky.ubot("dart")
async def _(c, m, _):
    await c.send_dice(m.chat.id, "🎯")
    return await m.delete()


@ky.ubot("basket")
async def _(c, m, _):
    await c.send_dice(m.chat.id, "🏀")
    return await m.delete()


@ky.ubot("bowling")
async def _(c, m, _):
    await c.send_dice(m.chat.id, "🎳")
    return await m.delete()


@ky.ubot("football")
async def _(c, m, _):
    await c.send_dice(m.chat.id, "⚽")
    return await m.delete()


@ky.ubot("slot")
async def _(c, m, _):
    await c.send_dice(m.chat.id, "🎰")
    return await m.delete()
