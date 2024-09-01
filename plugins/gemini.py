import os

import google.generativeai as genai
import requests
from pyrogram.enums import ChatAction
from pyrogram.errors import *
from Userbot import *

__MODULES__ = "ChatGpt"


def help_string(org):
    return h_s(org, "help_chatgpt")


genai.configure(api_key="AIzaSyC28dJ5wTyjm44ng1WCuz4uTppelgRcLuU")


def gemini(text):
    try:
        generation_config = {
            "temperature": 0.6,
            "top_p": 1,
            "top_k": 1,
            "max_output_tokens": 2048,
        }
        safety_settings = [
            {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_ONLY_HIGH"},
            {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_ONLY_HIGH"},
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_ONLY_HIGH",
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_ONLY_HIGH",
            },
        ]
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config=generation_config,
            safety_settings=safety_settings,
        )
        # convo = model.start_chat()
        # convo.send_message(text)
        respon = model.generate_content(text)
        if respon:
            return f"{respon.text}"
    except Exception as e:
        print(f"Error generating text: {str(e)}")
        return f"Error generating text: {str(e)}"


async def mari_kirim(c, m, query):
    em = Emojik(c)
    em.initialize()
    try:
        chat_id = m.chat.id
        if m.sender_chat:
            m.sender_chat.id
        else:
            m.from_user.id
        respon = gemini(query)
        await m._client.send_chat_action(chat_id, ChatAction.TYPING)
        await asyncio.sleep(2)
        if len(respon) > 4096:
            with open("chatbot.txt", "wb") as file:
                file.write(respon.encode("utf-8"))
            await m._client.send_chat_action(chat_id, ChatAction.UPLOAD_DOCUMENT)
            await asyncio.sleep(2)
            await m._client.send_document(
                chat_id, "chatbot.txt", reply_to_message_id=m.id
            )
            os.remove("chatbot.txt")
            await m._client.send_chat_action(chat_id, ChatAction.CANCEL)
        else:
            await m.reply_text(
                "{} {}".format(em.sukses, respon), reply_to_message_id=m.id
            )
        await m._client.send_chat_action(chat_id, ChatAction.CANCEL)
    except ChatWriteForbidden:
        pass


@ky.ubot("gemini")
async def _(c: nlx, m, _):
    em = Emojik(c)
    em.initialize()
    pros = await m.reply(_("proses").format(em.proses))
    reply_text = c.get_text(m)
    if not reply_text:
        return pros.edit(_("enc_5").format(em.gagal))
    await mari_kirim(c, m, reply_text)
    await pros.delete()


@ky.ubot("ai|ask")
async def _(client: nlx, message, _):
    em = Emojik(client)
    em.initialize()
    try:
        a = client.get_text(message)
        await client.send_chat_action(message.chat.id, ChatAction.TYPING)
        prs = await message.reply_text(_("proses").format(em.proses))
        url = f"https://widipe.com/v2/gpt4?text={a}"
        headers = {"accept": "application/json"}
        res = requests.get(url, headers=headers)
        try:
            if res.status_code == 200:
                x = res.json()["result"]
                await message.reply(
                    "{} {}".format(em.sukses, x), reply_to_message_id=message.id
                )
                return await prs.delete()
            else:
                return await prs.edit(_("err_1").format(em.gagal, response.text))
        except Exception as e:
            return await prs.edit(_("err").format(em.gagal, e))
    except Exception as e:
        return await prs.edit(_("err").format(em.gagal, e))


@ky.ubot("fluxai")
async def _(c: nlx, m, _):
    em = Emojik(c)
    em.initialize()
    pros = await m.reply(_("proses").format(em.proses))
    text = c.get_arg(m)
    if not text:
        return pros.edit(_("enc_5").format(em.gagal))
    url = "https://next-nolimit-api-app.vercel.app/api/flux-image-gen-beta/"
    payload = {"prompt": text}
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        with open("genai.jpg", "wb") as f:
            f.write(response.content)
        await m.reply_photo("genai.jpg")
        os.remove("genai.jpg")
    else:
        await m.reply(_("err_1").format(em.gagal, response.text))
    return await pros.delete()
