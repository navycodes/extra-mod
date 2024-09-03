from Userbot import *

__MODULES__ = "Afk"


def help_string(org):
    return h_s(org, "help_afk")


@ky.ubot("afk")
async def _(client: nlx, message, _):
    reason = client.get_arg(message)
    afk_handler = AFK_(client, message, reason)
    return await afk_handler.set_afk()


@ky.nocmd("AFK", nlx)
@capture_err
#@manage_handlers
async def _(client, message, _):
    afk_handler = AFK_(client, message)
    return await afk_handler.get_afk()


@ky.ubot("unafk")
async def _(client, message, _):
    afk_handler = AFK_(client, message)
    return await afk_handler.unset_afk()
