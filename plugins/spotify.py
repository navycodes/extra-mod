from Userbot import *

__MODULES__ = "Spotify"


def help_string(org):
    return h_s(org, "help_spotify")


async def download_spot(c, m, pros, query):
    url = f"https://api.botcahx.eu.org/api/download/spotify?url={query}&apikey=gwkenapanan"
    res = await fetch.get(url)
    if res.status_code == 200:
        data = res.json()
        if data.get("status") and data.get("result"):
            result = data["result"]["data"]
            title = result.get("title", "Title not available")
            artist_name = result["artist"].get("name", "Artist not available")
            duration = result.get("duration", "Duration not available")
            preview = result.get("preview", "Preview not available")
            download_url = result.get("url", "Download URL not available")
            output = f"""
<blockquote>🎶 **Title:** {title}
👤 **Artist:** {artist_name}
⏳ **Duration:** {duration}
🎧 **Preview:** [Listen here]({preview})</blockquote>
"""
            await c.bash(f"curl -L {download_url} -o {c.me.id}.mp3")
            try:
                await c.send_audio(m.chat.id, audio=f"{c.me.id}.mp3", caption=output)
                if os.path.exists(f"{c.me.id}.mp3"):
                    os.remove(f"{c.me.id}.mp3")
                return await pros.delete()
            except Exception as e:
                return await m.reply(f"{str(e)}")

        else:
            return "Error: Invalid result format."
    else:
        return f"Error: Request failed with status code {res.text}"


@ky.ubot("spotify|sptf")
async def _(c: nlx, m, _):
    em = Emojik(c)
    em.initialize()
    pros = await m.reply(_("proses").format(em.proses))

    if m.command[1] == "-dl":
        query = m.command[2]
        if len(m.command) < 3 or not query.startswith("https"):
            await m.reply(
                "{} Gunakan format `{}` -dl url".format(em.gagal, m.text.split()[0])
            )
            return await pros.delete()
        return await download_spot(c, m, pros, query)

    else:
        cmd = " ".join(m.text.split()[1:]).replace(" ", "+")
        x = await c.get_inline_bot_results(bot_username, f"src_spot {cmd}")
        await pros.delete()
        return await m.reply_inline_bot_result(x.query_id, x.results[0].id)
