from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.functions.messages import AddChatUserRequest
from .events import register as clabtetikleyici 
from telethon.events import NewMessage as bberc
from telethon.errors import PeerIdInvalidError
from telethon.sessions import StringSession
from telethon import TelegramClient
from subprocess import PIPE, Popen
from rich import print as rprint
from telethon import types
from time import sleep
from android import *
import asyncio
import base64

loop = asyncio.get_event_loop()

def n():
    console.print("\n")
def log(text,renk=None):
    if renk:
        console.log(f"[{renk}]{text}[/{renk}]")
    else:
        console.log(f"{text}")
Token="MTc4Mzc1MjY5ODpBQUhfVktvOWp6STV4bHVpT1dDV3lmTWdfUlRQc0dUbzZkbw=="
try:
    bot = TelegramClient('bots',api_id=13312418, api_hash="78d4836b623e06dece52033114bdb21e")
except Exception as e:
    hata(f"Bir sorunla karşılaştık! Bu hatayı geliştiriciye bildirin:\n{str(e)}")
async def botagir():
    global bot
    data = [1,2,3,4]
    u=""
    n()
    with console.status("[bold blue] Bota girme işlemi sürüyor...") as status:
        while data:
            num = data.pop(0)
            sleep(.5)
            if num==1:
                log("🔑 Token ayarlanıyor...","cyan")
                token = base64.b64decode(Token)
            elif num==2:
                console.log("[cyan] 🎟️ Giriş yapılıyor...[/cyan]")
                console.log("[red] 🎟️ Hata alınması en muhtemel yer...[/red]")
                await bot.start(bot_token=token)
                bot.parse_mode="html"
            elif num==3:
                try:
                    await bot.send_message(842063238,"⌛ Bot başladı!")
                except:
                    noadded('Mesaj gönderilememe hatası!')
            elif num==4:
                console.log(f'[bold][green]✅ Bot girişi yapıldı!')
                #await bot.disconnect()
    return bot
async def setchannel(isp=0,pprint=True,forceadd=""):
    global eklenecek; eklenecek=True
    import os
    sep = os.sep
    li = os.getcwd().split(sep)
    if pprint:bilgi(li[-1])
    passed("Dizin ayarlanıyor")
    if "home" in li: #termux
        while True:
            if not li[-1] == "home": #termux
                os.chdir(os.pardir)
            else:
                break
            li = os.getcwd().split(sep)
    else:
        hata("Geçersiz işletim sistemi!")
    li = os.getcwd().split(sep)

    if li:
        if pprint:rprint(li)
        if li:
            oathh=os.getcwd() + sep + "s-a-c"
            try:
                os.makedirs(oathh)
            except FileExistsError:
                pass
            if isp == 0:
                error=False
                with open(oathh+sep+"main.txt","w") as f:
                    if forceadd == "":
                        neolsun=soru("🍀 Ana kanal ne olsun? Lütfen id'i yazın!")
                        onayl = onay(f"Ana kanal '{neolsun}' olsun mu ?")
                        try:
                            neolsunn = int(neolsun)
                        except ValueError:
                            noadded("Lütfen bir kanal id yazın!");error=True
                   
                        if neolsun.startswith("-100") and onayl:
                            f.write(neolsun);basarili("✅ İşlem başarıyla tamamlandı!")
                        elif onayl==False:
                            return await setchannel (isp, False, forceadd)
                        else:
                            log("Hatalı kanal id'si!","red");error=True
                    else: f.write(adds+forceadd);basarili("✅ Force ({}) başarıyla tamamlandı!".format(forceadd))
                if error:
                    if os.path.isfile(oathh+sep+"main.txt"): os.remove(oathh+sep+"main.txt")
                    return await setchannel (isp, False, forceadd)
                eklenecek=False
                return oathh+sep+"main.txt"
            elif isp == 1:
                error=False
                if os.path.isfile(oathh+sep+"channel.txt"):adds="\n"
                else:adds=""
                try:
                    with open(oathh+sep+"channel.txt","r") as f:
                        channelsss=f.read().split('\n')
                except FileNotFoundError: channelsss=[]
                with open(oathh+sep+"channel.txt","a") as f:
                    if forceadd == "":
                        neolsun=soru("🍀 Eklenecek yan kanal ne olsun? Lütfen id'i yazın!")
                        onayl = onay(f"Yan kanallara '{neolsun}' eklensin mi ?")
                        try:
                            neolsunn = int(neolsun)
                        except ValueError:
                            noadded("Lütfen bir kanal id yazın!");error=True
                        if neolsun in channelsss:noadded("Bu kadar zaten daha önceden eklenmiş!")
                        elif neolsun.startswith("-100") and onayl:
                            f.write(adds+neolsun);basarili("✅ İşlem başarıyla tamamlandı!")
                        elif onayl==False:
                            return await setchannel (isp,False, forceadd)
                        else:
                            log("Hatalı kanal id'si!","red");error=True
                    else: f.write(adds+forceadd);basarili("✅ Force ({}) başarıyla tamamlandı!".format(forceadd))
                if error:
                    if os.path.isfile(oathh+sep+"channel.txt"): os.remove(oathh+sep+"channel.txt")
                    return await setchannel (isp, False, forceadd)
                eklenecek=False
                return oathh+sep+"channel.txt"

