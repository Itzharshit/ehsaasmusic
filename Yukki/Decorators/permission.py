from typing import Dict, List, Union

from Yukki import BOT_ID, app


def PermissionCheck(mystic):
    async def wrapper(_, message):
        a = await app.get_chat_member(message.chat.id, BOT_ID)
        if a.status != "administrator":
            return await message.reply_text(
                "𝙄 𝙣𝙚𝙚𝙙 𝙩𝙤 𝙗𝙚 𝙖𝙙𝙢𝙞𝙣 𝙬𝙞𝙩𝙝 𝙨𝙤𝙢𝙚 𝙥𝙚𝙧𝙢𝙞𝙨𝙨𝙞𝙤𝙣𝙨.:\n"
                + "\n- **can_manage_voice_chats:** To manage voice chats"
                + "\n- **can_delete_messages:** To delete Bot's Searched Waste"
                + "\n- **can_invite_users**: For inviting assistant to chat."
            )
        if not a.can_manage_voice_chats:
            await message.reply_text(
                "𝙄 𝙙𝙤𝙣'𝙩 𝙝𝙖𝙫𝙚 𝙩𝙝𝙚 𝙧𝙚𝙦𝙪𝙞𝙧𝙚𝙙 𝙥𝙚𝙧𝙢𝙞𝙨𝙨𝙞𝙤𝙣 𝙩𝙤 𝙥𝙚𝙧𝙛𝙤𝙧𝙢 𝙩𝙝𝙞𝙨 𝙖𝙘𝙩𝙞𝙤𝙣."
                + "\n**𝙋𝙚𝙧𝙢𝙞𝙨𝙨𝙞𝙤𝙣:** __MANAGE VOICE CHATS__"
            )
            return
        if not a.can_delete_messages:
            await message.reply_text(
                "𝙄 𝙙𝙤𝙣'𝙩 𝙝𝙖𝙫𝙚 𝙩𝙝𝙚 𝙧𝙚𝙦𝙪𝙞𝙧𝙚𝙙 𝙥𝙚𝙧𝙢𝙞𝙨𝙨𝙞𝙤𝙣 𝙩𝙤 𝙥𝙚𝙧𝙛𝙤𝙧𝙢 𝙩𝙝𝙞𝙨 𝙖𝙘𝙩𝙞𝙤𝙣."
                + "\n**𝙋𝙚𝙧𝙢𝙞𝙨𝙨𝙞𝙤𝙣:** __DELETE MESSAGES__"
            )
            return
        if not a.can_invite_users:
            await message.reply_text(
                "𝙄 𝙙𝙤𝙣'𝙩 𝙝𝙖𝙫𝙚 𝙩𝙝𝙚 𝙧𝙚𝙦𝙪𝙞𝙧𝙚𝙙 𝙥𝙚𝙧𝙢𝙞𝙨𝙨𝙞𝙤𝙣 𝙩𝙤 𝙥𝙚𝙧𝙛𝙤𝙧𝙢 𝙩𝙝𝙞𝙨 𝙖𝙘𝙩𝙞𝙤𝙣."
                + "\n**𝙋𝙚𝙧𝙢𝙞𝙨𝙨𝙞𝙤𝙣:** __INVITE USERS VIA LINK__"
            )
            return
        return await mystic(_, message)

    return wrapper
