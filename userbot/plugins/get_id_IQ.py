"""Get ID of any Telegram media, or any user
Syntax: .جلب ايدي"""
from telethon import events
from telethon.utils import pack_bot_file_id
from userbot.utils import admin_cmd


@borg.on(admin_cmd("جلب ايدي"))
async def _(event):
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        chat = await event.get_input_chat()
        r_msg = await event.get_reply_message()
        if r_msg.media:
            bot_api_file_id = pack_bot_file_id(r_msg.media)
            await event.edit("ايدي المحادثه: `{}`\nايدي الشخص: `{}`\nايدي فايل بوت: `{}`".format(str(event.chat_id), str(r_msg.from_id), bot_api_file_id))
        else:
            await event.edit("ايدي المحادثه: `{}`\nايدي الشخص: `{}`".format(str(event.chat_id), str(r_msg.from_id)))
    else:
        await event.edit("ايدي المحادثه: `{}`".format(str(event.chat_id)))
