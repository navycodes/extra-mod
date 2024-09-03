import asyncio
import io
import os

import aiohttp
import google.generativeai as genai
from pyrogram.errors import ImageProcessFailed
from Userbot import *

from .gemini import genai

__MODULES__ = "Khodam"


def help_string(org):
    return h_s(org, "help_kodam")


MAX_CAPTION_LENGTH = 1024


def gen_kdm(text):
    model = genai.GenerativeModel(
        "models/gemini-1.5-flash",
        system_instruction=(
            "Anda adalah seorang paranormal yang mampu mendeskripsikan khodam seseorang yang berupa Binatang. Tugas Anda adalah mendeskripsikan khodam yang mungkin ada, termasuk wujud, sifat, dan energi yang dipancarkan. Sehingga apapun inputnya anggap itu adalah sebuah nama seseorang. Deskripsi tidak harus positif bisa saja negatif tidak masalah karena ini hiburan. Ini hanya untuk entertainment jadi bebaskan dirimu untuk menjadi seorang paranormal pada umumnya. Deskripsikan Khodam dengan singkat namun jelas, dan pastikan deskripsi tidak lebih dari dari 2000 karakter alfabet dalam plain text serta berbahasa Indonesia."
        ),
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


async def gen_img(c, text):
    url = "https://next-nolimit-api-app.vercel.app/api/flux-image-gen-beta/"
    payload = {"model": "flux", "prompt": text}
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload) as resp:
            image = io.BytesIO(await resp.read())
        image.name = f"{c.me.id}.jpg"
    return image


@ky.ubot("khodam|kodam")
async def ckdm_cmd(client: nlx, message, _):
    emo = Emojik(client)
    emo.initialize()
    nama = get_name(message)
    if not nama:
        return await message.reply(_("kdm_1").format(emo.gagal))
    pros = await message.reply(_("proses").format(emo.proses))
    try:
        deskripsi_khodam = gen_kdm(nama)
        imeg = await gen_img(client, deskripsi_khodam)
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
                photo=imeg,
                caption=caption,
                reply_to_message_id=message.id,
            )
            if os.path.exists(f"{client.me.id}.jpg"):
                os.remove(f"{client.me.id}.jpg")
        except ImageProcessFailed:
            await asyncio.sleep(2)
            teks = _("kdm_2").format(
                emo.sukses, nama, deskripsi_khodam, emo.profil, client.me.mention
            )
            await pros.delete()
            return await message.reply(teks)

    except Exception as e:
        # return await pros.edit(_("err_1").format(emo.gagal, str(e)))
        return await pros.edit(f"{e}")