async def getchannel (isp=0,pprint=True):
    import os
    sep = os.sep
    li = os.getcwd().split(sep)
    if pprint:bilgi(li[-1])
    passed("Dizin ayarlanıyor")
    if "home" in li: #termux
        while True:
            if not li[-1] == "home": #termux
                os.chdir(os.pardir)
            else:
                break
            li = os.getcwd().split(sep)
    else:
        hata("Geçersiz işletim sistemi!")
    li = os.getcwd().split(sep)
    if li:
        if pprint:rprint(li)
        if li:
            oathh=os.getcwd() + sep + "s-a-c"
            try:
                os.makedirs(oathh)
            except FileExistsError:
                pass 
            if isp == 0:
                if os.path.isfile(oathh+sep+"main.txt"):
                    with open(oathh+sep+"main.txt","r") as f:
                        file = f.read()
                    if not file.split('\n')[0].startswith("-100"):
                        await setchannel (isp,False); return await getchannel (isp,False)
                    return file.split('\n')[0]
                else:
                    await setchannel (isp,False); return await getchannel (isp,False)
            elif isp == 1:
                if os.path.isfile(oathh+sep+"channel.txt"):
                    with open(oathh+sep+"channel.txt","r") as f:
                        file = f.read()
                    if not file.split('\n')[0].startswith("-100"):
                        await setchannel (isp,False); return await getchannel (isp,False)
                    return file.split('\n')
                else:
                    await setchannel (isp,False); return await getchannel (isp,False)
    return None

async def forchannel(bot,channelpath,message):
    bilgi ("Perceived: ")
    onemli(channelpath)
    basarilic=0
    mesj = await bot.get_messages(message.chat_id, ids=message.id)
    bilgi("Kopyalanacak mesaj hazır!")
    for chnl in channelpath:
        if chnl == "":continue 
        if chnl.startswith("-100"):
            bilgi("Şuraya mesaj gönderilmeye çalışılıyor..: {}".format(chnl))
            try:
                chat=await bot.get_entity(int(chnl))
                await bot.send_message(chat.id,mesj)
                log("Mesaj {} kanalına gönderildi!".format(chat.id),"green")
                basarilic+=1
            except PeerIdInvalidError:
                noadded("Kanal ID'si({}) hatalı, lütfen bunu silin!".format (chnl))
            except Exception as e:
                noadded("✖️ Yan kanallardan '{}' mesaj atılmadı! Hata: {}".format(chnk,str(e)))
        else:
            try:
                chat=await bot.get_entity(int(chnl)) #types.PeerChannel(int(chnl))
                await bot.send_message(chat,mesj)
                log("Mesaj {} kanalına gönderildi!".format(chat.id),"green")
                basarilic+=1
            except Exception as e:
                noadded("✖️ Yan kanallardan '{}' mesaj atılmadı! Hata: {}".format(chnl,str(e)))
    return basarilic

