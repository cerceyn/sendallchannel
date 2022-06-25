import asyncio
import base64
from subprocess import PIPE, Popen
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.functions.messages import AddChatUserRequest
from telethon.tl.functions.channels import InviteToChannelRequest
from time import sleep
from android import *
from . import console
def n():
    console.print("\n")
Token="MTc1ODU4MTE4NTpBQUc4YlQteTFPMDJNRW5EMmlqR3hzRGx6MXE3dEMyZWR1TQ=="
bot=None
async def botagir(bot):
    global Token
    data = [1,2,3,4]
    with console.status("[bold blue] Bota girme işlemi sürüyor...") as status:
        while data:
            num = data.pop(0)
            sleep(2)
            if num==1:
                console.log("[cyan] Token ayarlanıyor...[/cyan]")
                Token = base64.b64decode(Token)
            elif num==2:
                console.log("[cyan] Api bilgileri ayrıştırılıyor...[/cyan]")
                print (u)
                u = base64.b64decode("NzhkNDgzNmI2MjNlMDZkZWNlNTIwMzMxMTRiZGIyMWV8MTMzMTI0MTg=")
                api_id = int(u.split('|')[1]);api_hash=u.split('|')[0]
                console.log("[cyan] Api bilgileri:\n id: {}\nhash: {}..[/cyan]".format(api_id,api_hash))
                try:
                   bot = TelegramClient('bots',api_id=api_id, api_hash=api_hash)
                except Exception as e:
                   hata(f"Bir sorunla karşılaştık! Bu hatayı geliştiriciye bildirin:\n{str(e)}")
            elif num==3:
                console.log("[cyan] Giriş yapılıyor...[/cyan]")
                console.log("[red] Hata alınması en muhtemel yer...[/red]")
                try:
                   await bot.start(bot_token=Token)
                except Exception as e:
                   hata(f"Bir sorunla karşılaştık! Bu hatayı geliştiriciye bildirin:\n{str(e)}")
            elif num==4:
                console.log(f'[bold][red]Tamam!')
                await bot.disconnect()

async def main ():
    logo(True)
    n()
    global bot
    await botagir(bot)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        hata("Güle güle!")
        #loop.run_until_complete(disconn(userbot))





