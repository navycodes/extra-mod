import asyncio
import os

import google.generativeai as genai
from Userbot import *

from .gemini import genai

__MODULES__ = "Khodam"


def help_string(org):
    return h_s(org, "help_kodam")


def gen_kdm(c, text, _):
    model = genai.GenerativeModel(
        "models/gemini-1.5-flash", system_instruction=(_("intruk_khodam"))
    )
    try:
        response = model.generate_content(text)
        return response.text.strip()
    except Exception as e:
        return f"Terjadi kesalahan: {str(e)}"


def get_name(message):
    if message.reply_to_message:
        if message.reply_to_message.sender_chat:
            return None
        first_name = message.reply_to_message.from_user.first_name or ""
        last_name = message.reply_to_message.from_user.last_name or ""
        full_name = f"{first_name} {last_name}".strip()
        return full_name if full_name else None
    else:
        input_text = message.text.split(None, 1)
        return input_text[1].strip() if len(input_text) > 1 else None


@ky.ubot("khodam|kodam")
async def ckdm_cmd(client: nlx, message, _):
    emo = Emojik(client)
    emo.initialize()
    nama = get_name(message)
    if not nama:
        return await message.reply(_("kdm_1").format(emo.gagal))
    pros = await message.reply(_("proses").format(emo.proses))
    try:
        deskripsi_khodam = gen_kdm(client, nama, _)
        url = "https://next-nolimit-api-app.vercel.app/api/flux-image-gen-beta/"
        payload = {"model": "flux", "prompt": deskripsi_khodam}
        response = await fetch.post(url, json=payload)
        if response.status_code == 200:
            with open("genai.jpg", "wb") as f:
                f.write(response.content)
            caption = _("kdm_2").format(
                emo.sukses, nama, deskripsi_khodam, emo.profil, client.me.mention
            )
            if len(caption) > MAX_CAPTION_LENGTH:
                caption = caption[:MAX_CAPTION_LENGTH] + "..."
            try:
                await asyncio.sleep(2)
                await pros.delete()
                await client.send_photo(
                    message.chat.id,
                    photo="genai.jpg",
                    caption=caption,
                    reply_to_message_id=message.id,
                )
            except Exception as e:
                return await pros.edit(_("err_1").format(emo.gagal, e))
            finally:
                if os.path.exists("genai.jpg"):
                    os.remove("genai.jpg")
        else:
            await asyncio.sleep(2)
            teks = _("kdm_2").format(
                emo.sukses, nama, deskripsi_khodam, emo.profil, client.me.mention
            )
            return await pros.edit(teks)
    except Exception as e:
        return await pros.edit(_("err_1").format(emo.gagal, e))
