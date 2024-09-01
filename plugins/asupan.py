import asyncio
import os
import random

import aiohttp
import wget
from pyrogram.types import InputMediaPhoto

from Userbot import *

__MODULES__ = "Asupan"


def help_string(org):
    return h_s(org, "help_supan")


async def download_asupan_nya(c, m, _, em, value):
    if value == "hijaber":
        url = "https://api.botcahx.eu.org/api/asupan/hijaber?apikey=gwkenapanan"  # jpg
    elif value == "santuy":
        url = "https://api.botcahx.eu.org/api/asupan/santuy?apikey=gwkenapanan"  # mp4
    elif value == "ukhty":
        url = "https://api.botcahx.eu.org/api/asupan/ukhty?apikey=gwkenapanan"  # mp4
    elif value == "cecan":
        url = "https://api.botcahx.eu.org/api/asupan/cecan?apikey=gwkenapanan"  # jpg
    else:
        url = f"https://api.botcahx.eu.org/api/asupan/tiktok?query={value}&apikey=gwkenapanan"  # mp4

    if value in ["hijaber", "cecan"]:
        response = requests.get(url)
        if response.status_code == 200:
            with open("ce.jpg", "wb") as file:
                file.write(response.content)
            await m.reply_photo(
                "ce.jpg",
                caption=f"{em.sukses} <blockquote><b>Search by {c.me.mention}</blockquote></b>",
            )
            os.remove("ce.jpg")
        else:
            print(f"Permintaan gagal. Status code: {response.status_code}")
    elif value in ["ukhty", "santuy"]:
        response = requests.get(url)
        if response.status_code == 200:
            with open("ce.mp4", "wb") as file:
                file.write(response.content)
            await m.reply_video(
                "ce.mp4",
                caption=f"{em.sukses} <blockquote><b>Search by {c.me.mention}</blockquote></b>",
            )
            os.remove("ce.mp4")
        else:
            print(f"Permintaan gagal. Status code: {response.status_code}")
    else:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if (
                "status" in data
                and data["status"]
                and "code" in data
                and data["code"] == 200
            ):
                if "result" in data and "data" in data["result"]:
                    videos = data["result"]["data"]
                    if not videos:
                        await m.reply(
                            f"{em.gagal} <b>Tidak ada video yang ditemukan!! Coba gunakan nama akun tiktok lain.</b>"
                        )
                        return

                    video_info = random.choice(videos)
                    video_url = video_info["play"]
                    video_title = video_info["title"]
                    video_link = video_info["play"]

                    video_response = requests.get(video_url)
                    if video_response.status_code == 200:
                        video_filename = f"{video_title}.mp4"
                        with open(video_filename, "wb") as video_file:
                            video_file.write(video_response.content)

                        caption = f"Judul: {video_title}\nLink: {video_link}"
                        await m.reply_video(
                            video_filename,
                            caption=caption
                            + f"{em.sukses} <blockquote><b>Search by {c.me.mention}</blockquote></b>",
                        )
                        os.remove(video_filename)
                    else:
                        print(
                            f"Gagal mendownload video. Status code: {video_response.status_code}"
                        )
                else:
                    print("Key 'result' atau 'data' tidak ditemukan dalam respons API.")
            else:
                print("Tidak ada data video yang ditemukan atau status code salah.")
        else:
            print(f"Permintaan ke API gagal. Status code: {response.status_code}")


async def download_image(session, url):
    filename = url.split("/")[-1]
    async with session.get(url) as response:
        if response.status == 200:
            with open(filename, "wb") as f:
                f.write(await response.read())
            return filename
        return None


async def download_and_send_images(c, m, value):
    media_group = []
    url = f"https://api.botcahx.eu.org/api/search/bing-img?text={value}&apikey=gwkenapanan"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as data:
            if data.status == 200:
                result = await data.json()
                image_urls = result.get("result", [])
                tasks = [download_image(session, image_urls[i]) for i in range(3)]
                images = await asyncio.gather(*tasks)
                for im in images:
                    media_group.append(InputMediaPhoto(im))
                await m.reply_media_group(media_group)


@ky.ubot("bing-img")
async def _(c, m, _):
    em = Emojik(c)
    em.initialize()
    if len(m.command) < 2 and not m.reply_to_message:
        return await m.reply(
            f"{em.gagal} Silahkan gunakan contoh format: `{m.text.split()[0]} wanita cantik gaun putih`."
        )
    pros = await m.reply(_("proses").format(em.proses))
    value = nlx.get_text(m)
    await download_and_send_images(c, m, value)
    return await pros.delete()


@ky.ubot("asupan")
async def _(c, m, _):
    em = Emojik(c)
    em.initialize()
    if len(m.command) < 2:
        return await m.reply(
            f"{em.gagal} Silahkan gunakan contoh format: `{m.text.split()[0]} ukhty`."
        )
    pros = await m.reply(_("proses").format(em.proses))
    value = m.text.split()[1]
    await download_asupan_nya(c, m, _, em, value)
    return await pros.delete()


@ky.ubot("ppcp")
async def _(c, m, _):
    em = Emojik(c)
    em.initialize()
    all_foto = []
    pros = await m.reply(_("proses").format(em.proses))
    url = "https://api.botcahx.eu.org/api/randomgambar/couplepp?apikey=gwkenapanan"
    data = requests.get(url)
    if data.status_code == 200:
        file = data.json()
        a = file["result"]["male"]
        b = file["result"]["female"]
        foto_male = wget.download(a)
        foto_female = wget.download(b)
        all_foto.append(InputMediaPhoto(foto_male))
        all_foto.append(InputMediaPhoto(foto_female))
        await m.reply_media_group(all_foto)
        os.remove(foto_male)
        os.remove(foto_female)
        return await pros.delete()
    else:
        return await pros.edit("{} Maaf server sedang down".format(em.gagal))


@ky.ubot("meme")
async def _(c, m, _):
    em = Emojik(c)
    em.initialize()
    pros = await m.reply(_("proses").format(em.proses))
    url = "https://api.botcahx.eu.org/api/random/meme?apikey=gwkenapanan"
    data = requests.get(url)
    if data.status_code == 200:
        with open("mm.jpg", "wb") as file:
            file.write(data.content)
        await m.reply_photo("mm.jpg")
        os.remove("mm.jpg")
        return await pros.delete()
    else:
        return await pros.edit("{} Maaf server sedang down".format(em.gagal))
