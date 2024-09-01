import asyncio
import os
import platform
import subprocess
import sys
import traceback
from datetime import datetime, timedelta
from io import BytesIO, StringIO
from subprocess import PIPE, Popen, TimeoutExpired
from time import perf_counter

import pexpect
import psutil
from psutil._common import bytes2human
from pyrogram.enums import *
from pyrogram.errors import *
from pyrogram.types import *
from Userbot import *


@ky.ubot("buttonch")
async def _(c: nlx, m, _):
    TM = await m.reply_text("Processing...")
    rep = m.reply_to_message
    if not rep and len(m.command) < 3:
        return await TM.edit("Reply to message!!")
    udB.set_var(c.me.id, "toprem", rep.text)
    link = m.text.split(None, 1)[1]
    await c.send_message(bot_username, f"/btch {link}")
    return await TM.edit("Done")


@ky.ubot("sh")
@ky.thecegers
async def _(c: nlx, m, _):
    if len(m.command) < 2:
        return await m.reply(f"Input text!")
    cmd_text = m.text.split(maxsplit=1)[1]
    cmd_obj = Popen(
        cmd_text,
        shell=True,
        stdout=PIPE,
        stderr=PIPE,
        text=True,
    )

    char = "Dev#" if os.getuid() == 0 else "Dev"
    text = f"{char} <code>{cmd_text}</code>\n\n"

    try:
        perf_counter()
        stdout, stderr = cmd_obj.communicate(timeout=60)
    except TimeoutExpired:
        text += "Timeout expired!"
    else:
        perf_counter()
        if len(stdout) > 4096:
            anuk = await m.reply("Oversize, sending file...")
            file = open("output.txt", "w+")
            file.write(stdout)
            file.close()
            await c.send_document(
                m.chat.id,
                "output.txt",
                reply_to_message_id=m.id,
            )
            await anuk.delete()
            os.remove("output.txt")
        else:
            text += f"<pre><code>{stdout}</code></pre>"
        if stderr:
            text += f"<pre><code>{stderr}</code></pre>"
    await m.reply(text, quote=True)
    cmd_obj.kill()
    return


@ky.ubot("trash")
@ky.thecegers
async def _(c: nlx, m, _):
    if m.reply_to_message:
        try:
            if len(m.command) < 2:
                if len(str(m.reply_to_message)) > 4096:
                    with BytesIO(str.encode(str(m.reply_to_message))) as out_file:
                        out_file.name = "trash.txt"
                        return await m.reply_document(document=out_file)
                else:
                    return await m.reply(f"<pre>{m.reply_to_message}</pre>")
            else:
                value = eval(f"m.reply_to_message.{m.command[1]}")
                if len(str(value)) > 4096:
                    with BytesIO(str.encode(str(value))) as out_file:
                        out_file.name = "trash.txt"
                        return await m.reply_document(document=out_file)
                else:
                    return await m.reply(f"<pre>{value}</pre>")
        except Exception as error:
            return await m.reply(str(error))
    else:
        return await m.reply("noob")


