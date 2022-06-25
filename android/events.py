# Copyright (C) 2022 CerceynLab LLC.
#
# Licensed under the GNU Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#

import sys
from asyncio import create_subprocess_shell as asyncsubshell
from asyncio import subprocess as asyncsub
from os import remove
from time import gmtime, strftime
from traceback import format_exc
from telethon.events import NewMessage as NW, MessageEdited as ME, StopPropagation as SP
from telethon.errors.rpcerrorlist import MessageIdInvalidError

PATTERNS = ".!/"
def register(bot,**args):
    """ Yeni bir etkinlik kaydedin. """
    pattern = args.get('pattern', None)
    sudo = args.get('sudo', False)
    sevgili = args.get('sevgili', False)
    replyneeded = args.get('replyneeded',False)
    disable_edited = args.get('disable_edited', False)
    groups_only = args.get('groups_only', False)
    trigger_on_fwd = args.get('trigger_on_fwd', False)
    trigger_on_inline = args.get('trigger_on_inline', False)
    disable_errors = args.get('disable_errors', False)
    notifyoff = args.get('notifyoff', False)

    if pattern:
        args["pattern"] = pattern.replace("^.", "^["+ PATTERNS + "]")
    if "disable_edited" in args:
        del args['disable_edited']

    if "ignore_unsafe" in args:
        del args['ignore_unsafe']

    if "groups_only" in args:
        del args['groups_only']

    if "disable_errors" in args:
        del args['disable_errors']

    if "trigger_on_fwd" in args:
        del args['trigger_on_fwd']
      
    if "trigger_on_inline" in args:
        del args['trigger_on_inline']

    if 'replyneeded' in args:
        del args['replyneeded']

    if 'notifyoff' in args:
        del args['notifyoff']

    if "incoming" not in args:
        args['outgoing'] = True


    def decorator(func):
        async def wrapper(check):
            send_to = check.chat_id
            
            if not trigger_on_fwd and check.fwd_from:
                return

            if check.via_bot_id and not trigger_on_inline:
                return
             
            if groups_only and not check.is_group:
                if not notifyoff:
                    try:
                        await check.edit("`⛔ Bunun bir grup olduğunu sanmıyorum. Bu plugini bir grupta dene! `")
                    except:
                        await check.respond("`⛔ Bunun bir grup olduğunu sanmıyorum. Bu plugini bir grupta dene! `")
                return

            if replyneeded and not check.is_reply:
                if not notifyoff:
                    try:
                        await check.edit("`🤰🏻Bir mesajı yanıtlamalısın!`")
                    except:
                        await check.respond("`🤰🏻 Bir mesajı yanıtlamalısın!`")
                return

            try:
                await func(check)
                

            except SP:
                raise SP
            except KeyboardInterrupt:
                pass
            except MessageIdInvalidError:
                try: 
                    await check.respond('__🗒️ ( **Hata** ) :: Plugine ait mesaj silinmiş gibi görünüyor..__')
                except:
                    pass
            except BaseException:
                if not disable_errors:
                    date = strftime("%Y-%m-%d %H:%M:%S", gmtime())

                    eventtext = str(check.text)
                    text = "**≛『 HATA RAPORU 』≛**\n"
                    link = "[Geliştiriciye](https://t.me/berce)"
                    if len(eventtext)<20:
                        text += f"\n**🗒️ Şu yüzden:** {eventtext}\n"
                    text += "\n✆ İsterseniz, bunu bildirebilirsiniz."
                    text += f"- sadece bu mesajı {link} gönderin."
                    text += "**Hata ve tarih haricinde hiçbir şey** kayıt edilmez.\n"

                    ftext = ""
                    ftext += "========== UYARI =========="
                    ftext += "\nBu dosya sadece burada yüklendi,"
                    ftext += "\nSadece hata ve tarih kısmını kaydettik,"
                    ftext += "\nGizliliğinize saygı duyuyoruz,"
                    ftext += "\nBurada herhangi bir gizli veri varsa"
                    ftext += "\nBu hata raporu olmayabilir, kimse verilerinize ulaşamaz.\n"
                    ftext += "--------HATA GUNLUGU--------\n"
                    ftext += "\n➢ Tarih: " + date
                    ftext += "\n➢ Grup ID: " + str(check.chat_id)
                    ftext += "\n➢ Gönderen kişinin ID: " + str(check.sender_id)
                    ftext += "\n\n➢ Olay Tetikleyici:\n"
                    ftext += str(check.text)
                    ftext += "\n\n➢ Hata metni:\n"
                    ftext += str(sys.exc_info()[1])
                    ftext += "\n\n\n➢ Geri izleme bilgisi: \n"
                    ftext += str(format_exc())
                    ftext += "\n\n--------HATA GUNLUGU BITIS--------"

                    file = open("error.log", "w+")
                    file.write(ftext)
                    file.close()

                    await check.client.send_file(send_to,
                                                 "error.log",
                                                 caption=text)
                    try:
                        remove("error.log")
                    except:
                        pass
        if not disable_edited:
            bot.add_event_handler(wrapper, ME(**args))
        bot.add_event_handler(wrapper, NW(**args))

        return wrapper

    return decorator

