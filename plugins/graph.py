################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################


import os
from io import BytesIO

import requests
from PIL import Image
from pyrogram.enums import MessageMediaType
from Userbot import Emojik, h_s, ky, nlx
from ytelegraph import TelegraphAPI

__MODULES__ = "Telegraph"


def help_string(org):
    return h_s(org, "help_graph")


async def dl_thumbnail(client, message):
    if message.reply_to_message and message.reply_to_message.sticker:
        sticker = message.reply_to_message.sticker
        if sticker.thumbs:
            thumb_id = sticker.thumbs[0].file_id
            thumb_path = await client.download_media(thumb_id)

            # Konversi thumbnail ke format JPEG
            with Image.open(thumb_path) as img:
                img = img.convert("RGB")
                thumb_io = BytesIO()
                img.save(thumb_io, format="JPEG")
                thumb_io.seek(0)

            os.remove(thumb_path)
            return thumb_io, "image/jpeg"

    return await dl_pic(client, message.reply_to_message)


async def dl_pic(client, media):
    path = await client.download_media(media)
    mime_type = None

    if media.photo:
        mime_type = "image/jpeg"
    elif media.video:
        mime_type = "video/mp4"
    elif media.animation or media.sticker:
        mime_type = "image/gif"  # Anggap sebagai GIF jika animasi
    elif media.document:
        mime_type = "application/octet-stream"

    if not mime_type:
        return None, None

    with open(path, "rb") as f:
        content = f.read()

    os.remove(path)

    get_media = BytesIO(content)
    get_media.name = os.path.basename(path)

    return get_media, mime_type


@ky.ubot("tg")
async def _(client: nlx, message, _):
    emo = Emojik(client)
    emo.initialize()
    XD = await message.reply(_("proses").format(emo.proses))
    if not message.reply_to_message:
        return await XD.edit(_("grp_1").format(emo.gagal))
    telegraph = TelegraphAPI()
    if message.reply_to_message.media:
        try:
            media_type = message.reply_to_message.media
            media_data, mime_type = None, None

            if media_type == MessageMediaType.STICKER:
                media_data, mime_type = await dl_thumbnail(client, message)
            elif media_type in [
                MessageMediaType.PHOTO,
                MessageMediaType.VIDEO,
                MessageMediaType.ANIMATION,
                MessageMediaType.DOCUMENT,
            ]:
                media_data, mime_type = await dl_pic(client, message.reply_to_message)

            if media_data is None:
                await message.delete()
                return await XD.delete()

            media_data.seek(0)
            response = requests.post(
                "https://telegra.ph/upload",
                files={"file": ("file", media_data, mime_type)},
            ).json()

            if "error" in response:
                return await XD.edit(f"<code>{response['error']}</code>")

            media_url = response[0]["src"]
            page_content = [
                {"tag": "img", "attrs": {"src": f"https://telegra.ph{media_url}"}}
            ]
            if message.reply_to_message.caption:
                page_content.append(
                    {"tag": "p", "children": [message.reply_to_message.caption]}
                )
            page_title = f"{message.from_user.first_name} {message.from_user.last_name or ''}'s Media"
            media_page = telegraph.create_page(title=page_title, content=page_content)
            await XD.edit(
                _("grp_3").format(emo.sukses, media_page),
                disable_web_page_preview=True,
            )
        except Exception as exc:
            return await XD.edit(_("err_1").format(em.gagal, exc))
    elif message.reply_to_message.text:
        page_title = f"{client.me.first_name} {client.me.last_name or ''}"
        page_text = message.reply_to_message.text.replace("\n", "<br>")
        try:
            response = telegraph.create_page_md(title=page_title, content=page_text)
        except Exception as exc:
            return await XD.edit(_("err_1").format(em.gagal, exc))
        await XD.edit(
            _("grp_3").format(emo.sukses, response),
            disable_web_page_preview=True,
        )
