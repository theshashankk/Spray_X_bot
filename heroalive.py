
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

# ๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "๐๐๐๐๐๐๐๐๐"

# Thanks to Sipak bro and Raganork.. 
# animation Idea by @NOOB_GUY_OP (Sipakisking)
# Made by @ROMANTIC_KILLER...and thanks to @Crackexy for the logos...
# Kang with credits else gay...
# alive.py for รรลฎ$HรณpBรศ

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
pm_caption = "  __**๐๐๐๐๐๐๐๐๐ ๐๐ ๐๐๐๐๐ ๐๐๐ ๐๐๐๐๐ ๐๐ ๐๐๐๐**__\n\n"
pm_caption += f"โ `๐ท๐ด๐๐พ๐ฑ๐๐ธ๐ฝ๐ด:` [{DEFAULTUSER}](tg://user?id={mafia})\n"
pm_caption += f"โ `๐๐ด๐ป๐ด๐๐ท๐พ๐ฝ ๐๐ด๐๐๐ธ๐พ๐ฝ:` `1.15.0` \n"
pm_caption += f"โ `๐ท๐ด๐๐พ๐ฑ๐๐ธ๐ฝ๐ด ๐๐ด๐๐๐ธ๐พ๐ฝ:` `{mafiaversion}`\n"
pm_caption += f"โ `๐๐๐ณ๐พ:` `{sudou}`\n"
pm_caption += f"โ `๐ฒ๐ท๐ฐ๐ฝ๐ฝ๐ด๐ป:` [แดแดษชษด](https://t.me/MafiaBot_Support)\n"
pm_caption += f"โ `๐ท๐ด๐๐พ๐ฑ๐๐ธ๐ฝ๐ด ๐ป๐ด๐ฐ๐ณ๐ด๐:` [๐๐๐๐๐ฝ๐๐๐๐ ๐๐๐ผ๐ฟ๐๐](https://t.me/HerobrineLeader)\n"
pm_caption += f"โ `๐ฒ๐พ๐ฟ๐๐๐ธ๐ถ๐ท๐:` [Mafia Bot](https://github.com/H1M4N5HU0P/MAFIA-BOT)\n"
pm_caption += f"โค ๐๐๐๐๐๐๐๐ ๐๐: [ShashankxxD](t.me/xD_Shashank)\n"

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
