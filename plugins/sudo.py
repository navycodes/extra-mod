from Userbot import *

__MODULES__ = "Sudo"


def help_string(org):
    return h_s(org, "help_sudo")


@ky.ubot("addsudo")
async def _(c: nlx, m, _):
    em = Emojik(c)
    em.initialize()
    msg = await m.reply(_("proses").format(em.proses))
    user_id = await c.extract_user(m)
    if not user_id:
        return await msg.edit(_("prof_1").format(em.gagal))
    try:
        user = await c.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)
    usro = f"[{user.first_name} {user.last_name or ''}](tg://user?id={user.id})"
    sudoers = udB.get_list_from_var(c.me.id, "sudoers", "userid")
    if user.id in sudoers:
        return await msg.edit(_("sud_1").format(em.sukses, usro))
    try:
        udB.add_to_var(c.me.id, "sudoers", user.id, "userid")
        return await msg.edit(_("sud_2").format(em.sukses, usro))
    except Exception as error:
        return await msg.edit(error)


@ky.ubot("delsudo")
async def _(c: nlx, m, _):
    em = Emojik(c)
    em.initialize()
    msg = await m.reply(_("proses").format(em.proses))
    user_id = await c.extract_user(m)
    if not user_id:
        return await m.reply(_("prof_1").format(em.sukses))

    try:
        user = await c.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)

    sudo_users = udB.get_list_from_var(c.me.id, "sudoers", "userid")
    usro = f"[{user.first_name} {user.last_name or ''}](tg://user?id={user.id})"
    if user.id not in sudo_users:
        return await msg.edit(_("sud_3").format(em.sukses, usro))

    try:
        udB.remove_from_var(c.me.id, "sudoers", user.id, "userid")
        return await msg.edit(_("sud_4").format(em.sukses, usro))
    except Exception as error:
        return await msg.edit(_("err").format(em.gagal, error))


@ky.ubot("sudolist")
async def _(c: nlx, m, _):
    em = Emojik(c)
    em.initialize()
    msg = ""
    sudoers = udB.get_list_from_var(c.me.id, "sudoers", "userid")
    for ix in sudoers:
        try:
            org = await c.get_users(int(ix))
        except Exception:
            org = None
        if org:
            org = org.first_name if not org.mention else org.mention
            msg += f"• {org}\n"
        else:
            msg += f"• {ix}\n"

    if sudoers == 0:
        return await m.reply(_("sud_5").format(em.gagal))
    else:
        await m.reply(_("sud_6").format(em.sukses, msg))
        return
