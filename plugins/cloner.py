#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2020-2024 (c) Randy @xtdevs
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os

import requests
from pyrogram.errors import RPCError
from Userbot import *


async def get_clone_account(user_id):
    url = "https://akeno.randydev.my.id/ryuzaki/get-profile-clone"
    x = "d9a575b7f8ce61cb6997debd1c96ec7e8baad8d4c4f9c0bd42cec456503564b2"
    headers = {"Content-Type": "application/json", "api-key": x}
    payload = {"user_id": user_id}
    response = requests.get(url, headers=headers, json=payload)
    if response.status_code != 200:
        print(f"error response: {response.status_code}")
        return None
    return response.json()


async def post_clone_accont(
    user_id: int,
    first_name: str,
    last_name: str,
    profile_id: str,
    bio_data: str,
):
    url = "https://akeno.randydev.my.id/ryuzaki/profile-clone"
    payload = {
        "user_id": user_id,
        "first_name": first_name,
        "last_name": last_name,
        "profile_id": profile_id,
        "bio": bio_data,
    }
    x = "d9a575b7f8ce61cb6997debd1c96ec7e8baad8d4c4f9c0bd42cec456503564b2"
    headers = {"Content-Type": "application/json", "api-key": x}
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code != 200:
        print(f"error response: {response.status_code}")
        return None
    return response.json()


@ky.ubot("clone")
@ky.thecegers
async def user_clone(client, message):
    if len(message.command) < 2:
        return await message.reply_text("Invalid command")
    command, option = message.command[:2]
    reply_message = False
    account_revert = False
    if option == "-reply":
        reply_message = True
    elif option == "-revert":
        account_revert = True
    if reply_message and account_revert:
        return await message.reply_text("Invalid options. Choose either")
    elif reply_message:
        reply_messages = message.reply_to_message
        if not reply_messages:
            return await message.reply_text("Please reply to a message.")
        if not reply_messages.from_user:
            return await message.reply_text("Invalid user.")
        user_id = (
            reply_messages.from_user.id
            if reply_messages.from_user
            else "@" + reply_messages.from_user.username
        )
        try:
            me_user = await client.get_chat("me")
            await client.get_users("me")
            user = await client.get_chat(user_id)
            await client.get_users(user_id)
        except Exception as e:
            return await message.reply_text(f"Error: {e}")
        me_bio = me_user.bio if me_user else ""
        me_first_name = me_user.first_name if me_user else ""
        me_last_name = me_user.last_name if me_user else ""
        user_bio = user.bio if user else ""
        user_first_name = user.first_name if user else ""
        user_photo_file_id = user.photo.big_file_id if user.photo else None
        me_photo_file_id = None
        try:
            async for file in client.get_chat_photos(client.me.id, limit=1):
                me_photo_file_id = file.file_id if file else None
        except RPCError as rpc_error:
            return await message.reply_text(f"RPCError: {rpc_error}")
        except Exception as e:
            return await message.reply_text(f"Error: {e}")
        try:
            response = await post_clone_accont(
                user_id=me_user.id,
                first_name=me_first_name,
                last_name=me_last_name,
                profile_id=me_photo_file_id,
                bio_data=me_bio,
            )
            if response is None:
                return await message.reply_text("Error response")
            set_profile = None
            if user_photo_file_id:
                set_profile = await client.download_media(user_photo_file_id)
            if set_profile:
                await client.set_profile_photo(photo=set_profile)
            if user_first_name and user_bio:
                await client.update_profile(
                    first_name=user_first_name, last_name="", bio=user_bio
                )
            await message.reply_text("Successfully steal and set to your account!")
            if set_profile:
                os.remove(set_profile)
        except Exception as e:
            await message.reply_text(f"Error: {e}")
    elif account_revert:
        try:
            user = await client.get_users("me")
            user_back = await get_clone_account(user.id)
            if user_back is None:
                return await message.reply_text("Error response")
            photos = [p async for p in client.get_chat_photos("me")]
            if photos:
                await client.delete_profile_photos(photos[0].file_id)
            if user_back["randydev"]["bio"] and user_back["randydev"]["first_name"]:
                await client.update_profile(
                    first_name=user_back["randydev"]["first_name"],
                    last_name=user_back["randydev"]["last_name"],
                    bio=user_back["randydev"]["bio"],
                )
            else:
                return await message.reply_text(
                    "User doesn't have a profile bio and last name"
                )
            await message.reply_text("Successfully reverted back to your account!")
        except RPCError as rpc_error:
            await message.reply_text(f"RPCError: {rpc_error}")
        except Exception as e:
            await message.reply_text(f"Error: {e}")
    else:
        await message.reply_text("Invalid options. Choose either")
