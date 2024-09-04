import requests
from Userbot import *


async def process_message(c: nlx, m, _, text, decode=False):
    em = Emojik(c)
    em.initialize()
    if text:
        encoding_type = "base64" if not decode else "base64&decode=true"
        url = f"https://networkcalc.com/api/encoder/{text}?encoding={encoding_type}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if not decode and "encoded" in data:
                encoded_text = data["encoded"]
                return await m.reply(_("enc_1").format(em.sukses, encoded_text))
            elif decode and "decoded" in data:
                decoded_text = data["decoded"]
                return await m.reply(_("enc_2").format(em.sukses, decoded_text))
            else:
                gagal = f"encode" if not decode else "decode"
                return await m.reply(_("enc_3").format(em.gagal, gagal))
        else:
            return await m.reply(_("enc_4").format(em.gagal, response.status_code))
    else:
        return await m.reply(_("enc_5").format(em.gagal))


@ky.ubot("encode")
async def _(c: nlx, m, _):
    em = Emojik(c)
    em.initialize()
    pros = await m.reply(_("proses").format(em.proses))
    if m.reply_to_message and m.reply_to_message.text:
        text = m.reply_to_message.text
    else:
        text = " ".join(m.command[1:])
    await process_message(c, m, _, text)
    return await pros.delete()
    


@ky.ubot("decode")
async def _(c: nlx, m, _):
    em = Emojik(c)
    em.initialize()
    pros = await m.reply(_("proses").format(em.proses))
    if m.reply_to_message and m.reply_to_message.text:
        text = m.reply_to_message.text
    else:
        text = " ".join(m.command[1:])
    await process_message(c, m, _, text, decode=True)
    return await pros.delete()
    
