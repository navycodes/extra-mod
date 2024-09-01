################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV || Gojo_Satoru
"""
################################################################

from pyrogram.enums import *
from pyrogram.types import *

from Userbot import *

__MODULES__ = "Markdown"


def help_string(org):
    # return h_s(org, "help_mark")
    return (org, "Markdown")


@ky.ubot("markdown")
async def _(c: nlx, m, _):
    try:
        xi = await c.get_inline_bot_results(bot_username, "mark_in")
        await m.delete()
        await c.send_inline_bot_result(
            m.chat.id, xi.query_id, xi.results[0].id, reply_to_message_id=ReplyCheck(m)
        )
        return
    except Exception as e:
        await m.edit(f"{e}")
        return
