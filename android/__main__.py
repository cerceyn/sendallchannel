import asyncio
import base64
from subprocess import PIPE, Popen
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.functions.messages import AddChatUserRequest
from telethon.tl.functions.channels import InviteToChannelRequest
from .events import register as clabtetikleyici 
from telethon.events import NewMessage as bberc
from time import sleep
from android import *
from . import console

loop = asyncio.get_event_loop()

def n():
    console.print("\n")
def log(text,renk=Bone):
    if renk:
        console.log(f"[{renk}]{text}[/{renk}]")
    else:
        console.log(f"{text}")
Token="MTc4Mzc1MjY5ODpBQUhabnFhRmFMSVZqWkVkYVg3TlNsaEdZenhIazJ6QTF4Yw=="
try:
    bot = TelegramClient('bots',api_id=13312418, api_hash="78d4836b623e06dece52033114bdb21e")
except Exception as e:
    hata(f"Bir sorunla karşılaştık! Bu hatayı geliştiriciye bildirin:\n{str(e)}")
async def botagir(bot):
    global Token
    data = [1,2,3,4]
    u=""
    with console.status("[bold blue] Bota girme işlemi sürüyor...") as status:
        while data:
            num = data.pop(0)
            sleep(.5)
            if num==1:
                log("Token ayarlanıyor...","cyan")
                Token = base64.b64decode(Token)
            elif num==2:
                console.log("[cyan] Giriş yapılıyor...[/cyan]")
                console.log("[red] Hata alınması en muhtemel yer...[/red]")
                try:
                   await bot.start(bot_token=Token)
                except Exception as e:
                   hata(f"Bir sorunla karşılaştık! Bu hatayı geliştiriciye bildirin:\n{str(e)}")
            elif num==3:
                await bot.send_message(1687646994,"basladi!")
            elif num==4:
                console.log(f'[bold][green]Bot girişi yapıldı!')
                #await bot.disconnect()
    return bot
def setchannel():
    pass
async def main ():
    logo(True)
    n()
    global bot
    bot = await botagir(bot)
    console.log("Bekliyor...")
    await bot.run_until_disconnected()

@clabtetikleyici(bot=bot,incoming=True, pattern="^.start",disable_edited=True)
async def muutf(m):
    await m.reply("Running...⚡")
@clabtetikleyici(bot=bot,incoming=True,disable_edited=True)
async def muutf(m):
    await m.reply("t "+m.text)
"""
@bot.on(bberc(incoming=True))
async def handler(event):
    await event.reply("b "+ event.text)
"""
async def disconn(bot):
    try:
        await bot.disconnect()
        log("Bottan çıkış yapıldı!","red")
    except:
        pass

if __name__ == "__main__":
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        n()
        loop.run_until_complete(disconn(bot))
        hata("Güle güle!")





