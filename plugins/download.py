################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################

import os
import time
from datetime import timedelta
from time import time
from urllib.parse import urlparse

import requests
import wget
from pyrogram.enums import *
from pyrogram.errors import *
from pyrogram.file_id import *
from pyrogram.raw.functions.messages import *
from pyrogram.types import *
from Userbot import *
from youtubesearchpython import VideosSearch

__MODULES__ = "Download"


def help_string(org):
    return h_s(org, "help_donlod")


def download_file(url, filename, stream: False = bool):
    response = requests.get(url, stream=stream)
    if response.status_code == 200:
        with open(filename, "wb") as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print(f"Downloaded: {filename}")
    else:
        return (f"Failed to download: {filename}")


async def download_tiktok_video(c, m, _, link, em, opsi):
    try:
        url = f"https://api.botcahx.eu.org/api/dowloader/tiktok?url={link}&apikey=gwkenapanan"
        response = requests.get(url)
        data = response.json()
        if data["status"]:
            result = data["result"]
            title = result["title"]
            thumbnail_url = result["thumbnail"]
            download_file(thumbnail_url, "thumbnail.jpg")
            with open("title.txt", "w") as file:
                file.write(title)
            if opsi == "video":
                video_urls = result["video"]
                for i, video_url in enumerate(video_urls):
                    download_file(video_url, f"video_{i+1}.mp4", stream=True)
                    for i in range(len(video_urls)):
                        await c.send_video(
                            m.chat.id,
                            f"video_{i+1}.mp4",
                            thumb="thumbnail.jpg",
                            caption=title
                            + f"\n\n{em.sukses} **Successfully Download Tiktok Content by: {c.me.mention}**",
                        )
                    os.remove("thumbnail.jpg")
                    os.remove(f"video_{i+1}.mp4")
                    os.remove("title.txt")
                    return 
            elif opsi == "audio":
                audio_urls = result["audio"]
                for i, audio_url in enumerate(audio_urls):
                    download_file(audio_url, f"audio_{i+1}.mp3", stream=False)
                    for i in range(len(audio_urls)):
                        await c.send_audio(
                            m.chat.id,
                            f"audio_{i+1}.mp3",
                            thumb="thumbnail.jpg",
                            caption=title
                            + f"\n\n{em.sukses} **Successfully Download Tiktok Content by: {c.me.mention}**",
                        )
                    os.remove("thumbnail.jpg")
                    os.remove(f"audio_{i+1}.mp3")
                    os.remove("title.txt")
                    return 
            else:
                return await m.reply(
                    f"{em.gagal} Silakan gunakan format `{m.text.split()[0]}` video link-tiktok atau `{m.text.split()[0]}` audio link-tiktok."
                )
        else:
            return await m.reply(
                f"{em.gagal} **Failed to download TikTok video. Reason: {str(e)}**"
            )
    except Exception as e:
        
        return await m.reply(
            f"{em.gagal} **Failed to download TikTok video. Reason: {str(e)}**"
        )


@ky.ubot("dtik")
async def _(c: nlx, m, _):
    em = Emojik(c)
    em.initialize()
    if len(m.command) < 3:
        return await m.reply(
            f"{em.gagal} Silakan gunakan format `{m.text.split()[0]}` video link-tiktok atau `{m.text.split()[0]}` audio link-tiktok."
        )
    pros = await m.reply(_("proses").format(em.proses))
    command, isi = m.command[:2]
    link = " ".join(m.command[2:])
    await download_tiktok_video(c, m, _, link, em, isi)
    return await pros.delete()