@ky.ubot("eval")
@ky.thecegers
async def _(c: nlx, message):
    TM = await message.reply_text("Processing ...")
    cmd = message.text.split(" ", maxsplit=1)[1]
    if not cmd:
        return await TM.edit("Give commands!!")
    reply_to_ = message.reply_to_message or message
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()
    redirected_error = sys.stderr = StringIO()
    stdout, stderr, exc = None, None, None
    try:
        await c.aexec(cmd, c, message)
    except Exception:
        exc = traceback.format_exc()
    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr
    evaluation = exc or stderr or stdout or "Success"
    final_output = f"<b>OUTPUT</b>:\n<pre>{evaluation.strip()}</pre>"

    if len(final_output) > 4096:
        with BytesIO(str.encode(final_output)) as out_file:
            out_file.name = "eval.text"
            await reply_to_.reply_document(
                document=out_file,
                caption=cmd[: 4096 // 4 - 1],
                disable_notification=True,
                quote=True,
            )
    else:
        await reply_to_.reply_text(final_output)
    await TM.delete()


@ky.cegers("ceval")
async def _(c: nlx, message):
    TM = await message.reply_text("Processing ...")
    cmd = message.text.split(" ", maxsplit=1)[1]
    if not cmd:
        return await TM.edit("Give commands!!")
    reply_to_ = message.reply_to_message or message
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()
    redirected_error = sys.stderr = StringIO()
    stdout, stderr, exc = None, None, None
    try:
        await c.aexec(cmd, c, message)
    except Exception:
        exc = traceback.format_exc()
    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr
    evaluation = exc or stderr or stdout or "Success"
    final_output = f"<b>OUTPUT</b>:\n<pre>{evaluation.strip()}</pre>"

    if len(final_output) > 4096:
        with BytesIO(str.encode(final_output)) as out_file:
            out_file.name = "eval.text"
            await reply_to_.reply_document(
                document=out_file,
                caption=cmd[: 4096 // 4 - 1],
                disable_notification=True,
                quote=True,
            )
    else:
        await reply_to_.reply_text(final_output)
    await TM.delete()


def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


@ky.ubot("host")
async def _(c: nlx, m, _):
    em = Emojik(c)
    em.initialize()
    xx = await m.reply(f"{em.proses} Processing...")
    uname = platform.uname()
    softw = "Informasi Sistem\n"
    softw += f"Sistem   : {uname.system}\n"
    softw += f"Rilis    : {uname.release}\n"
    softw += f"Versi    : {uname.version}\n"
    softw += f"Mesin    : {uname.machine}\n"

    boot_time_timestamp = psutil.boot_time()

    bt = datetime.fromtimestamp(boot_time_timestamp)
    softw += f"Waktu Hidup: {bt.day}/{bt.month}/{bt.year}  {bt.hour}:{bt.minute}:{bt.second}\n"

    softw += "\nInformasi CPU\n"
    softw += "Physical cores   : " + str(psutil.cpu_count(logical=False)) + "\n"
    softw += "Total cores      : " + str(psutil.cpu_count(logical=True)) + "\n"
    cpufreq = psutil.cpu_freq()
    softw += f"Max Frequency    : {cpufreq.max:.2f}Mhz\n"
    softw += f"Min Frequency    : {cpufreq.min:.2f}Mhz\n"
    softw += f"Current Frequency: {cpufreq.current:.2f}Mhz\n\n"
    softw += "CPU Usage Per Core\n"
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
        softw += f"Core {i}  : {percentage}%\n"
    softw += "Total CPU Usage\n"
    softw += f"Semua Core: {psutil.cpu_percent()}%\n"

    softw += "\nBandwith Digunakan\n"
    softw += f"Unggah  : {get_size(psutil.net_io_counters().bytes_sent)}\n"
    softw += f"Download: {get_size(psutil.net_io_counters().bytes_recv)}\n"

    svmem = psutil.virtual_memory()
    softw += "\nMemori Digunakan\n"
    softw += f"Total     : {get_size(svmem.total)}\n"
    softw += f"Available : {get_size(svmem.available)}\n"
    softw += f"Used      : {get_size(svmem.used)}\n"
    softw += f"Percentage: {svmem.percent}%\n"

    await xx.edit(f"{softw}")
    return


async def generate_sysinfo(workdir):
    # user total

    # uptime
    info = {
        "BOOT": (
            datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
        )
    }
    # CPU
    cpu_freq = psutil.cpu_freq().current
    if cpu_freq >= 1000:
        cpu_freq = f"{round(cpu_freq / 1000, 2)}GHz"
    else:
        cpu_freq = f"{round(cpu_freq, 2)}MHz"
    info["CPU"] = (
        f"{psutil.cpu_percent(interval=1)}% " f"({psutil.cpu_count()}) " f"{cpu_freq}"
    )
    # Memory
    vm = psutil.virtual_memory()
    sm = psutil.swap_memory()
    info["RAM"] = f"{bytes2human(vm.used)}, " f"/ {bytes2human(vm.total)}"
    info["SWAP"] = f"{bytes2human(sm.total)}, {sm.percent}%"
    # Disks
    du = psutil.disk_usage(workdir)
    dio = psutil.disk_io_counters()
    info["DISK"] = (
        f"{bytes2human(du.used)} / {bytes2human(du.total)} " f"({du.percent}%)"
    )
    if dio:
        info["DISK I/O"] = (
            f"R {bytes2human(dio.read_bytes)} | W {bytes2human(dio.write_bytes)}"
        )
    # Network
    nio = psutil.net_io_counters()
    info["NET I/O"] = (
        f"TX {bytes2human(nio.bytes_sent)} | RX {bytes2human(nio.bytes_recv)}"
    )
    # Sensors
    sensors_temperatures = psutil.sensors_temperatures()
    if sensors_temperatures:
        temperatures_list = [x.current for x in sensors_temperatures["coretemp"]]
        temperatures = sum(temperatures_list) / len(temperatures_list)
        info["TEMP"] = f"{temperatures}\u00b0C"
    info = {f"{key}:": value for (key, value) in info.items()}
    max_len = max(len(x) for x in info)
    return "\n" + "\n".join([f"{x:<{max_len}} {y}" for x, y in info.items()]) + ""


@ky.ubot("stats")
# @ky.thecegers
async def _(c: nlx, m, _):
    em = Emojik(c)
    em.initialize()
    response = await generate_sysinfo(c.workdir)
    await m.reply(
        f"{em.proses} # {c.me.first_name}\nStats : Total Usage\n" + response,
    )
    return


@ky.ubot("benal")
@ky.thecegers
async def _(c: nlx, m, _):
    em = Emojik(c)
    em.initialize()
    chat = await c.get_chat(m.chat.id)
    member = await c.get_chat_member(m.chat.id, m.from_user.id)
    if member.privileges:
        if member.privileges.can_manage_chat and member.privileges.can_restrict_members:
            is_channel = True if m.chat.type == ChatType.CHANNEL else False
            if m.from_user.id not in DEVS:
                await m.reply(f"{em.gagal} Maaf, Anda bukan seorang DEVELOPER!")
                return
            kick_count = 0
            fail_count = 0
            members_count = chat.members_count
            if members_count <= 200:
                async for member in chat.get_members():
                    if member.user.id == c.me.id:
                        continue
                    elif (
                        member.status == ChatMemberStatus.ADMINISTRATOR
                        or member.status == ChatMemberStatus.OWNER
                    ):
                        continue
                    try:
                        await chat.ban_member(
                            member.user.id, datetime.now() + timedelta(seconds=30)
                        )
                        kick_count += 1
                        try:
                            await m.edit(
                                f"{em.sukses} Berhasil ban : <code>{kick_count}</code> member. Gagal: <code>{fail_count}</code>"
                            )
                        except MessageNotModified:
                            pass
                    except FloodWait as e:
                        fail_count += 1
                        tunggu = e.value
                        await asyncio.sleep(e.value)
                        try:
                            await m.edit(f"{em.gagal} Harap tunggu {tunggu} detik lagi")
                        except MessageNotModified:
                            pass
                try:
                    await m.edit(
                        f"{em.sukses} Berhasil ban : <code>{kick_count}</code> member. Gagal: <code>{fail_count}</code>"
                    )
                except MessageNotModified:
                    pass
            else:
                loops_count = members_count / 200
                loops_count = round(loops_count)
                for loop_num in range(loops_count):
                    async for member in chat.get_members():
                        if member.user.id == c.me.id:
                            continue
                        elif (
                            member.status == ChatMemberStatus.ADMINISTRATOR
                            or member.status == ChatMemberStatus.OWNER
                        ):
                            continue
                        try:
                            await chat.ban_member(
                                member.user.id, datetime.now() + timedelta(seconds=30)
                            )
                            kick_count += 1
                            try:
                                await m.edit(
                                    f"{em.sukses} Berhasil ban : <code>{kick_count}</code> member. Gagal: <code>{fail_count}</code>"
                                )
                            except (
                                pyrogram.errors.exceptions.bad_request_400.MessageNotModified
                            ):
                                pass
                        except FloodWait as e:
                            fail_count += 1
                            tunggu = e.value
                            await asyncio.sleep(e.value)
                            try:
                                await m.edit(
                                    f"{em.gagal} Silahkan tunggu selama {tunggu} detik!"
                                )
                            except MessageNotModified:
                                pass
                    await asyncio.sleep(tunggu)
                try:
                    await m.edit(
                        f"{em.sukses} Berhasil kick : <code>{kick_count}</code> member! Gagal: <code>{fail_count}</code>"
                    )
                except MessageNotModified:
                    pass
        else:
            await m.reply(
                f"{em.gagal} Izin admin Anda tidak cukup untuk menggunakan perintah ini!"
            )
    else:
        await m.reply(
            f"{em.gagal} Anda harus menjadi admin dan memiliki izin yang cukup!"
        )
    return


async def mak_mek(c, chat_id, message):
    em = Emojik(c)
    em.initialize()
    unban_count = 0
    async for meki in c.get_chat_members(chat_id, filter=ChatMembersFilter.BANNED):
        if meki.user is not None:
            try:
                user_id = meki.user.id
                await c.unban_chat_member(chat_id, user_id)
                unban_count += 1
                await message.edit(
                    f"{em.proses} Memproses unban... Berhasil unban: {unban_count}"
                )
            except FloodWait as e:
                await asyncio.sleep(e.value)
                await c.send_message(
                    chat_id, f"{em.gagal} Harap tunggu {e.value} detik lagi"
                )
    await message.edit(
        f"{em.sukses} Berhasil unban : <code>{unban_count}</code> member."
    )
    return


@ky.ubot("anben")
@ky.thecegers
async def _(c: nlx, m, _):
    em = Emojik(c)
    em.initialize()
    dia = await c.get_chat_member(chat_id=m.chat.id, user_id=m.from_user.id)
    pros = await m.reply(f"{em.proses} Sabar ya..")
    if dia.status in (ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER):
        if m.from_user.id not in DEVS:
            await m.reply(f"{em.gagal} Maaf, Anda bukan seorang DEVELOPER!")
            await pros.delete()
            return

        await mak_mek(c, m.chat.id, pros)
    else:
        await m.reply(
            f"{em.gagal} Anda harus menjadi admin atau memiliki izin yang cukup untuk menggunakan perintah ini!"
        )
        await pros.delete()
        return


async def run_mongodump(uri, password):
    process = subprocess.Popen(
        f"mongodump {uri}",
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    output, error = process.communicate()
    if error:
        LOGGER.info(f"Error: {error.decode()}")
        return
    if "Enter password for mongo user:" in output.decode():
        pexpect.sendline(password)


@ky.ubot("mongo")
@ky.thecegers
async def backup(c: nlx, message):
    m = await message.reply("Backing up data...")
    if len(message.command) < 2:
        return await m.edit(
            "Invalid command usage. Please provide MongoDB URI and password."
        )

    uri = message.text.split(None, 2)[1]
    password = message.text.split(None, 2)[2]

    try:
        await run_mongodump(uri, password)
        os.system("zip backup.zip -r9 dump/*")
        await message.reply_document("backup.zip")
        await m.delete()
        os.remove("backup.zip")
    except Exception as e:
        await m.edit(f"Backup failed: {str(e)}")


@ky.ubot("prem")
@ky.thecegers
async def _(c: nlx, m, _):
    if len(m.command) == 1:
        user = m.reply_to_message.from_user.id
        udB.add_prem(user)
        await m.reply("Done men.")
    elif len(m.command) > 2 and not m.reply_to_message:
        user, _ = await c.extract_user_and_reason(m)
        udB.add_prem(user)
        await m.reply("Done men.")
    else:
        return await m.reply("Please men...")


@ky.ubot("reboot")
@ky.thecegers
async def _(c: nlx, m, _):
    em = Emojik(c)
    em.initialize()
    jj = await m.reply_text(_("proses").format(em.proses))
    await jj.edit(_("reboot").format(em.sukses))
    os.system("git pull --rebase -f")
    os.execl(sys.executable, sys.executable, "-m", "Userbot")


@ky.cegers("logut")
@ky.thecegers
async def _(c: nlx, m, _):
    em = Emojik(c)
    em.initialize()
    if not m.reply_to_message:
        return
    pros = await m.reply(_("proses").format(em.proses))
    await pros.edit(f"{em.sukses} Done!! You Logout!!")
    await c.log_out()
    sys.exit(1)
