################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################



from telegraph.aio import Telegraph
from Userbot import Emojik, fetch, h_s, ky, nlx, bot

__MODULES__ = "Telegraph"


def help_string(org):
    return h_s(org, "help_graph")


async def post_to_telegraph(is_media: bool, title=None, content=None, media=None):
    telegraph = Telegraph()
    if telegraph.get_access_token() is None:
        await telegraph.create_account(short_name=bot.me.username)
    if is_media:
        # Create a Telegram Post Foto/Video
        response = await telegraph.upload_file(media)
        return f"https://img.yasirweb.eu.org{response[0]['src']}"
    # Create a Telegram Post using HTML Content
    response = await telegraph.create_page(
        title,
        html_content=content,
        author_url=f"https://t.me/{bot.me.username}",
        author_name=bot.me.username,
    )
    return f"https://graph.org/{response['path']}"


async def upload_media(m):
    media = await m.reply_to_message.download()
    url = "https://itzpire.com/tools/upload"
    with open(media, "rb") as file:
        files = {"file": file}
        response = await fetch.post(url, files=files)
    if response.status_code == 200:
        data = response.json()
        link = data["fileInfo"]["url"]
        return link
    else:
        return f"{response.text}"


@ky.ubot("tg")
async def _(client: nlx, message, _):
    emo = Emojik(client)
    emo.initialize()
    XD = await message.reply(_("proses").format(emo.proses))
    if not message.reply_to_message:
        return await XD.edit(_("grp_1").format(emo.gagal))
    if message.reply_to_message.text:
        page_title = f"{client.me.first_name} {client.me.last_name or ''}"
        page_text = message.reply_to_message.text
        page_text = page_text.replace("\n", "<br>")
        try:
            url = await post_to_telegraph(False, page_title, page_text)
        except Exception as exc:
            return await XD.edit(_("err").format(emo.gagal, exc))
        return await XD.edit("{} **Successfully Uploaded: <a href='{}'>Click Here</a>**".format(emo.sukses, url), disable_web_page_preview=True,
        )
    else:
        try:
            url = await upload_media(message)
        except Exception as exc:
            return await XD.edit(_("err").format(emo.gagal, exc))
        return await XD.edit("{} **Successfully Uploaded: <a href='{}'>Click Here</a>**".format(emo.sukses, url), disable_web_page_preview=True,
        )


@ky.ubot("upload|upl")
async def _(client: nlx, message, _):
    emo = Emojik(client)
    emo.initialize()
    XD = await message.reply(_("proses").format(emo.proses))
    rep = message.reply_to_message
    if not rep:
        return await XD.edit(_("grp_1").format(emo.gagal))
    try:
        url = await upload_media(message)
    except Exception as exc:
        return await XD.edit(_("err").format(emo.gagal, exc))
    return await XD.edit("{} **Successfully Uploaded: <a href='{}'>Click Here</a>**".format(emo.sukses, url), disable_web_page_preview=True,
        )
