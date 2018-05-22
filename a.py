# -*- coding: utf-8 -*-

from LineAPI.linepy import *
from LineAPI.akad.ttypes import Message
from LineAPI.akad.ttypes import ContentType as Type
from gtts import gTTS
from time import sleep
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from googletrans import Translator
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, six, ast, pytz, urllib, urllib3, urllib.parse, traceback, atexit, subprocess

cl = LINE()
#ririn = LINE("TOKENMU")

ririnMid = cl.profile.mid
ririnProfile = cl.getProfile()
ririnSettings = cl.getSettings()
ririnPoll = OEPoll(cl)
botStart = time.time()

print ("╔═════════════════════════\n║╔════════════════════════\n║╠❂➣ DNA BERHASIL LOGIN\n║╚════════════════════════\n╚═════════════════════════")

msg_dict = {}

wait = {
    "autoAdd": True,
    "autoJoin": True,
    "autoLeave": False,
    "autoRead": False,
    "autoRespon": True,
    "autoResponPc": False,
    "autoJoinTicket": True,
    "checkContact": False,
    "checkPost": False,
    "checkSticker": False,
    "changePictureProfile": False,
    "changeGroupPicture": [],
    "keyCommand": "",
    "leaveRoom": True,
    "myProfile": {
        "displayName": "",
        "coverId": "",
        "pictureStatus": "",
        "statusMessage": ""
    },
    "mimic": {
        "copy": False,
        "status": False,
        "target": {}
    },
    "Protectcancel": True,
    "Protectgr": True,
    "Protectinvite": True,
    "Protectjoin": False,
    "setKey": False,
    "sider": False,
    "unsendMessage": True
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

read = {
    "ROM": {},
    "readPoint": {},
    "readMember": {},
    "readTime": {}
}

list_language = {
    "list_textToSpeech": {
        "id": "Indonesia",
        "af" : "Afrikaans",
        "sq" : "Albanian",
        "ar" : "Arabic",
        "hy" : "Armenian",
        "bn" : "Bengali",
        "ca" : "Catalan",
        "zh" : "Chinese",
        "zh-cn" : "Chinese (Mandarin/China)",
        "zh-tw" : "Chinese (Mandarin/Taiwan)",
        "zh-yue" : "Chinese (Cantonese)",
        "hr" : "Croatian",
        "cs" : "Czech",
        "da" : "Danish",
        "nl" : "Dutch",
        "en" : "English",
        "en-au" : "English (Australia)",
        "en-uk" : "English (United Kingdom)",
        "en-us" : "English (United States)",
        "eo" : "Esperanto",
        "fi" : "Finnish",
        "fr" : "French",
        "de" : "German",
        "el" : "Greek",
        "hi" : "Hindi",
        "hu" : "Hungarian",
        "is" : "Icelandic",
        "id" : "Indonesian",
        "it" : "Italian",
        "ja" : "Japanese",
        "km" : "Khmer (Cambodian)",
        "ko" : "Korean",
        "la" : "Latin",
        "lv" : "Latvian",
        "mk" : "Macedonian",
        "no" : "Norwegian",
        "pl" : "Polish",
        "pt" : "Portuguese",
        "ro" : "Romanian",
        "ru" : "Russian",
        "sr" : "Serbian",
        "si" : "Sinhala",
        "sk" : "Slovak",
        "es" : "Spanish",
        "es-es" : "Spanish (Spain)",
        "es-us" : "Spanish (United States)",
        "sw" : "Swahili",
        "sv" : "Swedish",
        "ta" : "Tamil",
        "th" : "Thai",
        "tr" : "Turkish",
        "uk" : "Ukrainian",
        "vi" : "Vietnamese",
        "cy" : "Welsh"
    },
    "list_translate": {    
        "af": "afrikaans",
        "sq": "albanian",
        "am": "amharic",
        "ar": "arabic",
        "hy": "armenian",
        "az": "azerbaijani",
        "eu": "basque",
        "be": "belarusian",
        "bn": "bengali",
        "bs": "bosnian",
        "bg": "bulgarian",
        "ca": "catalan",
        "ceb": "cebuano",
        "ny": "chichewa",
        "zh-cn": "chinese (simplified)",
        "zh-tw": "chinese (traditional)",
        "co": "corsican",
        "hr": "croatian",
        "cs": "czech",
        "da": "danish",
        "nl": "dutch",
        "en": "english",
        "eo": "esperanto",
        "et": "estonian",
        "tl": "filipino",
        "fi": "finnish",
        "fr": "french",
        "fy": "frisian",
        "gl": "galician",
        "ka": "georgian",
        "de": "german",
        "el": "greek",
        "gu": "gujarati",
        "ht": "haitian creole",
        "ha": "hausa",
        "haw": "hawaiian",
        "iw": "hebrew",
        "hi": "hindi",
        "hmn": "hmong",
        "hu": "hungarian",
        "is": "icelandic",
        "ig": "igbo",
        "id": "indonesian",
        "ga": "irish",
        "it": "italian",
        "ja": "japanese",
        "jw": "javanese",
        "kn": "kannada",
        "kk": "kazakh",
        "km": "khmer",
        "ko": "korean",
        "ku": "kurdish (kurmanji)",
        "ky": "kyrgyz",
        "lo": "lao",
        "la": "latin",
        "lv": "latvian",
        "lt": "lithuanian",
        "lb": "luxembourgish",
        "mk": "macedonian",
        "mg": "malagasy",
        "ms": "malay",
        "ml": "malayalam",
        "mt": "maltese",
        "mi": "maori",
        "mr": "marathi",
        "mn": "mongolian",
        "my": "myanmar (burmese)",
        "ne": "nepali",
        "no": "norwegian",
        "ps": "pashto",
        "fa": "persian",
        "pl": "polish",
        "pt": "portuguese",
        "pa": "punjabi",
        "ro": "romanian",
        "ru": "russian",
        "sm": "samoan",
        "gd": "scots gaelic",
        "sr": "serbian",
        "st": "sesotho",
        "sn": "shona",
        "sd": "sindhi",
        "si": "sinhala",
        "sk": "slovak",
        "sl": "slovenian",
        "so": "somali",
        "es": "spanish",
        "su": "sundanese",
        "sw": "swahili",
        "sv": "swedish",
        "tg": "tajik",
        "ta": "tamil",
        "te": "telugu",
        "th": "thai",
        "tr": "turkish",
        "uk": "ukrainian",
        "ur": "urdu",
        "uz": "uzbek",
        "vi": "vietnamese",
        "cy": "welsh",
        "xh": "xhosa",
        "yi": "yiddish",
        "yo": "yoruba",
        "zu": "zulu",
        "fil": "Filipino",
        "he": "Hebrew"
    }
}

try:
    with open("Log_data.json","r",encoding="utf_8_sig") as f:
        msg_dict = json.loads(f.read())
except:
    print("Couldn't read Log data")
    
wait["myProfile"]["displayName"] = clProfile.displayName
wait["myProfile"]["statusMessage"] = clProfile.statusMessage
wait["myProfile"]["pictureStatus"] = clProfile.pictureStatus
coverId = ririn.getProfileDetail()["result"]["objectId"]
wait["myProfile"]["coverId"] = coverId

def restartBot():
    print ("[ INFO ] BOT RESTART")
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def logError(text):
    ririn.log("[ ERROR ] {}".format(str(text)))
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = "{}, {} - {} - {} | {}".format(str(hasil), str(inihari.strftime('%d')), str(bln), str(inihari.strftime('%Y')), str(inihari.strftime('%H:%M:%S')))
    with open("logError.txt","a") as error:
        error.write("\n[ {} ] {}".format(str(time), text))

def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > timedelta(1):
            if "path" in msg_dict[data]:
                ririn.deleteFile(msg_dict[data]["path"])
            del msg_dict[data]
            
def sendMention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@dee "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def command(text):
    pesan = text.lower()
    if wait["setKey"] == True:
        if pesan.startswith(wait["keyCommand"]):
            cmd = pesan.replace(wait["keyCommand"],"")
        else:
            cmd = "Undefined command"
    else:
        cmd = text.lower()
    return cmd

def help():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage = "• Gunakan「 " + key + " 」di depannya\n\n" + \
                  "「✭」 " + key + "Me\n" + \
                  "「✭」 " + key + "Mid「@」\n" + \
                  "「✭」 " + key + "Steal「@」\n" + \
                  "「✭」 " + key + "Cover「@」\n" + \
                  "「✭」 " + key + "Nk「@」\n" + \
                  "「✭」 " + key + "Kick1「@」\n" + \
                  "「✭」 " + key + "Clone「@」\n" + \
                  "「✭」 " + key + "Restore\n" + \
                  "「✭」 " + key + "Reject\n" + \
                  "「✭」 " + key + "Mybot\n" + \
                  "「✭」 " + key + "Setting\n" + \
                  "「✭」 " + key + "About\n" + \
                  "「✭」 " + key + "Restart\n" + \
                  "「✭」 " + key + "Runtime\n" + \
                  "「✭」 " + key + "Creator\n" + \
                  "「✭」 " + key + "Speed/Sp\n" + \
                  "「✭」 " + key + "Respontime\n" + \
                  "「✭」 " + key + "Tagall\n" + \
                  "「✭」 " + key + "Joinall\n" + \
                  "「✭」 " + key + "Byeall\n" + \
                  "「✭」 " + key + "Bye me\n" + \
                  "「✭」 " + key + "Leave「Namagrup」\n" + \
                  "「✭」 " + key + "Ginfo\n" + \
                  "「✭」 " + key + "Open\n" + \
                  "「✭」 " + key + "Close\n" + \
                  "「✭」 " + key + "Url\n" + \
                  "「✭」 " + key + "Gruplist\n" + \
                  "「✭」 " + key + "Open「nomer」\n" + \
                  "「✭」 " + key + "Close「nomer」\n" + \
                  "「✭」 " + key + "Infogrup「nomer」\n" + \
                  "「✭」 " + key + "Infomem「nomer」\n" + \
                  "「✭」 " + key + "Joinall「nomer」\n" + \
                  "「✭」 " + key + "Leaveall「nomer」\n" + \
                  "「✭」 " + key + "Remove chat\n" + \
                  "「✭」 " + key + "Lurking「on/off」\n" + \
                  "「✭」 " + key + "Lurkers\n" + \
                  "「✭」 " + key + "Sider「on/off」\n" + \
                  "「✭」 " + key + "Updatefoto\n" + \
                  "「✭」 " + key + "Updategrup\n" + \
                  "「✭」 " + key + "Updatebot\n" + \
                  "「✭」 " + key + "Broadcast:「Text」\n" + \
                  "「✭」 " + key + "Setkey「New Key」\n" + \
                  "「✭」 " + key + "Mykey\n" + \
                  "「✭」 " + key + "Resetkey\n" + \
                  "\n「 Turn In Media 」\n• Use「 " + key + " 」di depannya\n\n" + \
                  "「✭」 " + key + "Kode wilayah\n" + \
                  "「✭」 " + key + "Listmp3\n" + \
                  "「✭」 " + key + "Listvideo\n" + \
                  "「✭」 " + key + "Listimage\n" + \
                  "「✭」 " + key + "Liststicker\n" + \
                  "「✭」 " + key + "Addimg「Teks」\n" + \
                  "「✭」 " + key + "Dellimg「Teks」\n" + \
                  "「✭」 " + key + "Addmp3「Teks」\n" + \
                  "「✭」 " + key + "Dellmp3「Teks」\n" + \
                  "「✭」 " + key + "Addvideo「Teks」\n" + \
                  "「✭」 " + key + "Dellvideo「Teks」\n" + \
                  "「✭」 " + key + "Addsticker「Teks」\n" + \
                  "「✭」 " + key + "Dellsticker「Teks」\n" + \
                  "「✭」 " + key + "Spamtag:「jumlahnya」\n" + \
                  "「✭」 " + key + "Spamtag「@」\n" + \
                  "「✭」 " + key + "Spamcall:「jumlahnya」\n" + \
                  "「✭」 " + key + "Spamcall\n" + \
                  "「✭」 " + key + "Musik「Nama Penyanyi」\n" + \
                  "「✭」 " + key + "Get-fs「Query」\n" + \
                  "「✭」 " + key + "Get-line「ID Line」\n" + \
                  "「✭」 " + key + "Get-apk「Query」\n" + \
                  "「✭」 " + key + "Get-gif「Query」\n" + \
                  "「✭」 " + key + "Get-xxx「Query」\n" + \
                  "「✭」 " + key + "Get-anime「Query」\n" + \
                  "「✭」 " + key + "Get-mimpi「Query」\n" + \
                  "「✭」 " + key + "Get-audio「Query」\n" + \
                  "「✭」 " + key + "Get-mp3「Query」\n" + \
                  "「✭」 " + key + "Get-video「Query」\n" + \
                  "「✭」 " + key + "Get-bintang「Zodiak」\n" + \
                  "「✭」 " + key + "Get-zodiak「Zodiak」\n" + \
                  "「✭」 " + key + "Get-sholat「Nama Kota」\n" + \
                  "「✭」 " + key + "Get-cuaca「Nama Kota」\n" + \
                  "「✭」 " + key + "Get-lokasi「Nama Kota」\n" + \
                  "「✭」 " + key + "Get-lirik「Judul Lagu」\n" + \
                  "「✭」 " + key + "Get-instagram「User Name」\n" + \
                  "「✭」 " + key + "Get-date「tgl-bln-thn」\n" + \
                  "\n「 Setting Protection 」\n• Use「 " + key + " 」di depannya\n\n" + \
                  "「✭」 " + key + "Notag「on/off」\n" + \
                  "「✭」 " + key + "Protecall「on/off」\n" + \
                  "「✭」 " + key + "Protecturl「on/off」\n" + \
                  "「✭」 " + key + "Protectjoin「on/off」\n" + \
                  "「✭」 " + key + "Protectkick「on/off」\n" + \
                  "「✭」 " + key + "Protectinvite「on/off」\n" + \
                  "「✭」 " + key + "Protectcancel「on/off」\n" + \
                  "\n「 Setting User 」\n• Use「 " + key + " 」di depannya\n\n" + \
                  "「✭」 " + key + "Invite「on/off」\n" + \
                  "「✭」 " + key + "Sticker「on/off」\n" + \
                  "「✭」 " + key + "Unsend「on/off」\n" + \
                  "「✭」 " + key + "Respon「on/off」\n" + \
                  "「✭」 " + key + "Timeline「on/off」\n" + \
                  "「✭」 " + key + "Contact「on/off」\n" + \
                  "「✭」 " + key + "Autojoin「on/off」\n" + \
                  "「✭」 " + key + "Autoadd「on/off」\n" + \
                  "「✭」 " + key + "Welcome「on/off」\n" + \
                  "「✭」 " + key + "Autoleave「on/off」\n" + \
                  "「✭」 " + key + "Jointicket「on/off」\n" + \
                  "\n「 For Admin 」\n• Use「 " + key + " 」di depannya\n\n" + \
                  "「✭」 " + key + "Bot:on\n" + \
                  "「✭」 " + key + "Bot:expell\n" + \
                  "「✭」 " + key + "Staff:on\n" + \
                  "「✭」 " + key + "Staff:expell\n" + \
                  "「✭」 " + key + "Admin:on\n" + \
                  "「✭」 " + key + "Admin:expell\n" + \
                  "「✭」 " + key + "Botadd「@」\n" + \
                  "「✭」 " + key + "Botdell「@」\n" + \
                  "「✭」 " + key + "Staffadd「@」\n" + \
                  "「✭」 " + key + "Staffdell「@」\n" + \
                  "「✭」 " + key + "Adminadd「@」\n" + \
                  "「✭」 " + key + "Admindell「@」\n" + \
                  "「✭」 " + key + "Refresh\n" + \
                  "「✭」 " + key + "Listbot\n" + \
                  "「✭」 " + key + "Listadmin\n" + \
                  "「✭」 " + key + "Listprotect\n" + \
                  "\nKetik「 Refresh 」jika sudah\nmenggunakan command diatas...\n"
    return helpMessage

def helpbot():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage1 = "• Gunakan「 " + key + " 」di depannya\n\n" + \
                  "「✭」 " + key + "Blc\n" + \
                  "「✭」 " + key + "Ban:on\n" + \
                  "「✭」 " + key + "Unban:on\n" + \
                  "「✭」 " + key + "Ban「@」\n" + \
                  "「✭」 " + key + "Unban「@」\n" + \
                  "「✭」 " + key + "Talkban「@」\n" + \
                  "「✭」 " + key + "Untalkban「@」\n" + \
                  "「✭」 " + key + "Talkban:on\n" + \
                  "「✭」 " + key + "Untalkban:on\n" + \
                  "「✭」 " + key + "Banlist\n" + \
                  "「✭」 " + key + "Talkbanlist\n" + \
                  "「✭」 " + key + "Clearban\n" + \
                  "「✭」 " + key + "Refresh\n" + \
                  "\n「 Check Settings 」\n• Use「 " + key + " 」di depannya\n\n" + \
                  "「✭」 " + key + "Cek sider\n" + \
                  "「✭」 " + key + "Cek spam\n" + \
                  "「✭」 " + key + "Cek pesan \n" + \
                  "「✭」 " + key + "Cek respon \n" + \
                  "「✭」 " + key + "Cek leave\n" + \
                  "「✭」 " + key + "Cek welcome\n" + \
                  "「✭」 " + key + "Set sider:「Text」\n" + \
                  "「✭」 " + key + "Set spam:「Text」\n" + \
                  "「✭」 " + key + "Set pesan:「Text」\n" + \
                  "「✭」 " + key + "Set respon:「Text」\n" + \
                  "「✭」 " + key + "Set leave:「Text」\n" + \
                  "「✭」 " + key + "Set welcome:「Text」\n" + \
                  "「✭」 " + key + "Myname:「Nama」\n" + \
                  "「✭」 " + key + "Bot1name:「Nama」\n" + \
                  "「✭」 " + key + "Bot2name:「Nama」\n" + \
                  "「✭」 " + key + "Bot3name:「Nama」\n" + \
                  "「✭」 " + key + "Bot4name:「Nama」\n" + \
                  "「✭」 " + key + "Bot5name:「Nama」\n" + \
                  "「✭」 " + key + "Bot1up「Kirim fotonya」\n" + \
                  "「✭」 " + key + "Bot2up「Kirim fotonya」\n" + \
                  "「✭」 " + key + "Bot3up「Kirim fotonya」\n" + \
                  "「✭」 " + key + "Bot4up「Kirim fotonya」\n" + \
                  "「✭」 " + key + "Bot5up「Kirim fotonya」\n" + \
                  "「✭」 " + key + "Gift:「Mid korban」「Jumlah」\n" + \
                  "「✭」 " + key + "Spam:「Mid korban」「Jumlah」\n" + \
                  "\nKetik「 Refresh 」jika sudah\nmenggunakan command diatas...\n"
    return helpMessage1