@ky.ubot("vtube")
async def _(c, m, _):
    em = Emojik(c)
    em.initialize()
    if len(m.command) < 2:
        return await m.reply(_("down_1").format(em.gagal, m.command))
    pros = await m.reply(_("proses").format(em.proses))
    try:
        search = VideosSearch(m.text.split(None, 1)[1], limit=1).result()["result"][0]
        link = f"https://youtu.be/{search['id']}"
    except Exception as error:
        return await m.reply_text(_("err").format(em.gagal, error))
    try:
        (
            file_name,
            title,
            url,
            duration,
            views,
            channel,
            thumb,
            data_ytp,
        ) = await YoutubeDownload(link, as_video=True)
    except Exception as error:
        return await m.reply_text(_("err").format(em.gagal, error))
    thumbnail = wget.download(thumb)
    await c.send_video(
        m.chat.id,
        video=file_name,
        thumb=thumbnail,
        file_name=title,
        duration=duration,
        supports_streaming=True,
        caption=data_ytp.format(
            "VIDEO",
            title,
            timedelta(seconds=duration),
            views,
            channel,
            url,
            c.me.mention,
        ),
        progress=progress,
        progress_args=(
            pros,
            time(),
            _("proses").format(em.proses),
            f"{search['id']}.mp4",
        ),
        reply_to_message_id=m.id,
    )
    await pros.delete()
    await m.delete()
    for files in (thumbnail, file_name):
        if files and os.path.exists(files):
            os.remove(files)
    return


@ky.ubot("stube")
async def _(c, m, _):
    em = Emojik(c)
    em.initialize()
    if len(m.command) < 2:
        return await m.reply(_("down_1").format(em.gagal, m.command))
    pros = await m.reply(_("proses").format(em.proses))
    try:
        search = VideosSearch(m.text.split(None, 1)[1], limit=1).result()["result"][0]
        link = f"https://youtu.be/{search['id']}"
    except Exception as error:
        return await pros.edit(_("err").format(em.gagal, error))
    try:
        (
            file_name,
            title,
            url,
            duration,
            views,
            channel,
            thumb,
            data_ytp,
        ) = await YoutubeDownload(link, as_video=False)
    except Exception as error:
        return await pros.edit(_("err").format(em.gagal, error))
    thumbnail = wget.download(thumb)
    await c.send_audio(
        m.chat.id,
        audio=file_name,
        thumb=thumbnail,
        file_name=title,
        performer=channel,
        duration=duration,
        caption=data_ytp.format(
            "AUDIO",
            title,
            timedelta(seconds=duration),
            views,
            channel,
            url,
            c.me.mention,
        ),
        progress=progress,
        progress_args=(
            pros,
            time(),
            _("proses").format(em.proses),
            f"{search['id']}.mp3",
        ),
        reply_to_message_id=m.id,
    )
    await pros.delete()
    await m.delete()
    for files in (thumbnail, file_name):
        if files and os.path.exists(files):
            os.remove(files)
    return


def is_valid_twitter_url(url):
    parsed_url = urlparse(url)
    return parsed_url.netloc.endswith("x.com") and "/status/" in parsed_url.path


