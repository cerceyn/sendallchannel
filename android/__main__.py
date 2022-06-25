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
def log(text,renk=None):
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
                try:
                    await bot.send_message(1687646994,"basladi!")
                except:
                    noadded('Mesaj gönderilememe hatası!')
            elif num==4:
                console.log(f'[bold][green]Bot girişi yapıldı!')
                #await bot.disconnect()
    return bot
def setchannel(isp=0):
    import os
    sep = os.sep
    os.chdir(os.pardir)
    li = os.getcwd().split(sep)
    if li:
        print(li)
        if "home" in li: #termux
            oathh=os.getcwd() + sep + "s-a-c"
            try:
                os.makedirs(oathh)
            except FileExistsError:
                pass
            if isp == 0:
                with open(oathh+sep+"main.txt","w") as f:
                    neolsun=soru("Ana kanal ne olsun? Lütfen id'i yazın!")
                    onayl = onay(f"Ana kanal {neolsun} olsun mu?")
                   
                    if neolsun.startswith("-100") and onayl:
                        f.write(neolsun)
                        basarili("İşlem başarıyla tamamlandı!")
                    elif onayl==False:
                        setchannel (isp)
                    else:
                        log("Hatalı kanal id'si!","red")
                        f.write("None")
                return oathh+sep+"main.txt"
            elif isp == 1:
                with open(oathh+sep+"channel.txt","w") as f:
                    neolsun=soru("Eklenecek yan kanal ne olsun? Lütfen id'i yazın!")
                    onayl = onay(f"Yan kanallara {neolsun} eklensin mi ?")
                   
                    if neolsun.startswith("-100") and onayl:
                        f.write(neolsun)
                        basarili("İşlem başarıyla tamamlandı!")
                    elif onayl==False:
                        setchannel (isp)
                    else:
                        log("Hatalı kanal id'si!","red")
                        f.write("None")
                return oathh+sep+"channel.txt"

def getchannel (isp=0):
    import os
    sep = os.sep
    os.chdir(os.pardir)
    li = os.getcwd().split(sep)
    if li:
        print(li)
        if "home" in li: #termux
            oathh=os.getcwd() + sep + "s-a-c"
            try:
                os.makedirs(oathh)
            except FileExistsError:
                pass 
            if isp == 0:
                if os.path.isfile(oathh+sep+"main.txt"):
                    return oathh+sep+"main.txt"
                else:
                   return setchannel (isp)
            elif isp == 1:
                if os.path.isfile(oathh+sep+"channel.txt"):
                    return oathh+sep+"channel.txt"
                else:
                   return setchannel (isp)

async def main ():
    logo(True)
    n()
    bilgi("1:Botu başlat!\n2:Ana Kanal Ayarla veya Değiştir!\n3:Yan Kanal Ekle!")
    islem = soru("Yapacağınız işlemi seçin [1-2-3]?")
    if islem=="1":
        global bot
        mainpath= getchannel (0)
        channelpath= getchannel (1)
        bot = await botagir(bot)
        console.log("Bekliyor...")
        await bot.run_until_disconnected()
    elif islem=="2":
        setchannel ()
    elif islem=="3":
        setchannel (1)
    else:
        hata("Hatalı işlem seçimi!")

@clabtetikleyici(bot=bot,incoming=True, pattern="^.start",disable_edited=True)
async def muutf(m):
    await m.reply("Running...⚡")
@clabtetikleyici(bot=bot,incoming=True, pattern="^.setmaingroup(?: |$)(.*)",disable_edited=True)
async def muutf(m):
    string = afk_e.pattern_match.group(1)
    await m.reply("Set...⚡")

@clabtetikleyici(bot=bot,incoming=True,disable_edited=True)
async def muutf(m):
    if not m.text.startswith() in ["!","/"]:
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





