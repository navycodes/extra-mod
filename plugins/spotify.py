from Userbot import *
import wget
__MODULES__ = "Spotify"


def help_string(org):
    return h_s(org, "help_porn")

async def download_spot(c, m, query):
    url = f"https://api.botcahx.eu.org/api/download/spotify?url={query}&apikey=gwkenapanan"
    res = await fetch.get(url)
    if res.status_code == 200:
        data = res.json()
        if data.get('status') and data.get('result'):
            result = data['result']['data']
            thumbnail = result.get('thumbnail', 'Thumbnail not available')
            title = result.get('title', 'Title not available')
            artist_name = result['artist'].get('name', 'Artist not available')
            duration = result.get('duration', 'Duration not available')
            preview = result.get('preview', 'Preview not available')
            download_url = result.get('url', 'Download URL not available')
            thumb = wget.download(thumbnail)
            output = f"""
            🎶 **Title:** {title}
            👤 **Artist:** {artist_name}
            ⏳ **Duration:** {duration}
            🎧 **Preview:** [Listen here]({preview})
            """
            await c.bash(f"curl -L {download_url} -o {title}.mp3")
            try:
                await c.send_audio(m.chat.id, audio=f"{title}.mp3", caption=output)
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
    if len(m.command) < 3:
        xk = {"_id": c.me.id, "args": c.get_arg(m)}
        udB.set_var(c.me.id, "spot", xk)
        cmd = m.command[1]
        x = await c.get_inline_bot_results(bot_username, f"src_spot {cmd}")
        await m.reply_inline_bot_result(x.query_id, x.results[0].id)
    else:
        if "-dl" in m.command[1]:
            query = m.command[2]
            if not query.startswith("https"):
              return await m.reply("{} Gunakan format `{}` -dl url".format(em.gagal, m.text.split()[0]))
            await download_spot(c, m, query)
        else:
            return await m.reply("{} Gunakan format `{}` -dl url".format(em.gagal, m.text.split()[0]))
      
      
      
