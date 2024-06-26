import re, os, requests,pymongo
from telethon.sync import ( TelegramClient,events )
from func.dates import ( API_HASD ,
                         API_ID,
                         NUMERO,
                         APROVED,
                         CHAT_ID,
                         TOKEN,
                         get_bin_info,
                         getcards
                         
                         )

client = TelegramClient('SCRAPP', API_ID, API_HASD)
client.start(NUMERO)


def enviar(id,texto):

    params = {'chat_id': id,'caption': texto,'parse_mode': 'HTML','photo': 'https://imgur.com/a/oy8Iw8G','reply_markup': {'inline_keyboard': [[{'text': 'OWNER', 'url': 'https://t.me/deeeeppal'},{'text': 'GROUP SCRAPP ', 'url': 'https://t.me/levelinggroup'}],[{'text': 'PRECIOS SCRAPP', 'url': 'https://t.me/preciosscrapp'},]]}}
    requests.post(f'https://api.telegram.org/bot7201390658:AAFQM2dWf1jSfd2Ei4QThbEvfnO-LG-dKDg/sendPhoto', json=params)


@client.on(events.MessageEdited())
async def handler(event):

    getMsg = event.message.message.upper()  
    RexGex = r'\d{14,16}\|\d{1,2}\|\d{2,4}\|\d{3,4}'
    ScrCss = re.sub(RexGex, r'<code>\g<0></code>', getMsg)

    ccs = getcards(ScrCss)
    if ccs == False: return
    
    bin_info = get_bin_info(ccs[0])
    bina = ccs[0]
    
    for live in APROVED:
        if live in ScrCss:
            text = f'''<b>𝐋𝐄𝐕𝐄𝐋𝐈𝐍𝐆 𝐒𝐂𝐑𝐀𝐏𝐏 / 𝑷𝑹𝑬𝑴𝑰𝑼𝑵 

𝑭𝒊𝒏𝒅𝒆𝒓 𝑩𝒊𝒏 : #BIN{bin_info['number']}
𝑪𝑪: <code>{ccs[0]}|{ccs[1]}|{ccs[2]}|{ccs[3]}</code>
𝑺𝒕𝒂𝒕𝒖𝒔: Approved ✅
𝑹𝒆𝒔𝒑𝒐𝒏𝒔𝒆: <code>{live}</code>

𝑩𝒂𝒏𝒌: <code>{bina[:12]}xxxx|{ccs[1]}|{ccs[2]}|rnd</code> 
𝑩𝒂𝒏𝒌: <code>{bin_info['bank']}</code>
𝑰𝑵𝑭𝑶: {bin_info['type']} | {bin_info['vendor']} | {bin_info['level']} 
𝑪𝒐𝒖𝒏𝒕𝒓𝒚: {bin_info ['country']} [{bin_info['flag']}]</b>'''
            enviar(-1002153156891, text)
    

    text1 = f'''<b>𝐋𝐄𝐕𝐄𝐋𝐈𝐍𝐆 𝐒𝐂𝐑𝐀𝐏𝐏 / 𝐅𝐑𝐄𝐄

𝑭𝒊𝒏𝒅𝒆𝒓 𝑩𝒊𝒏 : #BIN{bin_info['number']}
𝑪𝑪: <code>{ccs[0]}|{ccs[1]}|{ccs[2]}|{ccs[3]}</code>

𝑬𝒙𝒕𝒓𝒂: <code>{bina[:12]}xxxx|{ccs[1]}|{ccs[2]}|rnd</code> 
𝑩𝒂𝒏𝒌: <code>{bin_info['bank']}</code>
𝑰𝑵𝑭𝑶: {bin_info['type']} | {bin_info['vendor']} | {bin_info['level']} 
𝑪𝒐𝒖𝒏𝒕𝒓𝒚: {bin_info ['country']} [{bin_info['flag']}]</b>'''
    enviar(-1002182276809, text1)
    

os.system("cls")

banner = """
    ____                          ___                       _    __
   / __ \  ___    _  __          /   | _      __  ____ _   (_)  / /_
  / /_/ / / _ \  | |/_/         / /| || | /| / / / __ `/  / /  / __/
 / _, _/ /  __/ _>  <          / ___ || |/ |/ / / /_/ /  / /  / /_
/_/ |_|  \___/ /_/|_|         /_/  |_||__/|__/  \__,_/  /_/   \__/
                                                𝗧𝗵𝗲𝗪𝗼𝗿𝗹𝗱𝗔𝗽𝗶𝘀 「🐉」

『⁣✪』User: 6411167257 
『⁣✪』Code by: @RexAwait 👑"""

print(banner)


client.run_until_disconnected()