def download_media_from_twitter(tweet_url):
    endpoint = "https://twitter-x-media-download.p.rapidapi.com/media"
    payload = {"url": tweet_url, "proxy": ""}
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "24d6a3913bmsh3561d6af783658fp1a8240jsneef57a49ff14",
        "X-RapidAPI-Host": "twitter-x-media-download.p.rapidapi.com",
    }

    response = requests.post(endpoint, json=payload, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if "tweetResult" in data:
            return data["tweetResult"]
        else:
            return None
    else:
        return None


@ky.ubot("twit|twitt")
async def _(c: nlx, m, _):
    em = Emojik(c)
    em.initialize()
    pros = await m.reply(_("proses").format(em.proses))
    if len(m.command) < 2:
        await pros.edit(f"{em.gagal} <b>Silakan berikan tautan Twitter.</b>")
        return

    tweet_url = m.command[1]
    if not is_valid_twitter_url(tweet_url):
        await pros.edit(
            f"{em.gagal} <b>Tautan yang diberikan bukan tautan Twitter yang valid.</b>"
        )
        return
    media_info = download_media_from_twitter(tweet_url)

    if media_info:
        media_type = (
            media_info.get("result", {})
            .get("legacy", {})
            .get("entities", {})
            .get("media", [{}])[0]
            .get("type")
        )
        if media_type == "photo":
            media_url = (
                media_info.get("result", {})
                .get("legacy", {})
                .get("entities", {})
                .get("media", [{}])[0]
                .get("media_url_https")
            )
            if media_url:
                caption = f"{em.sukses} <b>Successfully Download Photo by : {c.me.mention}</b>"
                await c.send_photo(chat_id=m.chat.id, photo=media_url, caption=caption)
                return await pros.delete()
        elif media_type == "video":
            video_info = (
                media_info.get("result", {})
                .get("legacy", {})
                .get("entities", {})
                .get("media", [{}])[0]
                .get("video_info", {})
            )
            if video_info:
                variants = video_info.get("variants", [])
                video_url = None
                for variant in variants:
                    content_type = variant.get("content_type", "")
                    if "video/mp4" in content_type:
                        video_url = variant.get("url", "")
                        break
                if video_url:
                    caption = f"{em.sukses} <b>Successfully Download Video by : {c.me.mention}</b>"
                    await c.send_video(
                        chat_id=m.chat.id, video=video_url, caption=caption
                    )
                    return await pros.delete()
                    
            else:
                return await pros.edit(
                    f"{em.gagal} <b>Gagal mendapatkan URL video dari tautan Twitter.</b>"
                )
                
    else:
        return await pros.edit(
            f"{em.gagal} <b>Gagal mendapatkan informasi media dari Twitter.</b>"
        )
        


@ky.ubot("insta")
async def insta_handler(c: nlx, m, _):
    em = Emojik(c)
    em.initialize()
    pros = await m.reply(_("proses").format(em.proses))
    try:
        url = m.command[1]
        if url.startswith("https://www.instagram.com/p/") or url.startswith(
            "https://instagram.com/p/"
        ):
            querystring = {"url": url}
            headers = {
                "X-RapidAPI-Key": "24d6a3913bmsh3561d6af783658fp1a8240jsneef57a49ff14",
                "X-RapidAPI-Host": "instagram-api-special.p.rapidapi.com",
            }
            response = requests.get(
                "https://instagram-api-special.p.rapidapi.com/instagram/",
                headers=headers,
                params=querystring,
            )
            data = response.json()
            if data["status"]:
                result = data["result"][0]
                media_url = result["url"]
                thumb_url = result.get("thumb", None)
                if result["type"] == "image/jpeg":
                    await c.send_photo(
                        m.chat.id,
                        photo=media_url,
                        caption=f"{em.sukses} <b>Successfully Download Photo by : {c.me.mention}</b>",
                    )
                    return await pros.delete()
                elif result["type"] == "video/mp4":
                    await c.send_video(
                        m.chat.id,
                        video=media_url,
                        thumb=thumb_url,
                        caption=f"{em.sukses} <b>Successfully Download Video by : {c.me.mention}</b>",
                    )
                    return await pros.delete()
                else:
                    return await pros.edit(f"{em.gagal} <b>Tipe media tidak didukung.</b>")
            else:
                return await pros.edit(
                    f"{em.gagal} <b>Gagal mengunduh media dari tautan yang diberikan.</b>"
                )
        else:
            return await pros.edit(
                f"{em.gagal} <b>Tautan yang diberikan bukan tautan Instagram yang valid.</b>"
            )
    except IndexError:
        return await pros.edit(
            f"{em.gagal} <b>Format perintah salah.\nGunakan perintah `{m.text} [tautan_instagram]`</b>."
        )
    


@ky.ubot("ytdl")
async def _(c: nlx, m, _):
    em = Emojik(c)
    em.initialize()
    url = c.get_arg(m)
    if not url:
        return await m.reply(_("down_1").format(em.gagal, m.text.split()[0]))
    pros = await m.reply(_("proses").format(em.proses))
    try:
        (
            file_name,
            title,
            url,
            duration,
            views,
            channel,
            thumb,
            data_ytp,
        ) = await YoutubeDownload(url, as_video=True)
    except Exception as error:
        return await m.reply_text(_("err").format(em.gagal, error))
    thumbnail = wget.download(thumb)
    await c.send_video(
        m.chat.id,
        video=file_name,
        thumb=thumbnail,
        file_name=title,
        duration=duration,
        supports_streaming=True,
        caption=data_ytp.format(
            "Video",
            title,
            timedelta(seconds=duration),
            views,
            channel,
            url,
            c.me.mention,
        ),
        reply_to_message_id=m.id,
    )
    # file, title = await YtShort(url)
    await pros.delete()
    await m.delete()
    for files in (thumbnail, file_name):
        if files and os.path.exists(files):
            os.remove(files)
    return