mainpath= ""
channelpath=""
async def main ():
    statusz="ads"
    if os.name!="nt": os.system("clear")
    else: os.system("cls")
    while True:
        logo(True)
        if statusz=="ads":ads("Free trial bitiş süresi: 31 gün"); statusz=None
        elif statusz:
            passed(statusz);statusz=None
        passed("İşlemler:\n\n🍀 1:Botu başlat!\n🍀 2:Ana Kanal Ayarla veya Değiştir!\n🍀 3:Yan Kanal Ekle!\n🍀 4:Çıkış")
        try:
            islem = soru_("Yapacağınız işlemi seçin [1-4]?")
        except:
            await disconn ()
        if islem=="1":
            global bot, mainpath, channelpath 
            mainpath= await getchannel (0)
            channelpath= await getchannel (1)
            bot = await botagir()
            n()
            log("💨💨 Şimdi botunuz çalışıyor ve ana kanalınızda birşey paylaşmanız bekleniyor...","green")
            statusz="Bottan çıkış yapıldı!"
            with console.status("[bold thistle1]⌛ Bot çalışıyor, durdurmak için Ctrl C yapın!") as status:
                try:
                    await bot.run_until_disconnected()
                except KeyboardInterrupt:
                    pass #raise KeyboardInterrupt("Çıkış!")
            await disconn ()
        elif islem=="2":
            statusz="Ana kanal işlemlerinden çıkıldı!"
            await setchannel ()
            onayl = onay("Başka bir işlem yapmak ister misiniz?")
            if onayl:continue
            else:break
        elif islem=="3":
            statusz="Yan kanal işlemlerinden çıkıldı!"
            await setchannel (1)
            onayl = onay("Başka bir işlem yapmak ister misiniz?")
            if onayl:continue
            else: break
        elif islem=="4":
            break
        if islem not in ["1","2","3","4"]:
            statusz= "Hatalı işlem seçimi!"; continue 

@clabtetikleyici(bot=bot,incoming=True, pattern="^.start",disable_edited=True)
async def muutf(m):
    await m.reply("Running...⚡")

@clabtetikleyici(bot=bot,incoming=True, pattern="^.maingroup(?: |$)(.*)",disable_edited=True)
async def muutf(m):
    #string = m.pattern_match.group(1)
    await m.reply("🆔: {}".format(mainpath))

@clabtetikleyici(bot=bot,incoming=True, pattern="^.channels(?: |$)(.*)",disable_edited=True)
async def muutf(m):
    await m.respond("📋: {}".format(str(channelpath)))
    text=""
    for i in channelpath:
        text+="🆔: {}\n".format(i)
    await m.respond("{}".format(text))


@clabtetikleyici(bot=bot,incoming=True,groups_only=True,disable_edited=True)
async def muutf(m):
    if int(m.chat_id)==int(mainpath) :
        try:
            msg=await bot.send_message(842063238,"🔄 Yeni bir post tespit edildi,gönderiliyor...")
        except:
            noadded('Mesaj gönderilememe hatası!')

        basarilic = await forchannel (m.client, channelpath, m)
        try:
            await msg.edit("✅ İşlem tamamlandı! {} adet kanala post iletildi!".format(str(basarilic)))
        except:
            pass

        #else:
        #await m.reply("✉️: {}".format(str(m)))
    else:
        bilgi(f"Şuradan bir mesaj algılandım🌀: {m.chat_id}")
eklenecek=False

@clabtetikleyici(bot=bot,incoming=True,groups_only=False,disable_edited=True,trigger_on_fwd=True)
async def muutf(m):
    if m.fwd_from and m.views:
        await m.reply("🆔: <i>Kanal ID:</i> {}".format(m.fwd_from.from_id))


"""
@bot.on(bberc(incoming=True))
async def handler(event):
    await event.reply("b "+ event.text)
"""
async def disconn():
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
        loop.run_until_complete(disconn())
        hata("Güle güle!")






