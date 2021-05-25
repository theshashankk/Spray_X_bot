
# Thanks to Sipak bro and Aryan.. 
# animation Idea by @NOOB_GUY_OP (Sipakisking) && @Hell boy_pikachu
# Made by @ROMANTIC_KILLER...and thanks to @Crackexy for the logos...
# Kang with credits else gay...
# Porting in Mafia Userbot by @H1M4N5HU0P

import asyncio
import random
from telethon import events
from userbot import ALIVE_NAME, mafiaversion
from userbot.utils import admin_cmd, sudo_cmd
from telethon.tl.types import ChannelParticipantsAdmins
from userbot.cmdhelp import CmdHelp

# 🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "𝐇𝐄𝐑𝐎𝐁𝐑𝐈𝐍𝐄"

# Thanks to Sipak bro and Raganork.. 
# animation Idea by @NOOB_GUY_OP (Sipakisking)
# Made by @ROMANTIC_KILLER...and thanks to @Crackexy for the logos...
# Kang with credits else gay...
# alive.py for ÂÝŮ$HópBØȚ

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

mafia = bot.uid

edit_time = 16
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/17d4b65bfae8799f04329.jpg"
""" =======================CONSTANTS====================== """
pm_caption = "  __**𝐇𝐄𝐑𝐎𝐁𝐑𝐈𝐍𝐄 𝐈𝐒 𝐀𝐋𝐈𝐕𝐄 𝐀𝐍𝐃 𝐑𝐄𝐀𝐃𝐘 𝐓𝐎 𝐒𝐏𝐀𝐌**__\n\n"
pm_caption += f"✘ `𝙷𝙴𝚁𝙾𝙱𝚁𝙸𝙽𝙴:` [{DEFAULTUSER}](tg://user?id={mafia})\n"
pm_caption += f"✘ `𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽:` `1.15.0` \n"
pm_caption += f"✘ `𝙷𝙴𝚁𝙾𝙱𝚁𝙸𝙽𝙴 𝚅𝙴𝚁𝚂𝙸𝙾𝙽:` `{mafiaversion}`\n"
pm_caption += f"✘ `𝚂𝚄𝙳𝙾:` `{sudou}`\n"
pm_caption += f"✘ `𝙲𝙷𝙰𝙽𝙽𝙴𝙻:` [ᴊᴏɪɴ](https://t.me/MafiaBot_Support)\n"
pm_caption += f"✘ `𝙷𝙴𝚁𝙾𝙱𝚁𝙸𝙽𝙴 𝙻𝙴𝙰𝙳𝙴𝚁:` [𝙃𝙀𝙍𝙊𝘽𝙍𝙄𝙉𝙀 𝙇𝙀𝘼𝘿𝙀𝙍](https://t.me/HerobrineLeader)\n"
pm_caption += f"✘ `𝙲𝙾𝙿𝚈𝚁𝙸𝙶𝙷𝚃:` [Mafia Bot](https://github.com/H1M4N5HU0P/MAFIA-BOT)\n"
pm_caption += f"➤ 𝐌𝐎𝐃𝐈𝐅𝐈𝐄𝐃 𝐁𝐘: [ShashankxxD](t.me/xD_Shashank)\n"

@bot.on(admin_cmd(outgoing=True, pattern="hero$"))
@bot.on(sudo_cmd(pattern="hero$", allow_sudo=True))
async def amireallyalive(alive):
    await alive.get_chat()   
    await alive.delete()
    on = await borg.send_file(alive.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(alive.chat_id, on, file=file2) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(alive.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(alive.chat_id, ok2, file=file1)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(alive.chat_id, ok3, file=file3)
    
    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(alive.chat_id, ok4, file=file2)
    
    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(alive.chat_id, ok5, file=file4)
    
    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(alive.chat_id, ok6, file=file1)
    
    await asyncio.sleep(edit_time)
    ok8 = await borg.edit_message(alive.chat_id, ok7, file=file2) 

    await asyncio.sleep(edit_time)
    ok9 = await borg.edit_message(alive.chat_id, ok8, file=file3)

    await asyncio.sleep(edit_time)
    ok10 = await borg.edit_message(alive.chat_id, ok9, file=file1)
    
    await asyncio.sleep(edit_time)
    ok11 = await borg.edit_message(alive.chat_id, ok10, file=file3)
    
    await asyncio.sleep(edit_time)
    ok12 = await borg.edit_message(alive.chat_id, ok11, file=file2)
    
    await asyncio.sleep(edit_time)
    ok13 = await borg.edit_message(alive.chat_id, ok12, file=file4)
    
    await asyncio.sleep(edit_time)
    ok14 = await borg.edit_message(alive.chat_id, on, file=file1)

    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, caption=pm_caption)
    await alive.delete()
    
    
CmdHelp("hero").add_command(
  "hero", None, "herobrine Official plugin"
).add_command(
  "hero", None, "To check am i jindq"
).add()
