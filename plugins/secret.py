from Userbot import *

__MODULES__ = "SecretMsg"


def help_string(org):
    return h_s(org, "help_secret")


@ky.ubot("msg")
async def msg_cmd(client, message, _):
    if not message.reply_to_message:
        return await message.reply(
            f"<code>{message.text}</code> [balas pesan pengguna - text]"
        )
    text = f"secret {id(message)}"
    await message.delete()
    x = await client.get_inline_bot_results(bot.me.username, text)
    return await message.reply_to_message.reply_inline_bot_result(
        x.query_id, x.results[0].id
    )
