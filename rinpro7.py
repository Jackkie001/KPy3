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

ririn = LINE("")
 #ririn = LINE("EtxpGC2IuAsld3O2Pidc.DlFU7XKB9Mi78Md+uAcqla.V12MNkA8+eafCmDCLWBClwyslqcA+KyOurCIMJ4mq50=")
dna1 = LINE("")
#dna1 = LINE("EtuLPEhpjjS71GuDU5f2.We7lj7PxgwBQ8O07ppSHuG.5DcABOIp9Jc0EdDh/u+PHBm+i07cdqjq9BGL9zOq5lk=")
#dna2 = LINE("")
#dna2 = LINE("Et6xGnlf14mOmnop4Pe1.Sl2u8yHwWYZHMslzI9Bi8q.h1HaVFpTVHL5usm69BvjLDD42QmKfiAEzEojY3femwY=") 
#dna3 = LINE("")
#dna3 = LINE("Et94vqCMv5NRretSOvl8.M53qiD/PJ1i6qsVfYwB7Ea.V2SGF9DxOIa6S6p7wXzC8N/OxUUrQQAb3Vz6pn9btPo=")
# dna4 = LINE("")
#dna4 = LINE("EtilRNFl9ztMAOHqJqv3.LTjIccO9HW0I2OLJ9e3wmW.gN258n1LMJk+w5JMCbmncCwXPPN18+TdmTcML9wTr34=")
#d na5 = LINE("")
# dna5 = LINE("EtaVFASOkHpxVH9xxb6a.i4cphH9h9VMs4DyAsZSSsG.9hTOd/zdCXUd/bdOfEPdnA9evlW23h+16QH2nGk9hbo=")
 #dna6 = LINE("")
#dna6 = LINE('EtzFBkX896gVvVTdWZqa.fW/HXK/P6ucyNSYHd42E2G.ejnDnbje+psyh7aE0ySMbtM/IRiVOxOv0YGN7XhymQk=')
#dn a7 = LINE("")
#dna7 = LINE("Etl0D13AR8TJaLWQ6TG3.GQe1F0FLgkB3suGK5WtUCW.6GPQBFNkQO1AbnSPAODwgO+vl14KuciJwrYY99QEjxY=")
 #dna8 = LINE("")
#dna8 = LINE("EtjCVvYSEcNxBcK1lUw3.fOtS1/ZYrVfyY2wr74a3uW.9YblQZHqVNFRXKhDbTd3vwkSev4CTfvRXX4tXjn+1V8=")
#dna9 = LINE("")
#dna9 = LINE("EtwPyGoOdgsrXEv4TJW1./PGYhVVe4uDle5Q6kp48qq.L5ssZx8fqnri74Cv4jggZ1zXdSG80IPUd5zlvv3Pg64=")
#dna10 = LINE("")
#dna10 = LINE("EtNKP9QYIovaSlKqHRzd.UC8K+GXOvK/3A1WWSKmQRq.AQAN+llfHPEjbyE5aChkpp4cElfAmrscBZ8M0tvk/sI=") #Ghost

ririnPoll = OEPoll(ririn)
KAC=[ririn,dna1]
#KAC=[ririn,dna1,dna2,dna3,dna4,dna5,dna6,dna7,dna8,dna9]
ririnMid = ririn.profile.mid
aMid = dna1.profile.mid
#bMid = dna2.profile.mid
#cMid = dna3.profile.mid
#dMid = dna4.profile.mid
#eMid = dna5.profile.mid
#fMid = dna6.profile.mid
#gMid = dna7.profile.mid
#hMid = dna8.profile.mid
#iMid = dna9.profile.mid
#jMid = dna10.profile.mid

Bots=[ririnMid,aMid]
#Bots=[ririnMid,aMid,bMid,cMid,dMid,eMid,fMid,gMid,hMid,iMid,jMid]
creator = ["u2ff21221ec149ca856b792c6dee280ff"]
Owner = ["u2ff21221ec149ca856b792c6dee280ff"]
admin = ["u2ff21221ec149ca856b792c6dee280ff","u0d9c78aab41cac3ec2d056a96979b187"]

responsename = ririn.getProfile().displayName
responsename2 = dna1.getProfile().displayName
#responsename3 = dna2.getProfile().displayName
#responsename4 = dna3.getProfile().displayName
#responsename5 = dna4.getProfile().displayName
#responsename6 = dna5.getProfile().displayName
#responsename7 = dna6.getProfile().displayName
#responsename8 = dna7.getProfile().displayName
#responsename9 = dna8.getProfile().displayName
#responsename10 = dna9.getProfile().displayName
#responsename11 = dna10.getProfile().displayName

ririnProfile = ririn.getProfile()
aProfile = dna1.getProfile()
#bProfile = dna2.getProfile()
#cProfile = dna3.getProfile()
#dProfile = dna4.getProfile()
#eProfile = dna5.getProfile()
#fProfile = dna6.getProfile()
#gProfile = dna7.getProfile()
#hProfile = dna8.getProfile()
#iProfile = dna9.getProfile()
#jProfile = dna10.getProfile()

ririnSettings = ririn.getSettings()
aSettings = dna1.getSettings()
#bSettings = dna2.getSettings()
#cSettings = dna3.getSettings()
#dSettings = dna4.getSettings()
#eSettings = dna5.getSettings()
#fSettings = dna6.getSettings()
#gSettings = dna7.getSettings()
#hSettings = dna8.getSettings()
#iSettings = dna9.getSettings()
#jSettings = dna10.getSettings()

botStart = time.time()

print ("╔═════════════════════════\n║╔════════════════════════\n║╠❂➣ DNA BERHASIL LOGIN\n║╚════════════════════════\n╚═════════════════════════")

msg_dict = {}

wait = {
    "autoAdd": True,
    "autoCancel": {"on":True,"members":3},
    "autoJoin": True,
    "autoLeave": False,
    "autoRead": False,
    "autoRespon": True,
    "autoResponPc": False,
    "autoJoinTicket": True,
    "blacklist": {},
    "checkContact": False,
    "checkPost": False,
    "checkSticker": False,
    "changePictureProfile": False,
    "changeGroupPicture": [],
    "CloseQR":True,
    "commentBlack": {},
    "dblack":False,
    "dblacklist":False,
    "invite": {},
    "keyCommand": "",
    "lang":"JP",
    "leaveRoom": True,
    "likeOn": True,
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
    "removechat": False,
    "setKey": False,
    "sider": False,
    "timeline":True,
    "unsendMessage": True,
    "wblack": False,
    "wblacklist":False,
    "whitelist": {}
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
    
wait["myProfile"]["displayName"] = ririnProfile.displayName
wait["myProfile"]["statusMessage"] = ririnProfile.statusMessage
wait["myProfile"]["pictureStatus"] = ririnProfile.pictureStatus
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
    ririn.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

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
    
def helpmessage():
    if wait['setKey'] == True:
        key = wait['keyCommand']
    else:
        key = ''
    helpMessage =   "╔════════════════════╗" + "\n" + \
                    "                    ✰ ᴅɴᴀ ʙᴏᴛ ✰" + "\n" + \
                    "╚════════════════════╝" + "\n" + \
	                "╔════════════════════╗" + "\n" + \
	                "               ✪ 🅿🆄🅱🅻🅸🅲 ✪" + "\n" + \
	                "╠════════════════════╝" + "\n" + \
	                "╠═☢════〚 ʜᴇʟᴘ 〛☢" + "\n" + \
	                "╠❂➣ " + key + "ʜᴇʟᴘ " + "\n" + \
	                "╠❂➣ " + key + "ᴛᴛs " + "\n" + \
	                "╠❂➣ " + key + "ᴛʀᴀɴsʟᴀᴛᴇ " + "\n" + \
	                "╠═☢════〚 ʙᴏᴛ 〛☢" + "\n" + \
	                "╠❂➣ " + key + "ᴀʙᴏᴜᴛ" + "\n" + \
	                "╠❂➣ " + key + "ᴀᴅᴍɪɴʟɪsᴛ" + "\n" + \
	                "╠❂➣ " + key + "ᴏᴡɴᴇʀʟɪsᴛ" + "\n" + \
	                "╠═☢════〚 sᴇʟғ 〛☢" + "\n" + \
	                "╠❂➣ " + key + "ᴍᴇ" + "\n" + \
	                "╠❂➣ " + key + "ᴍᴇɴᴛɪᴏɴ" + "\n" + \
	                "╠❂➣ " + key + "ᴍʏᴍɪᴅ" + "\n" + \
	                "╠❂➣ " + key + "ᴍʏɴᴀᴍᴇ" + "\n" + \
	                "╠❂➣ " + key + "ᴍʏʙɪᴏ" + "\n" + \
	                "╠❂➣ " + key + "ᴍʏᴘɪᴄᴛᴜʀᴇ" + "\n" + \
	                "╠❂➣ " + key + "ᴍʏᴠɪᴅᴇᴏᴘʀᴏғɪʟᴇ" + "\n" + \
	                "╠❂➣ " + key + "ᴍʏᴄᴏᴠᴇʀ" + "\n" + \
	                "╠═☢════〚 ɢʀᴏᴜᴘ 〛☢" + "\n" + \
	                "╠❂➣ " + key + "ɢʀᴏᴜᴘᴄʀᴇᴀᴛᴏʀ" + "\n" + \
	                "╠❂➣ " + key + "ɢʀᴏᴜᴘɪᴅ" + "\n" + \
	                "╠❂➣ " + key + "ɢʀᴏᴜᴘɴᴀᴍᴇ" + "\n" + \
	                "╠❂➣ " + key + "ɢʀᴏᴜᴘᴘɪᴄᴛᴜʀᴇ" + "\n" + \
	                "╠❂➣ " + key + "ɢʀᴏᴜᴘᴛɪᴄᴋᴇᴛ" + "\n" + \
	                "╠❂➣ " + key + "ɢʀᴏᴜᴘᴍᴇᴍʙᴇʀʟɪsᴛ" + "\n" + \
	                "╠❂➣ " + key + "ɢʀᴏᴜᴘɪɴғᴏ" + "\n" + \
	                "╠═☢════〚 sᴘᴇᴄɪᴀʟ 〛☢" + "\n" + \
	                "╠❂➣ " + key + "ʟᴜʀᴋɪɴɢ" + "\n" + \
	                "╠❂➣ " + key + "ʟᴜʀᴋɪɴɢ「ᴏɴ/ᴏғғ/ʀᴇsᴇᴛ」" + "\n" + \
	                "╠═☢════〚 ᴍᴇᴅɪᴀ 〛☢" + "\n" + \
	                "╠❂➣ " + key + "ᴄʜᴇᴄᴋʟᴏᴄᴀᴛɪᴏɴ「ʟᴏᴄᴀᴛɪᴏɴ」" + "\n" + \
	                "╠❂➣ " + key + "ᴄʜᴇᴄᴋᴘʀᴀʏᴛɪᴍᴇ「ʟᴏᴄᴀᴛɪᴏɴ」" + "\n" + \
	                "╠❂➣ " + key + "ᴄʜᴇᴄᴋᴡᴇᴀᴛʜᴇʀ「ʟᴏᴄᴀᴛɪᴏɴ」" + "\n" + \
	                "╠❂➣ " + key + "ᴄʜᴇᴄᴋᴡᴇʙsɪᴛᴇ「ᴜʀʟ」" + "\n" + \
	                "╠❂➣ " + key + "ɪɴsᴛᴀɪɴғᴏ 「ᴜsᴇʀɴᴀᴍᴇ」" + "\n" + \
	                "╠❂➣ " + key + "sᴇᴀʀᴄʜɪᴍᴀɢᴇ 「sᴇᴀʀᴄʜ」" + "\n" + \
	                "╠❂➣ " + key + "sᴇᴀʀᴄʜʟʏʀɪᴄ 「sᴇᴀʀᴄʜ」" + "\n" + \
	                "╠❂➣ " + key + "sᴇᴀʀᴄʜᴍᴜsɪᴄ 「sᴇᴀʀᴄʜ」" + "\n" + \
	                "╠❂➣ " + key + "sᴇᴀʀᴄʜʏᴏᴜᴛᴜʙᴇ「sᴇᴀʀᴄʜ」" + "\n" + \
	                "╔════════════════════╗" + "\n" + \
	                "                 ✪ 🅰🅳🅼🅸🅽 ✪" + "\n" + \
	                "╠════════════════════╝" + "\n" + \
	                "╠═☢════〚 ᴘʀᴏᴛᴇᴄᴛ 〛☢" + "\n" + \
	                "╠❂➣ " + key + "ᴘʀᴏᴄᴀɴᴄᴇʟ「ᴏɴ/ᴏғғ」" + "\n" + \
	                "╠❂➣ " + key + "ᴘʀᴏɢʀ「ᴏɴ/ᴏғғ」" + "\n" + \
	                "╠❂➣ " + key + "ᴘʀᴏɪɴᴠɪᴛᴇ「ᴏɴ/ᴏғғ」" + "\n" + \
	                "╠❂➣ " + key + "ᴘʀᴏᴊᴏɪɴ「ᴏɴ/ᴏғғ」" + "\n" + \
	                "╠═☢════〚 ʙᴏᴛ 〛☢" + "\n" + \
	                "╠❂➣ " + key + "sᴘ" + "\n" + \
	                "╠❂➣ " + key + "sᴘᴇᴇᴅ" + "\n" + \
	                "╠❂➣ " + key + "sᴇᴛ" + "\n" + \
	                "╠❂➣ " + key + "sᴛᴀᴛᴜs" + "\n" + \
	                "╠❂➣ " + key + "ᴀʙꜱᴇɴ" + "\n" + \
	                "╠❂➣ " + key + "ᴅɴᴀ" + "\n" + \
	                "╠❂➣ " + key + "ʀᴇꜱᴘᴏɴ" + "\n" + \
	                "╠═☢════〚 sᴛᴀᴛᴜs 〛☢" + "\n" + \
	                "╠❂➣ " + key + "ᴄʜᴇᴄᴋᴄᴏɴᴛᴀᴄᴛ「ᴏɴ/ᴏғғ」" + "\n" + \
	                "╠❂➣ " + key + "ᴄʜᴇᴄᴋᴘᴏsᴛ「ᴏɴ/ᴏғғ」" + "\n" + \
	                "╠❂➣ " + key + "ᴄʜᴇᴄᴋsᴛɪᴄᴋᴇʀ「ᴏɴ/ᴏғғ」" + "\n" + \
	                "╠═☢════〚 ɢʀᴏᴜᴘ 〛☢" + "\n" + \
	                "╠❂➣ " + key + "ʙᴀɴ" + "\n" + \
	                "╠❂➣ " + key + "ᴜɴʙᴀɴ" + "\n" + \
	                "╠❂➣ " + key + "ʙᴀɴ「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
	                "╠❂➣ " + key + "ᴜɴʙᴀɴ「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
	                "╠❂➣ " + key + "ʙʟᴀᴄᴋʟɪsᴛ 「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
	                "╠❂➣ " + key + "ʙᴀɴʟɪsᴛ" + "\n" + \
	                "╠❂➣ " + key + "ᴄᴇᴋʙᴀɴ" + "\n" + \
	                "╠❂➣ " + key + "ᴄʟᴇᴀʀ ʙᴀɴ" + "\n" + \
	                "╠❂➣ " + key + "ᴋɪʟʟ ʙᴀɴ" + "\n" + \
	                "╠❂➣ " + key + "ɴᴋ 「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
	                "╠❂➣ " + key + "sᴛᴇᴀʟ 「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
	                "╠❂➣ " + key + "ᴄʜᴀɴɢᴇɢʀᴏᴜᴘᴘɪᴄᴛᴜʀᴇ" + "\n" + \
	                "╠❂➣ " + key + "ɢʀᴏᴜᴘᴛɪᴄᴋᴇᴛ「ᴏɴ/ᴏғғ」" + "\n" + \
	                "╠❂➣ " + key + "ɪɴᴠɪᴛᴇ" + "\n" + \
	                "╠❂➣ " + key + "ɪɴᴠɪᴛᴇᴍɪᴅ「ᴍɪᴅ」''()''" + "\n" + \
	                "╠❂➣ " + key + "ɪɴᴠɪᴛᴇɢᴄ「ᴀᴍᴏᴜɴᴛ」" + "\n" + \
	                "╠═☢════〚 sᴘᴇᴄɪᴀʟ 〛☢" + "\n" + \
	                "╠❂➣ " + key + "ᴍɪᴍɪᴄ「ᴏɴ/ᴏғғ」" + "\n" + \
	                "╠❂➣ " + key + "ᴍɪᴍɪᴄᴀᴅᴅ「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
	                "╠❂➣ " + key + "ᴍɪᴍɪᴄᴅᴇʟ「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
	                "╠❂➣ " + key + "ᴍɪᴍɪᴄʟɪsᴛ" + "\n" + \
	                "╠❂➣ " + key + "sɪᴅᴇʀ「ᴏɴ/ᴏғғ」" + "\n" + \
	                "╠❂➣ " + key + "sᴛᴇᴀʟᴄᴏɴᴛᴀᴄᴛ「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
	                "╠❂➣ " + key + "sᴛᴇᴀʟᴍɪᴅ「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
	                "╠❂➣ " + key + "sᴛᴇᴀʟɴᴀᴍᴇ「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
	                "╠❂➣ " + key + "sᴛᴇᴀʟʙɪᴏ「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
	                "╠❂➣ " + key + "sᴛᴇᴀʟᴘɪᴄᴛᴜʀᴇ「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
	                "╠❂➣ " + key + "sᴛᴇᴀʟᴠɪᴅᴇᴏᴘʀᴏғɪʟᴇ「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
	                "╠❂➣ " + key + "sᴛᴇᴀʟᴄᴏᴠᴇʀ「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
	                "╠❂➣ ᴍʏᴋᴇʏ" + "\n" + \
	                "╠❂➣ sᴇᴛᴋᴇʏ「ᴏɴ/ᴏғғ」" + "\n" + \
	                "╔════════════════════╗" + "\n" + \
	                "                 ✪ 🅾🆆🅽🅴🆁 ✪" + "\n" + \
	                "╠════════════════════╝" + "\n" + \
	                "╠═☢════〚 ᴘʀᴏᴛᴇᴄᴛ 〛☢" + "\n" + \
	                "╠❂➣ " + key + "sᴇᴛᴘʀᴏ「ᴏɴ/ᴏғғ」" + "\n" + \
	                "╠═☢════〚 ʙᴏᴛ 〛☢" + "\n" + \
	                "╠❂➣ " + key + "ᴀᴅᴍɪɴᴀᴅᴅ「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
	                "╠❂➣ " + key + "ᴀᴅᴍɪɴᴅᴇʟ「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
	                "╠❂➣ " + key + "ʙᴀᴄᴋᴜᴘᴘʀᴏғɪʟᴇ" + "\n" + \
	                "╠❂➣ " + key + "ʙʏᴇ ᴀʟʟ" + "\n" + \
	                "╠❂➣ " + key + "ʙʏᴇ ᴅɴᴀ" + "\n" + \
	                "╠❂➣ " + key + "ᴄᴏᴍᴇ ᴅɴᴀ" +  "\n" + \
	                "╠❂➣ " + key + "ᴄʀᴀsʜ" +  "\n" + \
	                "╠❂➣ " + key + "ᴄʜᴀɴɢᴇʙɪᴏ:「ǫᴜᴇʀʏ」" + "\n" + \
	                "╠❂➣ " + key + "ᴄʜᴀɴɢᴇɴᴀᴍᴇ:「ǫᴜᴇʀʏ」" + "\n" + \
	                "╠❂➣ " + key + "ᴄʟᴏɴᴇᴘʀᴏғɪʟᴇ「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
	                "╠❂➣ " + key + "ᴄʜᴀɴɢᴇᴘɪᴄᴛᴜʀᴇᴘʀᴏғɪʟᴇ" + "\n" + \
	                "╠❂➣ " + key + "ᴇɴᴅᴄʜᴀᴛ" +  "\n" + \
	                "╠❂➣ " + key + "ɢʀᴏᴜᴘʟɪsᴛ" + "\n" + \
	                "╠❂➣ " + key + "ʀᴇsᴛᴀʀᴛ" + "\n" + \
	                "╠❂➣ " + key + "ʀᴇsᴛᴏʀᴇᴘʀᴏғɪʟᴇ" + "\n" + \
	                "╠❂➣ " + key + "ʀᴜɴᴛɪᴍᴇ" + "\n" + \
	                "╠═☢════〚 sᴛᴀᴛᴜs 〛☢" + "\n" + \
	                "╠❂➣ " + key + "ᴀᴜᴛᴏᴀᴅᴅ「ᴏɴ/ᴏғғ」" + "\n" + \
	                "╠❂➣ " + key + "ᴀᴜᴛᴏᴊᴏɪɴ「ᴏɴ/ᴏғғ」" + "\n" + \
	                "╠❂➣ " + key + "ᴀᴜᴛᴏᴊᴏɪɴᴛɪᴄᴋᴇᴛ「ᴏɴ/ᴏғғ」" + "\n" + \
	                "╠❂➣ " + key + "ᴀᴜᴛᴏʟᴇᴀᴠᴇ「ᴏɴ/ᴏғғ」" + "\n" + \
	                "╠❂➣ " + key + "ᴀᴜᴛᴏʀᴇᴀᴅ「ᴏɴ/ᴏғғ」" + "\n" + \
	                "╠❂➣ " + key + "ᴀᴜᴛᴏʀᴇsᴘᴏɴ「ᴏɴ/ᴏғғ」" + "\n" + \
	                "╠❂➣ " + key + "ᴀᴜᴛᴏʀᴇsᴘᴏɴᴘᴄ「ᴏɴ/ᴏғғ」" + "\n" + \
	                "╠❂➣ " + key + "ᴜɴsᴇɴᴅᴄʜᴀᴛ「ᴏɴ/ᴏғғ」" + "\n" + \
	                "╠═☢════〚 sᴇʀᴠᴇʀ ɪɴғᴏ 〛☢" + "\n" + \
	                "╠❂➣ " + key + "ᴄᴘᴜ" + "\n" + \
	                "╠❂➣ " + key + "ɪғᴄᴏɴғɪɢ" + "\n" + \
	                "╠❂➣ " + key + "ᴋᴇʀɴᴇʟ" + "\n" + \
	                "╠❂➣ " + key + "sʏsᴛᴇᴍ" + "\n" + \
	                "╠════════════════════╗" + "\n" + \
	                "                ᴄʀᴇᴅɪᴛs ʙʏ : ᴅ̶ᴇ̶ᴇ̶ ✯" + "\n" + \
	                "╚════════════════════╝" + "\n" + \
	                "╔════════════════════╗" + "\n" + \
	                "                   ✰ ᴅɴᴀ ʙᴏᴛ  ✰" + "\n" + \
                    "╚════════════════════╝"
    return helpMessage

def helptexttospeech():
    if wait['setKey'] == True:
        key = wait['keyCommand']
    else:
        key = ''
    helpTextToSpeech =  "╔════════════════════╗" + "\n" + \
                        "                    ✰ ᴅɴᴀ ʙᴏᴛ ✰" + "\n" + \
                        "╚════════════════════╝" + "\n" + \
                        "╔════════════════════╗" + "\n" + \
                        "          ◄]·✪·ᴛᴇxᴛᴛᴏsᴘᴇᴇᴄʜ·✪·[►" + "\n" + \
                        "╠════════════════════╝ " + "\n" + \
                        "╠❂➣ " + key + "ᴀғ : ᴀғʀɪᴋᴀᴀɴs" + "\n" + \
                        "╠❂➣ " + key + "sǫ : ᴀʟʙᴀɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴀʀ : ᴀʀᴀʙɪᴄ" + "\n" + \
                        "╠❂➣ " + key + "ʜʏ : ᴀʀᴍᴇɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ʙɴ : ʙᴇɴɢᴀʟɪ" + "\n" + \
                        "╠❂➣ " + key + "ᴄᴀ : ᴄᴀᴛᴀʟᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴢʜ : ᴄʜɪɴᴇsᴇ" + "\n" + \
                        "╠❂➣ " + key + "ᴢʜʏᴜᴇ : ᴄʜɪɴᴇsᴇ (ᴄᴀɴᴛᴏɴᴇsᴇ)" + "\n" + \
                        "╠❂➣ " + key + "ʜʀ : ᴄʀᴏᴀᴛɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴄs : ᴄᴢᴇᴄʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴅᴀ : ᴅᴀɴɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ɴʟ : ᴅᴜᴛᴄʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴇɴ : ᴇɴɢʟɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴇɴᴀᴜ : ᴇɴɢʟɪsʜ (ᴀᴜsᴛʀᴀʟɪᴀ)" + "\n" + \
                        "╠❂➣ " + key + "ᴇɴᴜᴋ : ᴇɴɢʟɪsʜ (ᴜᴋ)" + "\n" + \
                        "╠❂➣ " + key + "ᴇɴᴜs : ᴇɴɢʟɪsʜ (ᴜs)" + "\n" + \
                        "╠❂➣ " + key + "ᴇᴏ : ᴇsᴘᴇʀᴀɴᴛᴏ" + "\n" + \
                        "╠❂➣ " + key + "ғɪ : ғɪɴɴɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ғʀ : ғʀᴇɴᴄʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴅᴇ : ɢᴇʀᴍᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴇʟ : ɢʀᴇᴇᴋ" + "\n" + \
                        "╠❂➣ " + key + "ʜɪ : ʜɪɴᴅɪ" + "\n" + \
                        "╠❂➣ " + key + "ʜᴜ : ʜᴜɴɢᴀʀɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ɪs : ɪᴄᴇʟᴀɴᴅɪᴄ" + "\n" + \
                        "╠❂➣ " + key + "ɪᴅ : ɪɴᴅᴏɴᴇsɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ɪᴛ : ɪᴛᴀʟɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴊᴀ : ᴊᴀᴘᴀɴᴇsᴇ" + "\n" + \
                        "╠❂➣ " + key + "ᴋᴍ : ᴋʜᴍᴇʀ (ᴄᴀᴍʙᴏᴅɪᴀɴ)" + "\n" + \
                        "╠❂➣ " + key + "ᴋᴏ : ᴋᴏʀᴇᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ʟᴀ : ʟᴀᴛɪɴ" + "\n" + \
                        "╠❂➣ " + key + "ʟᴠ : ʟᴀᴛᴠɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴍᴋ : ᴍᴀᴄᴇᴅᴏɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ɴᴏ : ɴᴏʀᴡᴇɢɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴘʟ : ᴘᴏʟɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴘᴛ : ᴘᴏʀᴛᴜɢᴜᴇsᴇ" + "\n" + \
                        "╠❂➣ " + key + "ʀᴏ : ʀᴏᴍᴀɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ʀᴜ : ʀᴜssɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "sʀ : sᴇʀʙɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "sɪ : sɪɴʜᴀʟᴀ" + "\n" + \
                        "╠❂➣ " + key + "sᴋ : sʟᴏᴠᴀᴋ" + "\n" + \
                        "╠❂➣ " + key + "ᴇs : sᴘᴀɴɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴇsᴇs : sᴘᴀɴɪsʜ (sᴘᴀɪɴ)" + "\n" + \
                        "╠❂➣ " + key + "ᴇsᴜs : sᴘᴀɴɪsʜ (ᴜs)" + "\n" + \
                        "╠❂➣ " + key + "sᴡ : sᴡᴀʜɪʟɪ" + "\n" + \
                        "╠❂➣ " + key + "sᴠ : sᴡᴇᴅɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴛᴀ : ᴛᴀᴍɪʟ" + "\n" + \
                        "╠❂➣ " + key + "ᴛʜ : ᴛʜᴀɪ" + "\n" + \
                        "╠❂➣ " + key + "ᴛʀ : ᴛᴜʀᴋɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴜᴋ : ᴜᴋʀᴀɪɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴠɪ : ᴠɪᴇᴛɴᴀᴍᴇsᴇ" + "\n" + \
                        "╠❂➣ " + key + "ᴄʏ : ᴡᴇʟsʜ" + "\n" + \
                        "╠════════════════════╗" + "\n" + \
                        "               ᴄʀᴇᴅɪᴛs ʙʏ : ©ᴅ̶ᴇ̶ᴇ̶ ✯" + "\n" + \
                        "╚════════════════════╝" + "\n" + \
                        "╔════════════════════╗" + "\n" + \
                        "                    ✰ ᴅɴᴀ ʙᴏᴛ ✰" + "\n" + \
                        "╚════════════════════╝" + "\n" + \
                        "ᴄᴏɴᴛᴏʜ : " + key + "sᴀʏ-ɪᴅ ʀɪʀɪɴ"
    return helpTextToSpeech

def helptranslate():
    if wait['setKey'] == True:
        key = wait['keyCommand']
    else:
        key = ''
    helpTranslate = "╔════════════════════╗" + "\n" + \
                        "                     ✰ ᴅɴᴀ ʙᴏᴛ ✰" + "\n" + \
                        "╚════════════════════╝" + "\n" + \
                        "╔════════════════════╗" + "\n" + \
                        "             ◄]·✪·ᴛʀᴀɴsʟᴀᴛᴇ·✪·[►" + "\n" + \
                        "╠════════════════════╝" + "\n" + \
                        "╠❂➣ " + key + "ᴀғ : ᴀғʀɪᴋᴀᴀɴs" + "\n" + \
                        "╠❂➣ " + key + "sǫ : ᴀʟʙᴀɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴀᴍ : ᴀᴍʜᴀʀɪᴄ" + "\n" + \
                        "╠❂➣ " + key + "ᴀʀ : ᴀʀᴀʙɪᴄ" + "\n" + \
                        "╠❂➣ " + key + "ʜʏ : ᴀʀᴍᴇɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴀᴢ : ᴀᴢᴇʀʙᴀɪᴊᴀɴɪ" + "\n" + \
                        "╠❂➣ " + key + "ᴇᴜ : ʙᴀsǫᴜᴇ" + "\n" + \
                        "╠❂➣ " + key + "ʙᴇ : ʙᴇʟᴀʀᴜsɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ʙɴ : ʙᴇɴɢᴀʟɪ" + "\n" + \
                        "╠❂➣ " + key + "ʙs : ʙᴏsɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ʙɢ : ʙᴜʟɢᴀʀɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴄᴀ : ᴄᴀᴛᴀʟᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴄᴇʙ : ᴄᴇʙᴜᴀɴᴏ" + "\n" + \
                        "╠❂➣ " + key + "ɴʏ : ᴄʜɪᴄʜᴇᴡᴀ" + "\n" + \
                        "╠❂➣ " + key + "ᴢʜᴄɴ : ᴄʜɪɴᴇsᴇ (sɪᴍᴘʟɪғɪᴇᴅ)" + "\n" + \
                        "╠❂➣ " + key + "ᴢʜᴛᴡ : ᴄʜɪɴᴇsᴇ (ᴛʀᴀᴅɪᴛɪᴏɴᴀʟ)" + "\n" + \
                        "╠❂➣ " + key + "ᴄᴏ : ᴄᴏʀsɪᴄᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ʜʀ : ᴄʀᴏᴀᴛɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴄs : ᴄᴢᴇᴄʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴅᴀ : ᴅᴀɴɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ɴʟ : ᴅᴜᴛᴄʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴇɴ : ᴇɴɢʟɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴇᴏ : ᴇsᴘᴇʀᴀɴᴛᴏ" + "\n" + \
                        "╠❂➣ " + key + "ᴇᴛ : ᴇsᴛᴏɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴛʟ : ғɪʟɪᴘɪɴᴏ" + "\n" + \
                        "╠❂➣ " + key + "ғɪ : ғɪɴɴɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ғʀ : ғʀᴇɴᴄʜ" + "\n" + \
                        "╠❂➣ " + key + "ғʏ : ғʀɪsɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ɢʟ : ɢᴀʟɪᴄɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴋᴀ : ɢᴇᴏʀɢɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴅᴇ : ɢᴇʀᴍᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴇʟ : ɢʀᴇᴇᴋ" + "\n" + \
                        "╠❂➣ " + key + "ɢᴜ : ɢᴜᴊᴀʀᴀᴛɪ" + "\n" + \
                        "╠❂➣ " + key + "ʜᴛ : ʜᴀɪᴛɪᴀɴ ᴄʀᴇᴏʟᴇ" + "\n" + \
                        "╠❂➣ " + key + "ʜᴀ : ʜᴀᴜsᴀ" + "\n" + \
                        "╠❂➣ " + key + "ʜᴀᴡ : ʜᴀᴡᴀɪɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ɪᴡ : ʜᴇʙʀᴇᴡ" + "\n" + \
                        "╠❂➣ " + key + "ʜɪ : ʜɪɴᴅɪ" + "\n" + \
                        "╠❂➣ " + key + "ʜᴍɴ : ʜᴍᴏɴɢ" + "\n" + \
                        "╠❂➣ " + key + "ʜᴜ : ʜᴜɴɢᴀʀɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ɪs : ɪᴄᴇʟᴀɴᴅɪᴄ" + "\n" + \
                        "╠❂➣ " + key + "ɪɢ : ɪɢʙᴏ" + "\n" + \
                        "╠❂➣ " + key + "ɪᴅ : ɪɴᴅᴏɴᴇsɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ɢᴀ : ɪʀɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ɪᴛ : ɪᴛᴀʟɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴊᴀ : ᴊᴀᴘᴀɴᴇsᴇ" + "\n" + \
                        "╠❂➣ " + key + "ᴊᴡ : ᴊᴀᴠᴀɴᴇsᴇ" + "\n" + \
                        "╠❂➣ " + key + "ᴋɴ : ᴋᴀɴɴᴀᴅᴀ" + "\n" + \
                        "╠❂➣ " + key + "ᴋᴋ : ᴋᴀᴢᴀᴋʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴋᴍ : ᴋʜᴍᴇʀ" + "\n" + \
                        "╠❂➣ " + key + "ᴋᴏ : ᴋᴏʀᴇᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴋᴜ : ᴋᴜʀᴅɪsʜ (ᴋᴜʀᴍᴀɴᴊɪ)" + "\n" + \
                        "╠❂➣ " + key + "ᴋʏ : ᴋʏʀɢʏᴢ" + "\n" + \
                        "╠❂➣ " + key + "ʟᴏ : ʟᴀᴏ" + "\n" + \
                        "╠❂➣ " + key + "ʟᴀ : ʟᴀᴛɪɴ" + "\n" + \
                        "╠❂➣ " + key + "ʟᴠ : ʟᴀᴛᴠɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ʟᴛ : ʟɪᴛʜᴜᴀɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ʟʙ : ʟᴜxᴇᴍʙᴏᴜʀɢɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴍᴋ : ᴍᴀᴄᴇᴅᴏɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴍɢ : ᴍᴀʟᴀɢᴀsʏ" + "\n" + \
                        "╠❂➣ " + key + "ᴍs : ᴍᴀʟᴀʏ" + "\n" + \
                        "╠❂➣ " + key + "ᴍʟ : ᴍᴀʟᴀʏᴀʟᴀᴍ" + "\n" + \
                        "╠❂➣ " + key + "ᴍᴛ : ᴍᴀʟᴛᴇsᴇ" + "\n" + \
                        "╠❂➣ " + key + "ᴍɪ : ᴍᴀᴏʀɪ" + "\n" + \
                        "╠❂➣ " + key + "ᴍʀ : ᴍᴀʀᴀᴛʜɪ" + "\n" + \
                        "╠❂➣ " + key + "ᴍɴ : ᴍᴏɴɢᴏʟɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴍʏ : ᴍʏᴀɴᴍᴀʀ (ʙᴜʀᴍᴇsᴇ)" + "\n" + \
                        "╠❂➣ " + key + "ɴᴇ : ɴᴇᴘᴀʟɪ" + "\n" + \
                        "╠❂➣ " + key + "ɴᴏ : ɴᴏʀᴡᴇɢɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴘs : ᴘᴀsʜᴛᴏ" + "\n" + \
                        "╠❂➣ " + key + "ғᴀ : ᴘᴇʀsɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴘʟ : ᴘᴏʟɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴘᴛ : ᴘᴏʀᴛᴜɢᴜᴇsᴇ" + "\n" + \
                        "╠❂➣ " + key + "ᴘᴀ : ᴘᴜɴᴊᴀʙɪ" + "\n" + \
                        "╠❂➣ " + key + "ʀᴏ : ʀᴏᴍᴀɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ʀᴜ : ʀᴜssɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "sᴍ : sᴀᴍᴏᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ɢᴅ : sᴄᴏᴛs ɢᴀᴇʟɪᴄ" + "\n" + \
                        "╠❂➣ " + key + "sʀ : sᴇʀʙɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "sᴛ : sᴇsᴏᴛʜᴏ" + "\n" + \
                        "╠❂➣ " + key + "sɴ : sʜᴏɴᴀ" + "\n" + \
                        "╠❂➣ " + key + "sᴅ : sɪɴᴅʜɪ" + "\n" + \
                        "╠❂➣ " + key + "sɪ : sɪɴʜᴀʟᴀ" + "\n" + \
                        "╠❂➣ " + key + "sᴋ : sʟᴏᴠᴀᴋ" + "\n" + \
                        "╠❂➣ " + key + "sʟ : sʟᴏᴠᴇɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "sᴏ : sᴏᴍᴀʟɪ" + "\n" + \
                        "╠❂➣ " + key + "ᴇs : sᴘᴀɴɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "sᴜ : sᴜɴᴅᴀɴᴇsᴇ" + "\n" + \
                        "╠❂➣ " + key + "sᴡ : sᴡᴀʜɪʟɪ" + "\n" + \
                        "╠❂➣ " + key + "sᴠ : sᴡᴇᴅɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴛɢ : ᴛᴀᴊɪᴋ" + "\n" + \
                        "╠❂➣ " + key + "ᴛᴀ : ᴛᴀᴍɪʟ" + "\n" + \
                        "╠❂➣ " + key + "ᴛᴇ : ᴛᴇʟᴜɢᴜ" + "\n" + \
                        "╠❂➣ " + key + "ᴛʜ : ᴛʜᴀɪ" + "\n" + \
                        "╠❂➣ " + key + "ᴛʀ : ᴛᴜʀᴋɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴜᴋ : ᴜᴋʀᴀɪɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴜʀ : ᴜʀᴅᴜ" + "\n" + \
                        "╠❂➣ " + key + "ᴜᴢ : ᴜᴢʙᴇᴋ" + "\n" + \
                        "╠❂➣ " + key + "ᴠɪ : ᴠɪᴇᴛɴᴀᴍᴇsᴇ" + "\n" + \
                        "╠❂➣ " + key + "ᴄʏ : ᴡᴇʟsʜ" + "\n" + \
                        "╠❂➣ " + key + "xʜ : xʜᴏsᴀ" + "\n" + \
                        "╠❂➣ " + key + "ʏɪ : ʏɪᴅᴅɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ʏᴏ : ʏᴏʀᴜʙᴀ" + "\n" + \
                        "╠❂➣ " + key + "ᴢᴜ : ᴢᴜʟᴜ" + "\n" + \
                        "╠❂➣ " + key + "ғɪʟ : ғɪʟɪᴘɪɴᴏ" + "\n" + \
                        "╠❂➣ " + key + "ʜᴇ : ʜᴇʙʀᴇᴡ" + "\n" + \
                        "╠════════════════════╗" + "\n" + \
                        "              ᴄʀᴇᴅɪᴛs ʙʏ : ©ᴅ̶ᴇ̶ᴇ̶ ✯" + "\n" + \
                        "╚════════════════════╝" + "\n" + \
                        "╔════════════════════╗" + "\n" + \
                        "                    ✰ ᴅɴᴀ ʙᴏᴛ ✰" + "\n" + \
                        "╚════════════════════╝" + "\n" + \
                        "ᴄᴏɴᴛᴏʜ : " + key + "ᴛʀ-ɪᴅ ʀɪʀɪɴ"
    return helpTranslate
    
def ririnBot(op):
    try:
        if op.type == 0:
            print ("[ 0 ] Succes")
            return

        if op.type == 5:
            print ("[ 5 ] Add Contact")
            if wait["autoAdd"] == True:
                ririn.findAndAddContactsByMid(op.param1)
            ririn.sendMessage(op.param1, "╔════════════════════╗\n                   「ᴀᴜᴛᴏ ʀᴇᴘʟʏ」\n                             ʙʏ:\n                    ✰ ᴅɴᴀ ʙᴏᴛ ✰\n╚════════════════════╝\n       ʜᴀʟʟᴏ, ᴛʜᴀɴᴋs ғᴏʀ ᴀᴅᴅ ᴍᴇ\n\n                    ᴏᴘᴇɴ ᴏʀᴅᴇʀ :\n               ✪ sᴇʟғʙᴏᴛ ᴏɴʟʏ ✪\n            ✪ sᴇʟғʙᴏᴛ + ᴀssɪsᴛ ✪\n                ✪ ʙᴏᴛ ᴘʀᴏᴛᴇᴄᴛ ✪\n              「ᴀʟʟ ʙᴏᴛ ᴘʏᴛʜᴏɴ з」\n\n         ᴍɪɴᴀᴛ ᴘᴄ ᴀᴋᴜɴ ᴅɪ ʙᴀᴡᴀʜ :\n        [line.me/ti/p/ppgIZ0JLDW]")

        if op.type == 11:
            if wait["Protectgr"] == True:
              if op.param2 not in admin:
                 if op.param2 not in Bots:
                 	X = dna2.getGroup(op.param1)
                 	X.preventedJoinByTicket = False
                 	dna2.updateGroup(X)
                 	Ticket = dna2.reissueGroupTicket(op.param1)
                 	dna10.acceptGroupInvitationByTicket(op.param1,Ticket)
                 	dna10.kickoutFromGroup(op.param1,[op.param2])
                 	dna10.leaveGroup(op.param1)
                 	X = dna1.getGroup(op.param1)
                 	X.preventedJoinByTicket = True
                 	dna1.updateGroup(X)

        if op.type == 13:
            print ("[ 13 ] Invite Into Group")
            if ririnMid in op.param3:
                if wait["autoJoin"] == True:
                    ririn.acceptGroupInvitation(op.param1)
                dan = ririn.getContact(op.param2)
                tgb = ririn.getGroup(op.param1)
                sendMention(op.param1, "ʜᴀʟᴏ @!      ,ᴛʜx ғᴏʀ ɪɴᴠɪᴛᴇ ᴍᴇ".format(str(tgb.name)),[op.param2])
                ririn.sendContact(op.param1, op.param2)
                ririn.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath))
                
        if op.type == 13:
           if wait["Protectinvite"] == True:
              if op.param2 not in admin:
                 if op.param2 not in Bots:
                    ririn.cancelGroupInvitation(op.param1,[op.param3])
                    dan = ririn.getContact(op.param2)
                    tgb = ririn.getGroup(op.param1)
                    sendMention(op.param1, "ᴍᴀᴜ ɴɢᴜɴᴅᴀɴɢ sɪᴀᴘᴀ ᴋᴀ @!       \nᴋᴋ ʙᴜᴋᴀɴ ᴀᴅᴍɪɴ\nᴊᴀᴅɪ ᴀᴋᴜ ᴄᴀɴᴄᴇʟ 😛".format(str(tgb.name)),[op.param2])
                    
        if op.type == 13:
                if op.param3 in ririnMid:
                    if op.param2 in aMid:
                        G = dna1.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        dna1.updateGroup(G)
                        Ticket = dna1.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ririn.updateGroup(G)
                        Ticket = ririn.reissueGroupTicket(op.param1)

                if op.param3 in aMid:
                    if op.param2 in bMid:
                        X = dna2.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        dna2.updateGroup(X)
                        Ti = dna2.reissueGroupTicket(op.param1)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        dna1.updateGroup(X)
                        Ti = dna1.reissueGroupTicket(op.param1)

                if op.param3 in bMid:
                    if op.param2 in cMid:
                        X = dna3.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        dna3.updateGroup(X)
                        Ti = dna3.reissueGroupTicket(op.param1)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        dna2.updateGroup(X)
                        Ti = dna2.reissueGroupTicket(op.param1)
                        
                if op.param3 in cMid:
                    if op.param2 in dMid:
                        X = dna4.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        dna4.updateGroup(X)
                        Ti = dna4.reissueGroupTicket(op.param1)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        dna3.updateGroup(X)
                        Ti = dna3.reissueGroupTicket(op.param1)

                if op.param3 in dMid:
                    if op.param2 in eMid:
                        X = dna5.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        dna5.updateGroup(X)
                        Ti = dna5.reissueGroupTicket(op.param1)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        dna4.updateGroup(X)
                        Ti = dna4.reissueGroupTicket(op.param1)
                        
                if op.param3 in eMid:
                    if op.param2 in ririnMid:
                        G = ririn.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ririn.updateGroup(G)
                        Ticket = ririn.reissueGroupTicket(op.param1)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        dna5.updateGroup(G)
                        Ticket = dna5.reissueGroupTicket(op.param1)
                        
        if op.type == 13:
            if ririnMid in op.param3:
                G = ririn.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            ririn.rejectGroupInvitation(op.param1)
                        else:
                            ririn.acceptGroupInvitation(op.param1)
                    else:
                        ririn.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        ririn.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    ririn.cancelGroupInvitation(op.param1, matched_list)
                
        if op.type == 15:
        	dan = ririn.getContact(op.param2)
        	tgb = ririn.getGroup(op.param1)
        	sendMention(op.param1, "ɴᴀʜ ᴋᴀɴ ʙᴀᴘᴇʀ @!      , ɢᴀᴋ ᴜsᴀʜ ʙᴀʟɪᴋ ᴅɪ {} ʟᴀɢɪ ʏᴀ\nsᴇʟᴀᴍᴀᴛ ᴊᴀʟᴀɴ ᴅᴀɴ sᴇᴍᴏɢᴀʜ ᴛᴇɴᴀɴɢ ᴅɪʟᴜᴀʀ sᴀɴᴀ 😘😘😘".format(str(tgb.name)),[op.param2])
        	ririn.sendContact(op.param1, op.param2)
        	ririn.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath))
        	
        if op.type == 17:
        	dan = ririn.getContact(op.param2)
        	tgb = ririn.getGroup(op.param1)
        	sendMention(op.param1, "ʜᴏʟᴀ @!         ,\nᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ɢʀᴏᴜᴘ {} \nᴊᴀɴɢᴀɴ ʟᴜᴘᴀ ᴄʜᴇᴄᴋ ɴᴏᴛᴇ ʏᴀ \nᴀᴡᴀs ᴋᴀʟᴀᴜ ʙᴀᴘᴇʀᴀɴ 😘😘😘".format(str(tgb.name)),[op.param2])
        	ririn.sendContact(op.param1, op.param2)
        	ririn.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath))
        	
        if op.type == 17:
            if wait["Protectjoin"] == True:
                if op.param2 not in admin:
                    try:
                        contact = ririn.getContact(op.param2)
                        random.choice(KAC).cancelGroupInvitation(op.param1,[op.param2])
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except Exception as e:
                        print(e)

        if op.type == 17:
           if op.param2 in wait["blacklist"]:
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])

        if op.type == 19:
           if op.param2 not in admin:
              if op.param2 not in Bots:
                 if op.param2 not in wait["whitelist"]:
                    wait["blacklist"][op.param2] = True
                    print("kicker kicked")
                 else:
                    pass

        if op.type == 19:
              if op.param2 not in admin:
                 if op.param2 not in Bots:
                  try:
                   random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  except:
                      try:
                          random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                          random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                      except:
                          print ("User Kick")

        if op.type == 19:
           if op.param3 in admin:
               try:
                   random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                   random.choice(KAC).inviteIntoGroup(op.param1,admin)
               except:
                   try:
                       random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                       random.choice(KAC).inviteIntoGroup(op.param1,admin)
                   except:
                       print ("Admin Kicked")
                       
                       
        if op.type == 19:
          if op.param2 in Bots:
            pass
          if op.param2 in admin:
            pass
          else:
            if op.param3 in ririnMid:
              if op.param2 not in Bots or admin:
                try:
                  G = dna5.getGroup(op.param1)
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  dna5.updateGroup(G)
                  Ticket = dna5.reissueGroupTicket(op.param1)
                  ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  ririn.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1)
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            if op.param3 in aMid:
              if op.param2 not in Bots or admin:
                try:
                  G = ririn.getGroup(op.param1)
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  ririn.updateGroup(G)
                  Ticket = ririn.reissueGroupTicket(op.param1)
                  dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  dna1.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1)
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            if op.param3 in bMid:
              if op.param2 not in Bots or admin:
                try:
                  G = dna1.getGroup(op.param1)
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  dna1.updateGroup(G)
                  Ticket = dna1.reissueGroupTicket(op.param1)
                  dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  dna2.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1)
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            if op.param3 in cMid:
              if op.param2 not in Bots or admin:
                try:
                  G = dna2.getGroup(op.param1)
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  dna2.updateGroup(G)
                  Ticket = dna2.reissueGroupTicket(op.param1)
                  dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  dna3.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1)
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            if op.param3 in dMid:
              if op.param2 not in Bots or admin:
                try:
                  G = dna3.getGroup(op.param1)
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  dna3.updateGroup(G)
                  Ticket = dna3.reissueGroupTicket(op.param1)
                  dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  dna4.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1)
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            if op.param3 in eMid:
              if op.param2 not in Bots or admin:
                try:
                  G = dna4.getGroup(op.param1)
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  dna4.updateGroup(G)
                  Ticket = dna4.reissueGroupTicket(op.param1)
                  dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  dna5.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1)
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)

        if op.type == 22:
            if wait["leaveRoom"] == True:
                ririn.leaveRoom(op.param1)

        if op.type == 24:
            if wait["leaveRoom"] == True:
                ririn.leaveRoom(op.param1)
                
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg._from
                if msg._from == ririnMid:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            ririn.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = ririn.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            ririn.updateGroup(X)
                        except:
                            ririn.sendMessage(msg.to,"ᴇʀʀᴏʀ")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    ririn.leaveRoom(msg.to)
                
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        ririn.sendMessage(msg.to,"ᴀʟʀᴇᴀᴅʏ")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        ririn.sendMessage(msg.to,"ᴅᴇᴄɪᴅᴇᴅ ɴᴏᴛ ᴛᴏ ᴄᴏᴍᴍᴇɴᴛ")
                        
               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        ririn.sendMessage(msg.to,"ᴅᴇʟᴇᴛᴇᴅ")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        ririn.sendMessage(msg.to,"It is not in the black list")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        ririn.sendMessage(msg.to,"ᴀʟʀᴇᴀᴅʏ")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        ririn.sendMessage(msg.to,"ᴀᴅᴅᴇᴅ")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        ririn.sendMessage(msg.to,"ᴅᴇʟᴇᴛᴇᴅ")
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        ririn.sendMessage(msg.to,"ɪᴛ ɪs ɴᴏᴛ ɪɴ ᴛʜᴇ ʙʟᴀᴄᴋ ʟɪsᴛ")
                
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
                if wait["invite"] == True:
                    _name = msg.contentMetadata["displayName"]
                    invite = msg.contentMetadata["mid"]
                    groups = ririn.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            ririn.sendMessage(msg.to, _name +  "sᴜᴅᴀʜ ᴅɪ ᴅᴀʟᴀᴍ ɢʀᴜᴘ")
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                ririn.findAndAddContactsByMid(target)
                                ririn.inviteIntoGroup(msg.to,[target])
                                ririn.sendMessage(msg.to,"Invite " + _name)
                                wait["invite"] = False
                                break                              
                            except:             
                                    ririn.sendMessage(msg.to,"ᴇʀʀᴏʀ")
                                    wait["invite"] = False
                                    break
            else:
                if wait["invite"] == True:
                    _name = msg.contentMetadata["displayName"]
                    invite = msg.contentMetadata["mid"]
                    groups = dna1.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            dna1.sendMessage(msg.to, _name + "sᴜᴅᴀʜ ᴅɪ ᴅᴀʟᴀᴍ ɢʀᴜᴘ")
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                dna1.findAndAddContactsByMid(target)
                                dna1.inviteIntoGroup(msg.to,[target])
                                dna1.sendMessage(msg.to,"Invite " + _name)
                                wait["invite"] = False
                                break                              
                            except:             
                                    dna1.sendMessage(msg.to,"ᴇʀʀᴏʀ")
                                    wait["invite"] = False
                                    break

        if op.type == 26:
            try:
                print ("[ 26 ] SEND MESSAGE")
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                setKey = wait["keyCommand"].title()
                if wait["setKey"] == False:
                    setKey = ''
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                        if sender != ririn.profile.mid:
                            to = sender
                        else:
                            to = receiver
                    elif msg.toType == 1:
                        to = receiver
                    elif msg.toType == 2:
                        to = receiver
                    if msg.contentType == 0:
                        if text is None:
                            return
                        else:
                            cmd = command(text)
                            if cmd == "help":
                                helpMessage = helpmessage()
                                ririn.sendMessage(msg.to, str(helpMessage))
                                ririn.sendContact(to, "u39b98d8a2032c9bb289f583811a2b941")
                            elif cmd == "tts":
                                helpTextToSpeech = helptexttospeech()
                                ririn.sendMessage(msg.to, str(helpTextToSpeech))
                                ririn.sendContact(to, "u39b98d8a2032c9bb289f583811a2b941")
                            elif cmd == "translate":
                                helpTranslate = helptranslate()
                                ririn.sendMessage(msg.to, str(helpTranslate))
                                ririn.sendContact(to, "u39b98d8a2032c9bb289f583811a2b941")
                            elif cmd.startswith("changekey:"):
                                sep = text.split(" ")
                                key = text.replace(sep[0] + " ","")
                                if " " in key:
                                    ririn.sendMessage(msg.to, "ᴅᴏɴ'ᴛ ᴛʏᴘᴏ ʙʀᴏ")
                                else:
                                    wait["keyCommand"] = str(key).lower()
                                    ririn.sendMessage(msg.to, "sᴜᴄᴄᴇs ᴄʜᴀɴɢᴇ ᴋᴇʏ [ {} ]".format(str(key).lower()))
                            elif cmd == "sp":
                            	if msg._from in admin:
                            		ririn.sendMessage(msg.to, "❂➣ ʟᴏᴀᴅɪɴɢ...")
                            		sp = int(round(time.time() *1000))
                            		ririn.sendMessage(msg.to,"ᴍʏ sᴘᴇᴇᴅ : %sms" % (sp - op.createdTime))
                            elif cmd == "speed":
                            	if msg._from in admin:
                            		start = time.time()
                            		ririn.sendMessage(msg.to, "❂➣ ʟᴏᴀᴅɪɴɢ...")
                            		elapsed_time = time.time() - start
                            		ririn.sendMessage(msg.to, "ᴍʏ sᴘᴇᴇᴅ : %sms" % (elapsed_time))
                            elif cmd == "runtime":
                            	if msg._from in Owner:
                            		timeNow = time.time()
                            		runtime = timeNow - botStart
                            		runtime = format_timespan(runtime)
                            		ririn.sendMessage(msg.to, "ʀᴜɴɴɪɴɢ ɪɴ.. {}".format(str(runtime)))
                            elif cmd == "restart":
                            	if msg._from in Owner:
                            		ririn.sendMessage(msg.to, "ʙᴏᴛ ʜᴀᴠᴇ ʙᴇᴇɴ ʀᴇsᴛᴀʀᴛ")
                            		restartBot()
                            elif cmd == "ifconfig":
                            	if msg._from in Owner:
                            		botKernel = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE).communicate()[0]
                            		ririn.sendMessage(msg.to, str(botKernel) + "\n\n☢══〚 sᴇʀᴠᴇʀ ɪɴғᴏ ɴᴇᴛsᴛᴀᴛ 〛══☢")
                            elif cmd == "system":
                            	if msg._from in Owner:
                            		botKernel = subprocess.Popen(["df","-h"], stdout=subprocess.PIPE).communicate()[0]
                            		ririn.sendMessage(msg.to, str(botKernel) + "\n\n☢══〚 sᴇʀᴠᴇʀ ɪɴғᴏ sʏsᴛᴇᴍ 〛══☢")
                            elif cmd == "kernel":
                            	if msg._from in Owner:
                            		botKernel = subprocess.Popen(["uname","-srvmpio"], stdout=subprocess.PIPE).communicate()[0]
                            		ririn.sendMessage(msg.to, str(botKernel) + "\n\n☢══〚 sᴇʀᴠᴇʀ ɪɴғᴏ ᴋᴇʀɴᴇʟ 〛══☢")
                            elif cmd == "cpu":
                            	if msg._from:
                            		botKernel = subprocess.Popen(["cat","/proc/cpuinfo"], stdout=subprocess.PIPE).communicate()[0]
                            		ririn.sendMessage(msg.to, str(botKernel) + "\n\n☢══〚 sᴇʀᴠᴇʀ ɪɴғᴏ ᴄᴘᴜ 〛══☢")

                            elif cmd == "come dna":
                            	if msg._from in Owner:
                            		G = ririn.getGroup(msg.to)
                            		ginfo = ririn.getGroup(msg.to)
                            		G.preventedJoinByTicket = False
                            		ririn.updateGroup(G)
                            		invsend = 0
                            		Ticket = ririn.reissueGroupTicket(msg.to)
                            		dna1.acceptGroupInvitationByTicket(msg.to,Ticket)
                            		time.sleep(0.01)
                            		dna2.acceptGroupInvitationByTicket(msg.to,Ticket)
                            		time.sleep(0.01)
                            		dna3.acceptGroupInvitationByTicket(msg.to,Ticket)
                            		time.sleep(0.01)
                            		dna4.acceptGroupInvitationByTicket(msg.to,Ticket)
                            		time.sleep(0.01)
                            		dna5.acceptGroupInvitationByTicket(msg.to,Ticket)
                            		time.sleep(0.01)
                            		dna6.acceptGroupInvitationByTicket(msg.to,Ticket)
                            		time.sleep(0.01)
                            		dna7.acceptGroupInvitationByTicket(msg.to,Ticket)
                            		time.sleep(0.01)
                            		dna8.acceptGroupInvitationByTicket(msg.to,Ticket)
                            		time.sleep(0.01)
                            		dna9.acceptGroupInvitationByTicket(msg.to,Ticket)
                            		time.sleep(0.01)
                            		G = dna1.getGroup(msg.to)
                            		ginfo = dna1.getGroup(msg.to)
                            		G.preventedJoinByTicket = True
                            		dna1.updateGroup(G)
                            elif cmd == "bye dna":
                            	if msg._from in Owner:
                            		if msg.toType == 2:
                            			ginfo = ririn.getGroup(msg.to)
                            			try:
                            				dna1.leaveGroup(msg.to)
                            				dna2.leaveGroup(msg.to)
                            				dna3.leaveGroup(msg.to)
                            				dna4.leaveGroup(msg.to)
                            				dna5.leaveGroup(msg.to)
                            				dna6.leaveGroup(msg.to)
                            				dna7.leaveGroup(msg.to)
                            				dna8.leaveGroup(msg.to)
                            				dna9.leaveGroup(msg.to)
                            			except:
                            				pass
                            elif cmd == "bye all":
                            	if msg._from in Owner:
                            		if msg.toType == 2:
                            			ginfo = ririn.getGroup(msg.to)
                            			try:
                            				dna1.leaveGroup(msg.to)
                            				dna2.leaveGroup(msg.to)
                            				dna3.leaveGroup(msg.to)
                            				dna4.leaveGroup(msg.to)
                            				dna5.leaveGroup(msg.to)
                            				dna6.leaveGroup(msg.to)
                            				dna7.leaveGroup(msg.to)
                            				dna8.leaveGroup(msg.to)
                            				dna9.leaveGroup(msg.to)
                            				ririn.leaveGroup(msg.to)
                            			except:
                            				pass
                            elif cmd == "respon":
                            	if msg._from in admin:
                            		ririn.sendMessage(msg.to,responsename)
                            		dna1.sendMessage(msg.to,responsename2)
                            		dna2.sendMessage(msg.to,responsename3)
                            		dna3.sendMessage(msg.to,responsename4)
                            		dna4.sendMessage(msg.to,responsename5)
                            		dna5.sendMessage(msg.to,responsename6)
                            		dna6.sendMessage(msg.to,responsename7)
                            		dna7.sendMessage(msg.to,responsename8)
                            		dna8.sendMessage(msg.to,responsename9)
                            		dna9.sendMessage(msg.to,responsename10)
                            		random.choice(KAC).sendMessage(msg.to,"ᴀʟʟ ᴄᴏᴍᴘʟᴇᴛᴇᴅ")
                            elif cmd == "absen":
                            	if msg._from in admin:
                            		ririn.sendContact(to, ririnMid)
                            		dna1.sendContact(to, aMid)
                            		dna2.sendContact(to, bMid)
                            		dna3.sendContact(to, cMid)
                            		dna4.sendContact(to, dMid)
                            		dna5.sendContact(to, eMid)
                            		dna6.sendContact(to, fMid)
                            		dna7.sendContact(to, gMid)
                            		dna8.sendContact(to, hMid)
                            		dna9.sendContact(to, iMid)
                            		random.choice(KAC).sendMessage(msg.to,"ᴀʟʟ ᴄᴏᴍᴘʟᴇᴛᴇᴅ")
                            elif cmd == "dna":
                            	if msg._from in admin:
                            		ririn.sendMessage(msg.to,"ᴀʟʀᴇᴀᴅʏ ᴏɴ")
                            		dna1.sendMessage(msg.to,"ᴀʟʀᴇᴀᴅʏ ᴏɴ")
                            		dna2.sendMessage(msg.to,"ᴀʟʀᴇᴀᴅʏ ᴏɴ")
                            		dna3.sendMessage(msg.to,"ᴀʟʀᴇᴀᴅʏ ᴏɴ")
                            		dna4.sendMessage(msg.to,"ᴀʟʀᴇᴀᴅʏ ᴏɴ")
                            		dna5.sendMessage(msg.to,"ᴀʟʀᴇᴀᴅʏ ᴏɴ")
                            		dna6.sendMessage(msg.to,"ᴀʟʀᴇᴀᴅʏ ᴏɴ")
                            		dna7.sendMessage(msg.to,"ᴀʟʀᴇᴀᴅʏ ᴏɴ")
                            		dna8.sendMessage(msg.to,"ᴀʟʀᴇᴀᴅʏ ᴏɴ")
                            		dna9.sendMessage(msg.to,"ᴀʟʀᴇᴀᴅʏ ᴏɴ")
                            		random.choice(KAC).sendMessage(msg.to,"ᴀʟʟ ᴄᴏᴍᴘʟᴇᴛᴇᴅ")
                            		
                            elif cmd.startswith("adminadd "):
                                if msg._from in Owner:
                                    MENTION = eval(msg.contentMetadata["MENTION"])
                                    key = MENTION["MENTIONEES"][0]["M"]
                                    admin.append(str(key))
                                    ririn.sendMessage(msg.to,"      ᴀᴅᴍɪɴ\n✰ ᴅɴᴀ ʙᴏᴛ ✰\n        ᴀᴅᴅ\n   ᴇxᴇᴄᴜᴛᴇᴅ")

                            elif cmd.startswith("admindel "):
                                if msg._from in Owner:
                                    MENTION = eval(msg.contentMetadata["MENTION"])
                                    key = MENTION["MENTIONEES"][0]["M"]
                                    admin.remove(str(key))
                                    ririn.sendMessage(msg.to,"      ᴀᴅᴍɪɴ\n✰ ᴅɴᴀ ʙᴏᴛ ✰\n     ʀᴇᴍᴏᴠᴇ\n   ᴇxᴇᴄᴜᴛᴇᴅ")

                            elif cmd == "adminlist":
                            	if admin == []:
                            		ririn.sendMessage(msg.to,"ᴛʜᴇ ᴀᴅᴍɪɴʟɪsᴛ ɪs ᴇᴍᴘᴛʏ")
                            	else:
                            		ririn.sendMessage(msg.to,"ᴡᴀɪᴛɪɴɢ ғᴏʀ ᴀᴅᴍɪɴʟɪsᴛ...")
                            		mc = "╔════════════════\n╠✪➣  ✰ ᴅɴᴀ ʙᴏᴛ ✰\n╠══✪〘 ᴀᴅᴍɪɴʟɪsᴛ 〙✪═══\n"
                            		for mi_d in admin:
                            			mc += "╠✪ " +ririn.getContact(mi_d).displayName + "\n"
                            		ririn.sendMessage(msg.to,mc + "╠════════════════\n╠✪〘 line.me/ti/p/~sosid001 〙\n╚════════════════")
                            		ririn.sendContact(to, "u39b98d8a2032c9bb289f583811a2b941")
                            elif cmd == "ownerlist":
                                try:
                                	arr = []
                                	owner = "u2ff21221ec149ca856b792c6dee280ff"
                                	creator = ririn.getContact(owner)
                                	ret_ = "╔════════════════"
                                	ret_ += "\n╠✪➣  ✰ ᴅɴᴀ ʙᴏᴛ ✰"
                                	ret_ += "\n╠══✪〘ᴏᴡɴᴇʀ ʟɪsᴛ〙✪═══"
                                	ret_ += "\n╠✪ ᴏᴡɴᴇʀʟɪsᴛ : : {}".format(creator.displayName)
                                	ret_ += "\n╠════════════════"
                                	ret_ += "\n╠✪〘 line.me/ti/p/~sosid001 〙"
                                	ret_ += "\n╚════════════════"
                                	ririn.sendMessage(msg.to,"ᴡᴀɪᴛɪɴɢ ғᴏʀ ᴏᴡɴᴇʀʟɪsᴛ...")
                                	ririn.sendMessage(msg.to, str(ret_))
                                	ririn.sendContact(to, "u39b98d8a2032c9bb289f583811a2b941")
                                except Exception as e:
                                	ririn.sendMessage(msg.to, str(e))
                            elif cmd == "about":
                                try:
                                	arr = []
                                	owner = "u2ff21221ec149ca856b792c6dee280ff"
                                	creator = ririn.getContact(owner)
                                	contact = ririn.getContact(ririnMid)
                                	grouplist = ririn.getGroupIdsJoined()
                                	contactlist = ririn.getAllContactIds()
                                	blockedlist = ririn.getBlockedContactIds()
                                	ret_ = "╔══[ ᴀʙᴏᴜᴛ ʙᴏᴛ ]"
                                	ret_ += "\n╠✪ ʟɪɴᴇ : {}".format(contact.displayName)
                                	ret_ += "\n╠✪ ɢʀᴏᴜᴘ : {}".format(str(len(grouplist)))
                                	ret_ += "\n╠✪ ғʀɪᴇɴᴅ : {}".format(str(len(contactlist)))
                                	ret_ += "\n╠✪ ʙʟᴏᴄᴋᴇᴅ : {}".format(str(len(blockedlist)))
                                	ret_ += "\n╠══[ ᴀʙᴏᴜᴛ ʙᴏᴛ ]"
                                	ret_ += "\n╠✪ ᴠᴇʀsɪᴏɴ : ᴘʀᴇᴍɪᴜᴍ ᴘʀᴏᴛᴇᴄᴛ ᴘʏз"
                                	ret_ += "\n╠✪ ᴄʀᴇᴀᴛᴏʀ : {}".format(creator.displayName)
                                	ret_ += "\n╚══[ ᴅᴏɴ'ᴛ ʙᴇ ʀᴇᴍᴀᴋᴇ 😝 ]"
                                	ririn.sendContact(to, "u39b98d8a2032c9bb289f583811a2b941")
                                	ririn.sendMessage(msg.to, str(ret_))
                                except Exception as e:
                                	ririn.sendMessage(msg.to, str(e))
#------------------------------------============================------------------------------------#
#======================-----------✰ ᴅɴᴀ ʙᴏᴛ ✰-----------======================#
#------------------------------------============================------------------------------------#
                            elif cmd.startswith("invitemid"):
                            	if msg._from in admin:
                            		midd = msg.text.replace("Invitemid","")
                            		ririn.findAndAddContactsByMid(midd)
                            		ririn.inviteIntoGroup(msg.to,[midd])
                            		print ("InviteMid Succes")
                            elif cmd == "invite":
                            	if msg._from in admin:
                            		wait["invite"] = True
                            		ririn.sendMessage(msg.to,"sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ")
                            		print ("Invite Contact Succes")
                            		
                            elif cmd == "ban":
                            	if msg._from in admin:
                            		wait["wblacklist"] = True
                            		ririn.sendMessage(msg.to,"sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ")
                            		print ("Ban Contact Succes")
                            elif cmd == "Unban":
                            	if msg._from in admin:
                            		wait["dblacklist"] = True
                            		ririn.sendMessage(msg.to,"sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ")
                            		print ("Unban Contact Succes")
                                	
                            elif "Ban @" in msg.text:
                            	if msg._from in admin:
                            		if msg.toType == 2:
                            			print("[Ban]ok")
                            			_name = msg.text.replace("Ban @","")
                            			_nametarget = _name.rstrip('  ')
                            			gs = ririn.getGroup(msg.to)
                            			targets = []
                            			for g in gs.members:
                            				if _nametarget == g.displayName:
                            					targets.append(g.mid)
                            			if targets == []:
                            				ririn.sendMessage(msg.to,"ᴛᴀʀɢᴇᴛ ɴᴏᴛ ғᴏᴜɴᴅ")
                            			else:
                            				for target in targets:
                            					try:
                            						wait["blacklist"][target] = True
                            						f=codecs.open('st2__b.json','w','utf-8')
                            						json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            						ririn.sendMessage(msg.to,"ᴛᴀʀɢᴇᴛ ʀᴇᴀᴅʏ")
                            					except:
                            						ririn.sendMessage(msg.to,"sᴜᴄᴄᴇs")
                            						
                            elif "Unban @" in msg.text:
                            	if msg._from in admin:
                            		if msg.toType == 2:
                            			print("[Unban]ok")
                            			_name = msg.text.replace("Unban @","")
                            			_nametarget = _name.rstrip('  ')
                            			gs = ririn.getGroup(msg.to)
                            			talrgets = []
                            			for g in gs.members:
                            				if _nametarget == g.displayName:
                            					targets.append(g.mid)
                            			if targets == []:
                            				ririn.sendMessage(msg.to,"ᴛᴀʀɢᴇᴛ ɴᴏᴛ ғᴏᴜɴᴅ")
                            			else:
                            				for target in targets:
                            					try:
                            						del wait["blacklist"][target]
                            						f=codecs.open('st2__b.json','w','utf-8')
                            						json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            						ririn.sendMessage(msg.to,"sᴜᴄᴄᴇs")
                            					except:
                            						ririn.sendMessage(msg.to,"sᴜᴄᴄᴇs")
                            						
                            elif "Blacklist @ " in msg.text:
                            	if msg._from in admin:
                            		_name = msg.text.replace("Blacklist @ ","")
                            		_kicktarget = _name.rstrip(' ')
                            		gs = dna2.getGroup(msg.to)
                            		targets = []
                            		for g in gs.members:
                            			if _kicktarget == g.displayName:
                            				targets.append(g.mid)
                            				if targets == []:
                            					ririn.sendMessage(msg.to,"ɴᴏᴛ ғᴏᴜɴᴅ")
                            				else:
                            					for target in targets:
                            						try:
                            							wait["blacklist"][target] = True
                            							f=codecs.open('st2__b.json','w','utf-8')
                            							json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            							ririn.sendMessage(msg.to,"sᴜᴄᴄᴇs")
                            						except:
                            							ririn.sendMessage(msg.to,"ᴇʀʀᴏʀ")
                            							
                            elif cmd == "cek ban":
                            	if msg._from in admin:
                            		if msg.toType == 2:
                            			group = ririn.getGroup(msg.to)
                            			gMembMids = [contact.mid for contact in group.members]
                            			matched_list = []
                            			for tag in wait["blacklist"]:
                            				matched_list+=filter(lambda str: str == tag, gMembMids)
                            			cocoa = ""
                            			for mm in matched_list:
                            				cocoa += mm + "\n"
                            			ririn.sendMessage(msg.to,cocoa + "")
                            			
                            elif cmd == "clear ban":
                            	if msg._from in admin:
                            		wait["blacklist"] = {}
                            		ririn.sendMessage(msg.to,"ᴅᴏɴᴇ")
                            		print ("Clear Ban Succes")
                            		
                            elif cmd == "banlist":
                            	if msg._from in admin:
                            		if wait["blacklist"] == {}:
                            			ririn.sendMessage(msg.to,"ɴᴏᴛʜɪɴɢ")
                            		else:
                            			ririn.sendMessage(msg.to,"ʙʟᴀᴄᴋʟɪsᴛ ᴜsᴇʀ'")
                            			mc = ""
                            			for mi_d in wait["blacklist"]:
                            				mc += "->" +ririn.getContact(mi_d).displayName + "\n"
                            			ririn.sendMessage(msg.to,mc)
                            			print ("Banlist Send")
                            			
                            elif cmd == "kill ban":
                            	if msg._from in admin:
                            		if msg.toType == 2:
                            			group = ririn.getGroup(msg.to)
                            			gMembMids = [contact.mid for contact in group.members]
                            			matched_list = []
                            			for tag in wait["blacklist"]:
                            				matched_list+=filter(lambda str: str == tag, gMembMids)
                            			if matched_list == []:
                            				ririn.sendMessage(msg.to,"ᴛʜᴇʀᴇ ᴡᴀs ɴᴏ ʙʟᴀᴄᴋʟɪsᴛ ᴜsᴇʀ")
                            				return
                            			for jj in matched_list:
                            				random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                            			ririn.sendMessage(msg.to,"ᴜʀ ғᴠᴄᴋɪɴɢ ʙɪᴛɔʜ")
                            			print ("Kill Ban Succes") 
                            			
                            elif "!kickall" in msg.text:
                            	gs = ririn.getGroup(msg.to)
                            	try:
                            		klist=[ririn,dna1,dna2,dna3,dna4,dna5,dna6,dna7,dna8,dna9]
                            		kicker=random.choice(klist)
                            		kicker.kickoutFromGroup(msg.to,["op.param2"])
                            	except:
                            		ririn.sendMessage(msg.to,"sᴇᴇ ʏᴀ...")
                            			
                            elif "Nk " in msg.text:
                            	if msg._from in admin:
                            		nk0 = msg.text.replace("Nk ","")
                            		nk1 = nk0.lstrip()
                            		nk2 = nk1.replace("@","")
                            		nk3 = nk2.rstrip()
                            		_name = nk3
                            		gs = ririn.getGroup(msg.to)
                            		targets = []
                            		for s in gs.members:
                            			if _name in s.displayName:
                            				targets.append(s.mid)
                            		if targets == []:
                            			sendMessage(msg.to,"ᴜsᴇʀ ᴅᴏᴇs ɴᴏᴛ ᴇxɪsᴛ")
                            			pass
                            		else:
                            			for target in targets:
                            				try:
                            					klist=[ririn,dna1,dna2,dna3,dna4,dna5,dna6,dna7,dna8,dna9]
                            					kicker=random.choice(klist)
                            					kicker.kickoutFromGroup(msg.to,[target])
                            					print (msg.to,[g.mid])
                            				except:
                            					ririn.sendMessage(msg.to,"sᴇᴇ ʏᴀ...")
                            					
                            elif "Steal " in msg.text:
                            	if msg._from in admin:
                            		nk0 = msg.text.replace("Steal ","")
                            		nk1 = nk0.lstrip()
                            		nk2 = nk1.replace("@","")
                            		nk3 = nk2.rstrip()
                            		_name = nk3
                            		gs = ririn.getGroup(msg.to)
                            		ginfo = ririn.getGroup(msg.to)
                            		gs.preventedJoinByTicket = False
                            		ririn.updateGroup(gs)
                            		invsend = 0
                            		Ticket = ririn.reissueGroupTicket(msg.to)
                            		dna10.acceptGroupInvitationByTicket(msg.to,Ticket)
                            		time.sleep(0.01)
                            		targets = []
                            		for s in gs.members:
                            			if _name in s.displayName:
                            				targets.append(s.mid)
                            		if targets == []:
                            			sendMessage(msg.to,"ᴜsᴇʀ ᴅᴏᴇs ɴᴏᴛ ᴇxɪsᴛ")
                            			pass
                            		else:
                            			for target in targets:
                            				try:
                            					dna9.sendMessage(msg.to,"sᴇᴍᴏɢᴀ ᴋᴀᴜ ʙᴀʜᴀɢɪᴀ ᴅɪ ɴᴇʀᴀᴋᴀ 👹👹")
                            					dna10.kickoutFromGroup(msg.to,[target])
                            					print (msg.to,[g.mid])
                            				except:
                            					dna10.leaveGroup(msg.to)
                            					gs = dna1.getGroup(msg.to)
                            					gs.preventedJoinByTicket = True
                            					dna1.updateGroup(gs)
                            					gs.preventedJoinByTicket(gs)
                            					dna1.updateGroup(gs)
                            					print ("Steal Succes")
                            				
#------------------------------------============================------------------------------------#
#======================-----------✰ ᴅɴᴀ ʙᴏᴛ ✰-----------======================#
#------------------------------------============================------------------------------------#
                            elif cmd == "autoadd on":
                            	if msg._from in Owner:
                            		wait["autoAdd"] = True
                            		ririn.sendMessage(msg.to, "ᴀᴜᴛᴏ ᴀᴅᴅ ᴏɴ")
                            elif cmd == "autoadd off":
                            	if msg._from in Owner:
                            		wait["autoAdd"] = False
                            		ririn.sendMessage(msg.to, "ᴀᴜᴛᴏ ᴀᴅᴅ ᴏғғ")
                            elif cmd == "autojoin on":
                            	if msg._from in Owner:
                            		wait["autoJoin"] = True
                            		ririn.sendMessage(msg.to, "ᴀᴜᴛᴏ ᴊᴏɪɴ ᴏɴ")
                            elif cmd == "autojoin off":
                            	if msg._from in Owner:
                            		wait["autoJoin"] = False
                            		ririn.sendMessage(msg.to, "ᴀᴜᴛᴏ ᴊᴏɪɴ ᴏɴ ᴏғғ")
                            elif cmd == "autoleave on":
                            	if msg._from in Owner:
                            		wait["autoLeave"] = True
                            		ririn.sendMessage(msg.to, "ᴀᴜᴛᴏ ʟᴇᴀᴠᴇ ᴏɴ")
                            elif cmd == "autoleave off":
                            	if msg._from in Owner:
                            		wait["autoLeave"] = False
                            		ririn.sendMessage(msg.to, "ᴀᴜᴛᴏ ʟᴇᴀᴠᴇ ᴏғғ")
                            elif cmd == "autoresponpc on":
                            	if msg._from in Owner:
                            		wait["autoResponPc"] = True
                            		ririn.sendMessage(msg.to, "ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ ғᴏʀ ᴘᴇʀsᴏɴᴀʟ ᴄʜᴀᴛ ᴏɴ")
                            elif cmd == "autoresponpc off":
                            	if msg._from in Owner:
                            		wait["autoResponPc"] = False
                            		ririn.sendMessage(msg.to, "ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ ғᴏʀ ᴘᴇʀsᴏɴᴀʟ ᴄʜᴀᴛ ᴏғғ")
                            elif cmd == "autorespon on":
                            	if msg._from in Owner:
                            		wait["autoRespon"] = True
                            		ririn.sendMessage(msg.to, "ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ ᴏɴ")
                            elif cmd == "autorespon off":
                            	if msg._from in Owner:
                            		wait["autoRespon"] = False
                            		ririn.sendMessage(msg.to, "ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ ᴏғғ")
                            elif cmd == "autoread on":
                            	if msg._from in Owner:
                            		wait["autoRead"] = True
                            		ririn.sendMessage(msg.to, "ᴀᴜᴛᴏ ʀᴇᴀᴅ ᴏɴ")
                            elif cmd == "autoread off":
                            	if msg._from in Owner:
                            		wait["autoRead"] = False
                            		ririn.sendMessage(msg.to, "ᴀᴜᴛᴏ ʀᴇᴀᴅ ᴏғғ")
                            elif cmd == "autojointicket on":
                            	if msg._from in Owner:
                            		wait["autoJoinTicket"] = True
                            		ririn.sendMessage(msg.to, "ᴊᴏɪɴ ʙʏ ᴛɪᴄᴋᴇᴛ ᴏɴ")
                            elif cmd == "autoJoinTicket off":
                            	if msg._from in Owner:
                            		wait["autoJoin"] = False
                            		ririn.sendMessage(msg.to, "ᴊᴏɪɴ ʙʏ ᴛɪᴄᴋᴇᴛ ᴏғғ")
                            elif cmd == "contact on":
                            	if msg._from in Owner:
                            		wait["checkContact"] = True
                            		ririn.sendMessage(msg.to, "ᴄʜᴇᴄᴋ ᴄᴏɴᴛᴀᴄᴛ ᴏɴ")
                            elif cmd == "contact off":
                            	if msg._from in Owner:
                            		wait["checkContact"] = False
                            		ririn.sendMessage(msg.to, "ᴄʜᴇᴄᴋ ᴄᴏɴᴛᴀᴄᴛ ᴏғғ")
                            elif cmd == "checkpost on":
                            	if msg._from in admin:
                            		wait["checkPost"] = True
                            		ririn.sendMessage(msg.to, "ᴄʜᴇᴄᴋ ᴘᴏsᴛ ᴏɴ")
                            elif cmd == "checkpost off":
                            	if msg._from in admin:
                            		wait["checkPost"] = False
                            		ririn.sendMessage(msg.to, "ᴄʜᴇᴄᴋ ᴘᴏsᴛ ᴏғғ")
                            elif cmd == "checksticker on":
                            	if msg._from in admin:
                            		wait["checkSticker"] = True
                            		ririn.sendMessage(msg.to, "ᴄʜᴇᴄᴋ sᴛɪᴄᴋᴇʀ ᴏɴ")
                            elif cmd == "checksticker off":
                            	if msg._from in admin:
                            		wait["checkSticker"] = False
                            		ririn.sendMessage(msg.to, "ᴄʜᴇᴄᴋ sᴛɪᴄᴋᴇʀ ᴏғғ")
                            elif cmd == "unsendchat on":
                            	if msg._from in Owner:
                            		wait["unsendMessage"] = True
                            		ririn.sendMessage(msg.to, "ᴜɴsᴇɴᴅ ᴍᴇssᴀɢᴇ ᴏɴ")
                            elif cmd == "unsendchat off":
                            	if msg._from in Owner:
                            		wait["unsendMessage"] = False
                            		ririn.sendMessage(msg.to, "ᴜɴsᴇɴᴅ ᴍᴇssᴀɢᴇ ᴏғғ")
                            elif cmd == "status":
                            	if msg._from in admin:
                            		try:
                            			ret_ = "╔═════[ ·✪·sᴛᴀᴛᴜs·✪· ]═════╗"
                            			if wait["autoAdd"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴀᴜᴛᴏ ᴀᴅᴅ 「⚪」"
                            			else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴀᴜᴛᴏ ᴀᴅᴅ 「⚫」"
                            			if wait["autoJoin"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴀᴜᴛᴏ ᴊᴏɪɴ 「⚪」"
                            			else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴀᴜᴛᴏ ᴊᴏɪɴ 「⚫」"
                            			if wait["autoLeave"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴀᴜᴛᴏ ʟᴇᴀᴠᴇ 「⚪」"
                            			else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴀᴜᴛᴏ ʟᴇᴀᴠᴇ 「⚫」"
                            			if wait["autoJoinTicket"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴊᴏɪɴ ᴛɪᴄᴋᴇᴛ 「⚪」"
                            			else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴊᴏɪɴ ᴛɪᴄᴋᴇᴛ 「⚫」"
                            			if wait["autoRead"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴀᴜᴛᴏ ʀᴇᴀᴅ 「⚪」"
                            			else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴀᴜᴛᴏ ʀᴇᴀᴅ 「⚫」"
                            			if wait["autoRespon"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ 「⚪」"
                            			else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ 「⚫」"
                            			if wait["autoResponPc"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ ᴘᴄ 「⚪」"
                            			else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ ᴘᴄ 「⚫」"
                            			if wait["checkContact"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴄʜᴇᴄᴋ ᴄᴏɴᴛᴀᴄᴛ 「⚪」"
                            			else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴄʜᴇᴄᴋ ᴄᴏɴᴛᴀᴄᴛ 「⚫」"
                            			if wait["checkPost"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴄʜᴇᴄᴋ ᴘᴏsᴛ 「⚪」"
                            			else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴄʜᴇᴄᴋ ᴘᴏsᴛ 「⚫」"
                            			if wait["checkSticker"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴄʜᴇᴄᴋ sᴛɪᴄᴋᴇʀ 「⚪」"
                            			else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴄʜᴇᴄᴋ sᴛɪᴄᴋᴇʀ 「⚫」"
                            			if wait["setKey"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] sᴇᴛ ᴋᴇʏ 「⚪」"
                            			else: ret_ += "\n╠❂➣ [ ᴏғғ ] sᴇᴛ ᴋᴇʏ 「⚫」"
                            			if wait["unsendMessage"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴜɴsᴇɴᴅ ᴍsɢ 「⚪」"
                            			else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴜɴsᴇɴᴅ ᴍsɢ 「⚫」"
                            			ret_ += "\n╚═════[ ✯ ᴅɴᴀ ʙᴏᴛ ✯ ]═════╝"
                            			ririn.sendMessage(msg.to, str(ret_))
                            			ririn.sendContact(to, "u39b98d8a2032c9bb289f583811a2b941")
                            		except Exception as e:
                            			ririn.sendMessage(msg.to, str(e))
                            elif cmd == "set":
                            	if msg._from in admin:
                            		try:
                            			ret_ = "╔═════[ ·✪·  s ᴇ ᴛ  ·✪· ]═════╗"
                            			if wait["Protectcancel"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴘʀᴏᴛᴇᴄᴛ ᴄᴀɴᴄᴇʟ 「🔒」"
                            			else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴘʀᴏᴛᴇᴄᴛ ᴄᴀɴᴄᴇʟ 「🔓」"
                            			if wait["Protectgr"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴘʀᴏᴛᴇᴄᴛ ɢʀ 「🔒」"
                            			else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴘʀᴏᴛᴇᴄᴛ ɢʀ 「🔓」"
                            			if wait["Protectinvite"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴘʀᴏᴛᴇᴄᴛ ɪɴᴠɪᴛᴇ 「🔒」"
                            			else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴘʀᴏᴛᴇᴄᴛ ɪɴᴠɪᴛᴇ 「🔓」"
                            			if wait["Protectjoin"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴘʀᴏᴛᴇᴄᴛ ᴊᴏɪɴ 「🔒」"
                            			else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴘʀᴏᴛᴇᴄᴛ ᴊᴏɪɴ 「🔓」"
                            			ret_ += "\n╚═════[ ✯ ᴅɴᴀ ʙᴏᴛ ✯ ]═════╝"
                            			ririn.sendMessage(msg.to, str(ret_))
                            			ririn.sendContact(to, "u39b98d8a2032c9bb289f583811a2b941")
                            		except Exception as e:
                            			ririn.sendMessage(msg.to, str(e))
                            elif cmd == "procancel on":
                            	if msg._from in admin:
                            		wait["Protectcancel"] = True
                            		ririn.sendMessage(msg.to, "ᴘʀᴏᴛᴇᴄᴛɪᴏɴ ᴄᴀɴᴄᴇʟ ɪɴᴠɪᴛᴇ sᴇᴛ ᴛᴏ ᴏɴ")
                            elif cmd == "procancel off":
                            	if msg._from in admin:
                            		wait["Protectcancel"] = False
                            		ririn.sendMessage(msg.to, "ᴘʀᴏᴛᴇᴄᴛɪᴏɴ ᴄᴀɴᴄᴇʟ ɪɴᴠɪᴛᴇ sᴇᴛ ᴛᴏ ᴏғғ")
                            elif cmd == "progr on":
                            	if msg._from in admin:
                            		wait["Protectgr"] = True
                            		ririn.sendMessage(msg.to, "ᴘʀᴏᴛᴇᴄᴛɪᴏɴ ɢʀᴏᴜᴘ sᴇᴛ ᴛᴏ ᴏɴ")
                            elif cmd == "progr off":
                            	if msg._from in admin:
                            		wait["Protectgr"] = False
                            		ririn.sendMessage(msg.to, "ᴘʀᴏᴛᴇᴄᴛɪᴏɴ ɢʀᴏᴜᴘ sᴇᴛ ᴛᴏ ᴏғғ")
                            elif cmd == "proinvite on":
                            	if msg._from in admin:
                            		wait["Protectinvite"] = True
                            		ririn.sendMessage(msg.to, "ᴘʀᴏᴛᴇᴄᴛɪᴏɴ ɪɴᴠɪᴛᴇ sᴇᴛ ᴛᴏ ᴏɴ")
                            elif cmd == "proinvite off":
                            	if msg._from in admin:
                            		wait["Protectinvite"] = False
                            		ririn.sendMessage(msg.to, "ᴘʀᴏᴛᴇᴄᴛɪᴏɴ ɪɴᴠɪᴛᴇ sᴇᴛ ᴛᴏ ᴏғғ")
                            elif cmd == "projoin on":
                            	if msg._from in admin:
                            		wait["Protectjoin"] = True
                            		ririn.sendMessage(msg.to, "ᴘʀᴏᴛᴇᴄᴛɪᴏɴ ᴊᴏɪɴ sᴇᴛ ᴛᴏ ᴏɴ")
                            elif cmd == "projoin off":
                            	if msg._from in admin:
                            		wait["Protectjoin"] = False
                            		ririn.sendMessage(msg.to, "ᴘʀᴏᴛᴇᴄᴛɪᴏɴ ᴊᴏɪɴ sᴇᴛ ᴛᴏ ᴏғғ")
                            elif cmd == "setpro on":
                            	if msg._from in Owner:
                            		wait["Protectcancel"] = True
                            		ririn.sendMessage(msg.to, "➲ ᴘʀᴏᴛᴇᴄᴛ ᴄᴀɴᴄᴇʟ sᴇᴛ ᴛᴏ ᴏɴ")
                            		wait["Protectgr"] = True
                            		ririn.sendMessage(msg.to, "➲ ᴘʀᴏᴛᴇᴄᴛ ɢʀᴏᴜᴘ sᴇᴛ ᴛᴏ ᴏɴ")
                            		wait["Protectinvite"] = True
                            		ririn.sendMessage(msg.to, "➲ ᴘʀᴏᴛᴇᴄᴛ ɪɴᴠɪᴛᴇ sᴇᴛ ᴛᴏ ᴏɴ")
                            		wait["Protectjoin"] = True
                            		ririn.sendMessage(msg.to, "➲ ᴘʀᴏᴛᴇᴄᴛ ᴊᴏɪɴ sᴇᴛ ᴛᴏ ᴏɴ")
                            elif cmd == "setpro off":
                            	if msg._from in Owner:
                            		wait["Protectcancel"] = False
                            		ririn.sendMessage(msg.to, "➲ ᴘʀᴏᴛᴇᴄᴛ ᴄᴀɴᴄᴇʟ sᴇᴛ ᴛᴏ ᴏғғ")
                            		wait["Protectgr"] = False
                            		ririn.sendMessage(msg.to, "➲ ᴘʀᴏᴛᴇᴄᴛ ɢʀᴏᴜᴘ sᴇᴛ ᴛᴏ ᴏғғ")
                            		wait["Protectinvite"] = False
                            		ririn.sendMessage(msg.to, "➲ ᴘʀᴏᴛᴇᴄᴛ ɪɴᴠɪᴛᴇ sᴇᴛ ᴛᴏ ᴏғғ")
                            		wait["Protectjoin"] = False
                            		ririn.sendMessage(msg.to, "➲ ᴘʀᴏᴛᴇᴄᴛ ᴊᴏɪɴ sᴇᴛ ᴛᴏ ᴏғғ")
#------------------------------------============================------------------------------------#
#======================-----------✰ ᴅɴᴀ ʙᴏᴛ ✰-----------======================#
#------------------------------------============================------------------------------------#
                            elif cmd == "crash":
                            	if msg._from in admin:
                            		ririn.sendContact(to, "u1f41296217e740650e0448b96851a3e2',")
                            elif cmd == "endchat":
                            	if msg._from in Owner:
                            		if wait["removechat"] == True:
                            			ririn.sendMessage(msg.to, "ᴘʀᴏsᴇs ʀᴇᴍᴏᴠᴇ ᴄʜᴀᴛ...")
                            		if wait["removechat"] == False:
                            			pass
                            elif cmd.startswith("changename:"):
                            	if msg._from in Owner:
                            		sep = text.split(" ")
                            		string = text.replace(sep[0] + " ","")
                            		if len(string) <= 20:
                            			profile = Bots.getProfile()
                            			profile.displayName = string
                            			Bots.updateProfile(profile)
                            			ririn.sendMessage(msg.to,"ᴄʜᴀɴɢᴇ ɴᴀᴍᴇ sᴜᴄᴄᴇs :{}".format(str(string)))
                            elif cmd.startswith("changebio:"):
                            	if msg._from in Owner:
                            		sep = text.split(" ")
                            		string = text.replace(sep[0] + " ","")
                            		if len(string) <= 500:
                            			profile = Bots.getProfile()
                            			profile.statusMessage = string
                            			Bots.updateProfile(profile)
                            			ririn.sendMessage(msg.to,"ᴄʜᴀɴɢᴇ ᴘʀᴏғɪʟᴇ sᴜᴄᴄᴇs :{}".format(str(string)))
                            elif cmd == "me":
                                ririn.sendContact(to, sender)
                            elif cmd == "mymid":
                                ririn.sendMessage(msg.to, "[ ᴍɪᴅ ]\n{}".format(sender))
                            elif cmd == "myname":
                                contact = ririn.getContact(sender)
                                ririn.sendMessage(msg.to, "[ ᴅɪsᴘʟᴀʏ ɴᴀᴍᴇ ]\n{}".format(contact.displayName))
                            elif cmd == "mybio":
                                contact = ririn.getContact(sender)
                                ririn.sendMessage(msg.to, "[ sᴛᴀᴛᴜs ᴍᴇssᴀɢᴇ ]\n{}".format(contact.statusMessage))
                            elif cmd == "mypicture":
                                contact = ririn.getContact(sender)
                                ririn.sendImageWithURL(to,"http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))
                            elif cmd == "myvideoprofile":
                                contact = ririn.getContact(sender)
                                ririn.sendVideoWithURL(to,"http://dl.profile.line-cdn.net/{}/vp".format(contact.pictureStatus))
                            elif cmd == "mycover":
                                channel = ririn.getProfileCoverURL(sender)          
                                path = str(channel)
                                ririn.sendImageWithURL(to, path)
                            elif cmd.startswith ('invitegc '):
                            	if msg._from in admin:
                            		if msg.toType == 2:
                            			sep = text.split(" ")
                            			strnum = text.replace(sep[0] + " ","")
                            			num = int(strnum)
                            			ririn.sendMessage(msg.to, "sᴜᴄᴄᴇs ɪɴᴠɪᴛᴇ ɢʀᴏᴜᴘ ᴄᴀʟʟ")
                            			for var in range(0,num):
                            				group = ririn.getGroup(to)
                            				members = [mem.mid for mem in group.members]
                            				ririn.inviteIntoGroupCall(to, contactIds=members)
                            elif cmd.startswith("cloneprofile "):
                            	if msg._from in Owner:
                            		if 'MENTION' in msg.contentMetadata.keys()!= None:
                            			names = re.findall(r'@(\w+)', text)
                            			mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            			mentionees = mention['MENTIONEES']
                            			lists = []
                            			for mention in mentionees:
                            				if mention["M"] not in lists:
                            					lists.append(mention["M"])
                            			for ls in lists:
                            				contact = Bots.getContact(ls)
                            				Bots.cloneContactProfile(ls)
                            				ririn.sendMessage(msg.to, "ᴄʟᴏɴᴇ ᴘʀᴏғɪʟᴇ sᴜᴄᴄᴇs : {}".format(contact.displayName))
                            elif cmd == "restoreprofile":
                            	if msg._from in Owner:
                                	try:
                                		ririnProfile = ririn.getProfile()
                                		ririnProfile.displayName = str(wait["myProfile"]["displayName"])
                                		ririnProfile.statusMessage = str(wait["myProfile"]["statusMessage"])
                                		ririnProfile.pictureStatus = str(wait["myProfile"]["pictureStatus"])
                                		ririn.updateProfileAttribute(8, ririnProfile.pictureStatus)
                                		ririn.updateProfile(ririnProfile)
                                		coverId = str(wait["myProfile"]["coverId"])
                                		ririn.updateProfileCoverById(coverId)
                                		ririn.sendMessage(msg.to, "ʀᴇsᴛᴏʀᴇ ᴘʀᴏғɪʟᴇ sᴜᴄᴄᴇs, ᴡᴀɪᴛ ᴀ ғᴇᴡ ᴍɪɴᴜᴛᴇs")
                                	except Exception as e:
                                		ririn.sendMessage(msg.to, "ʀᴇsᴛᴏʀᴇ ᴘʀᴏғɪʟᴇ ғᴀɪʟᴇᴅ")
                                		logError(error)
                            elif cmd == "backupprofile":
                            	if msg._from in Owner:
                            		try:
                            			profile = ririn.getProfile()
                            			wait["myProfile"]["displayName"] = str(profile.displayName)
                            			wait["myProfile"]["statusMessage"] = str(profile.statusMessage)
                            			wait["myProfile"]["pictureStatus"] = str(profile.pictureStatus)
                            			coverId = ririn.getProfileDetail()["result"]["objectId"]
                            			wait["myProfile"]["coverId"] = str(coverId)
                            			ririn.sendMessage(msg.to, "ʙᴀᴄᴋᴜᴘ ᴘʀᴏғɪʟᴇ sᴜᴄᴄᴇs")
                            		except Exception as e:
                            			ririn.sendMessage(msg.to, "ʙᴀᴄᴋᴜᴘ ᴘʀᴏғɪʟᴇ ғᴀɪʟᴇᴅ")
                            			logError(error)
                            elif cmd.startswith("stealmid "):
                            	if msg._from in admin:
                            		if 'MENTION' in msg.contentMetadata.keys()!= None:
                            			names = re.findall(r'@(\w+)', text)
                            			mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            			mentionees = mention['MENTIONEES']
                            			lists = []
                            			for mention in mentionees:
                            				if mention["M"] not in lists:
                            					lists.append(mention["M"])
                            				ret_ = "[ Mid User ]"
                            				for ls in lists:
                            					ret_ += "\n{}".format(str(ls))
                            				ririn.sendMessage(msg.to, str(ret_))
                            elif cmd.startswith("stealname "):
                            	if msg._from in admin:
                            		if 'MENTION' in msg.contentMetadata.keys()!= None:
                            			names = re.findall(r'@(\w+)', text)
                            			mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            			mentionees = mention['MENTIONEES']
                            			lists = []
                            			for mention in mentionees:
                            				if mention["M"] not in lists:
                            					lists.append(mention["M"])
                            				ret_ = "[ Mid User ]"
                            				for ls in lists:
                            					contact = ririn.getContact(ls)
                            					ririn.sendMessage(msg.to, "[ Display Name ]\n{}".format(str(contact.displayName)))
                            elif cmd.startswith("stealbio "):
                            	if msg._from in admin:
                            		if 'MENTION' in msg.contentMetadata.keys()!= None:
                            			names = re.findall(r'@(\w+)', text)
                            			mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            			mentionees = mention['MENTIONEES']
                            			lists = []
                            			for mention in mentionees:
                            				if mention["M"] not in lists:
                            					lists.append(mention["M"])
                            				for ls in lists:
                            					contact = ririn.getContact(ls)
                            					ririn.sendMessage(msg.to, "[ sᴛᴀᴛᴜs ᴍᴇssᴀɢᴇ ]\n{}".format(str(contact.statusMessage)))
                            	if msg._from in admin:
                            		if 'MENTION' in msg.contentMetadata.keys()!= None:
                            			names = re.findall(r'@(\w+)', text)
                            			mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            			mentionees = mention['MENTIONEES']
                            			lists = []
                            			for mention in mentionees:
                            				if mention["M"] not in lists:
                            					lists.append(mention["M"])
                            				for ls in lists:
                            					contact = ririn.getContact(ls)
                            					path = "http://dl.profile.line.naver.jp/{}".format(contact.pictureStatus)
                            					ririn.sendImageWithURL(to, str(path))
                            elif cmd.startswith("stealvideoprofile "):
                            	if msg._from in admin:
                            		if 'MENTION' in msg.contentMetadata.keys()!= None:
                            			names = re.findall(r'@(\w+)', text)
                            			mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            			mentionees = mention['MENTIONEES']
                            			lists = []
                            			for mention in mentionees:
                            				if mention["M"] not in lists:
                            					lists.append(mention["M"])
                            				for ls in lists:
                            					contact = ririn.getContact(ls)
                            					path = "http://dl.profile.line.naver.jp/{}/vp".format(contact.pictureStatus)
                            					ririn.sendVideoWithURL(to, str(path))
                            elif cmd.startswith("stealcover "):
                            	if msg._from in admin:
                            		if ririn != None:
                            			if 'MENTION' in msg.contentMetadata.keys()!= None:
                            				names = re.findall(r'@(\w+)', text)
                            				mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            				mentionees = mention['MENTIONEES']
                            				lists = []
                            				for mention in mentionees:
                            					if mention["M"] not in lists:
                            						lists.append(mention["M"])
                            					for ls in lists:
                            						channel = ririn.getProfileCoverURL(ls)
                            						path = str(channel)
                            						ririn.sendImageWithURL(to, str(path))
#------------------------------------============================------------------------------------#
#======================-----------✰ ᴅɴᴀ ʙᴏᴛ ✰-----------======================#
#------------------------------------============================------------------------------------#
                            elif cmd == 'groupcreator':
                                group = ririn.getGroup(to)
                                GS = group.creator.mid
                                ririn.sendContact(to, GS)
                            elif cmd == 'groupid':
                                gid = ririn.getGroup(to)
                                ririn.sendMessage(msg.to, "[ɢʀᴏᴜᴘ ɪᴅ : : ]\n" + gid.id)
                            elif cmd == 'grouppicture':
                                group = ririn.getGroup(to)
                                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                                ririn.sendImageWithURL(to, path)
                            elif cmd == 'groupname':
                                gid = ririn.getGroup(to)
                                ririn.sendMessage(msg.to, "[ɢʀᴏᴜᴘ ɴᴀᴍᴇ : ]\n" + gid.name)
                            elif cmd == 'groupticket':
                                if msg.toType == 2:
                                    group = ririn.getGroup(to)
                                    if group.preventedJoinByTicket == False:
                                        ticket = ririn.reissueGroupTicket(to)
                                        ririn.sendMessage(msg.to, "[ ɢʀᴏᴜᴘ ᴛɪᴄᴋᴇᴛ ]\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                                    else:
                                        ririn.sendMessage(msg.to, "ᴛʜᴇ ǫʀ ɢʀᴏᴜᴘ ɪs ɴᴏᴛ ᴏᴘᴇɴ ᴘʟᴇᴀsᴇ ᴏᴘᴇɴ ɪᴛ ғɪʀsᴛ ᴡɪᴛʜ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅ {}openqr".format(str(wait["keyCommand"])))
                            elif cmd == 'groupticket on':
                            	if msg._from in admin:
                            		if msg.toType == 2:
                            			group = ririn.getGroup(to)
                            			if group.preventedJoinByTicket == False:
                            				ririn.sendMessage(msg.to, "ᴀʟʀᴇᴀᴅʏ ᴏᴘᴇɴ")
                            			else:
                            				group.preventedJoinByTicket = False
                            				ririn.updateGroup(group)
                            				ririn.sendMessage(msg.to, "sᴜᴄᴄᴇs ᴏᴘᴇɴ ǫʀ ɢʀᴏᴜᴘ")
                            elif cmd == 'groupticket off':
                            	if msg._from in admin:
                            		if msg.toType == 2:
                            			group = ririn.getGroup(to)
                            			if group.preventedJoinByTicket == True:
                            				ririn.sendMessage(msg.to, "ᴀʟʀᴇᴀᴅʏ ᴄʟᴏsᴇᴅ")
                            			else:
                            				group.preventedJoinByTicket = True
                            				ririn.updateGroup(group)
                            				ririn.sendMessage(msg.to, "sᴜᴄᴄᴇs ᴄʟᴏsᴇ ǫʀ ɢʀᴏᴜᴘ")
                            elif cmd == 'groupinfo':
                                group = ririn.getGroup(to)
                                try:
                                    gCreator = group.creator.displayName
                                except:
                                    gCreator = "ɴᴏᴛ ғᴏᴜɴᴅ"
                                if group.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(group.invitee))
                                if group.preventedJoinByTicket == True:
                                    gQr = "ᴄʟᴏsᴇᴅ"
                                    gTicket = "ɴᴏʟ'"
                                else:
                                    gQr = "ᴏᴘᴇɴ"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(ririn.reissueGroupTicket(group.id)))
                                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                                ret_ = "╔════[ ·✪ɢʀᴏᴜᴘ ɪɴғᴏ✪· ]════╗"
                                ret_ += "\n╠❂➣ ɢʀᴏᴜᴘ ɴᴀᴍᴇ : {}".format(str(group.name))
                                ret_ += "\n╠❂➣ ɢʀᴏᴜᴘ ɪᴅ : {}".format(group.id)
                                ret_ += "\n╠❂➣ ᴄʀᴇᴀᴛᴏʀ :  {}".format(str(gCreator))
                                ret_ += "\n╠❂➣ ᴍᴇᴍʙᴇʀ : {}".format(str(len(group.members)))
                                ret_ += "\n╠❂➣ ᴘᴇɴᴅɪɴɢ : {}".format(gPending)
                                ret_ += "\n╠❂➣ ǫʀ ɢʀᴏᴜᴘ : {}".format(gQr)
                                ret_ += "\n╠❂➣ ᴛɪᴄᴋᴇᴛ ɢʀᴏᴜᴘ : {}".format(gTicket)
                                ret_ += "\n╚═════[ ✯ ᴅɴᴀ ʙᴏᴛ ✯ ]═════╝"
                                ririn.sendMessage(msg.to, str(ret_))
                                ririn.sendImageWithURL(to, path)
                            elif cmd == 'groupmemberlist':
                                if msg.toType == 2:
                                    group = ririn.getGroup(to)
                                    ret_ = "╔══[ ᴍᴇᴍʙᴇʀ  ʟɪsᴛ ]══✪"
                                    no = 0 + 1
                                    for mem in group.members:
                                        ret_ += "\n╠❂➣ {}. {}".format(str(no), str(mem.displayName))
                                        no += 1
                                    ret_ += "\n╚═══[ ᴛᴏᴛᴀʟ : {} ]═══✪".format(str(len(group.members)))
                                    ririn.sendMessage(msg.to, str(ret_))
                            elif cmd == 'grouplist':
                            	if msg._from in admin:
                                    groups = ririn.groups
                                    ret_ = "╔═[ ✯ ɢʀᴏᴜᴘ  ʟɪsᴛ ✯ ]═✪"
                                    no = 0 + 1
                                    for gid in groups:
                                        group = ririn.getGroup(gid)
                                        ret_ += "\n╠❂➣ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                                        no += 1
                                    ret_ += "\n╚═══[ ᴛᴏᴛᴀʟ : {} ]═══✪".format(str(len(groups)))
                                    ririn.sendMessage(msg.to, str(ret_))
#------------------------------------============================------------------------------------#
#======================-----------✰ ᴅɴᴀ ʙᴏᴛ ✰-----------======================#
#------------------------------------============================------------------------------------#
                            elif cmd == "changepictureprofile":
                            	if msg._from in Owner:
                            		wait["changePictureProfile"] = True
                            		ririn.sendMessage(msg.to, "sᴇɴᴅ ᴘɪᴄᴛᴜʀᴇ")
                            elif cmd == "changegrouppicture":
                            	if msg._from in admin:
                            		if msg.toType == 2:
                            			if to not in wait["changeGroupPicture"]:
                            				wait["changeGroupPicture"].append(to)
                            			ririn.sendMessage(msg.to, "sᴇɴᴅ ᴘɪᴄᴛᴜʀᴇ")
                            elif cmd == 'mention':
                                group = ririn.getGroup(msg.to)
                                nama = [contact.mid for contact in group.members]
                                k = len(nama)//100
                                for a in range(k+1):
                                    txt = u''
                                    s=0
                                    b=[]
                                    for i in group.members[a*100 : (a+1)*100]:
                                        b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                        s += 7
                                        txt += u'@Zero \n'
                                    ririn.sendMessage(msg.to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                                    ririn.sendMessage(msg.to, "Total {} Mention".format(str(len(nama))))
                                    
                            elif cmd == "sider on":
                            	if msg._from in admin:
                            		try:
                            			del cctv['point'][msg.to]
                            			del cctv['sidermem'][msg.to]
                            			del cctv['cyduk'][msg.to]
                            		except:
                            			pass
                            		cctv['point'][msg.to] = msg.id
                            		cctv['sidermem'][msg.to] = ""
                            		cctv['cyduk'][msg.to]=True
                            		wait["Sider"] = True
                            		ririn.sendMessage(msg.to,"sɪᴅᴇʀ sᴇᴛ ᴛᴏ ᴏɴ")
                            elif cmd == "sider off":
                            	if msg._from in admin:
                            		if msg.to in cctv['point']:
                            			cctv['cyduk'][msg.to]=False
                            			wait["Sider"] = False
                            			ririn.sendMessage(msg.to,"sɪᴅᴇʀ sᴇᴛ ᴛᴏ ᴏғғ")
                            		else:
                            			ririn.sendMessage(msg.to,"sɪᴅᴇʀ ɴᴏᴛ sᴇᴛ")           
                            elif cmd == "lurking on":
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if receiver in read['readPoint']:
                                    try:
                                        del read['readPoint'][receiver]
                                        del read['readMember'][receiver]
                                        del read['readTime'][receiver]
                                    except:
                                        pass
                                    read['readPoint'][receiver] = msg_id
                                    read['readMember'][receiver] = ""
                                    read['readTime'][receiver] = readTime
                                    read['ROM'][receiver] = {}
                                    ririn.sendMessage(receiver,"ʟᴜʀᴋɪɴɢ sᴇᴛ ᴏɴ")
                                else:
                                    try:
                                        del read['readPoint'][receiver]
                                        del read['readMember'][receiver]
                                        del read['readTime'][receiver]
                                    except:
                                        pass
                                    read['readPoint'][receiver] = msg_id
                                    read['readMember'][receiver] = ""
                                    read['readTime'][receiver] = readTime
                                    read['ROM'][receiver] = {}
                                    ririn.sendMessage(receiver,"sᴇᴛ ʀᴇᴀᴅɪɴɢ ᴘᴏɪɴᴛ : \n" + readTime)
                            elif cmd == "lurking off":
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if receiver not in read['readPoint']:
                                    ririn.sendMessage(receiver,"ʟᴜʀᴋɪɴɢ sᴇᴛ ᴏғғ")
                                else:
                                    try:
                                        del read['readPoint'][receiver]
                                        del read['readMember'][receiver]
                                        del read['readTime'][receiver]
                                    except:
                                        pass
                                    ririn.sendMessage(receiver,"ᴅᴇʟᴇᴛᴇ ʀᴇᴀᴅɪɴɢ ᴘᴏɪɴᴛ : \n" + readTime)
        
                            elif cmd == "lurking reset":
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if msg.to in read["readPoint"]:
                                    try:
                                        del read["readPoint"][msg.to]
                                        del read["readMember"][msg.to]
                                        del read["readTime"][msg.to]
                                        del read["ROM"][msg.to]
                                    except:
                                        pass
                                    read['readPoint'][receiver] = msg_id
                                    read['readMember'][receiver] = ""
                                    read['readTime'][receiver] = readTime
                                    read['ROM'][receiver] = {}
                                    ririn.sendMessage(msg.to, "ʀᴇsᴇᴛ ʀᴇᴀᴅɪɴɢ ᴘᴏɪɴᴛ : \n" + readTime)
                                else:
                                    ririn.sendMessage(msg.to, "ʟᴜʀᴋɪɴɢ ɴᴏᴛ ᴀᴋᴛɪᴠᴇ, ᴄᴏᴜʟᴅ ɴᴏᴛ ʙᴇ ʀᴇsᴇᴛ")
                                    
                            elif cmd == "lurking":
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if receiver in read['readPoint']:
                                    if read["ROM"][receiver].items() == []:
                                        ririn.sendMessage(receiver,"ɴᴏ sɪᴅᴇʀ")
                                    else:
                                        chiya = []
                                        for rom in read["ROM"][receiver].items():
                                            chiya.append(rom[1])
                                        cmem = ririn.getContacts(chiya) 
                                        zx = ""
                                        zxc = ""
                                        zx2 = []
                                        xpesan = '[ ʀ ᴇ ᴀ ᴅ ᴇ ʀ ]\n'
                                    for x in range(len(cmem)):
                                        xname = str(cmem[x].displayName)
                                        pesan = ''
                                        pesan2 = pesan+"@c\n"
                                        xlen = str(len(zxc)+len(xpesan))
                                        xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                        zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                        zx2.append(zx)
                                        zxc += pesan2
                                    text = xpesan+ zxc + "\n" + readTime
                                    try:
                                        ririn.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                    except Exception as error:
                                        print (error)
                                    pass
                                else:
                                    ririn.sendMessage(receiver,"ʟᴜʀᴋɪɴɢ ɴᴏᴛ ᴀᴄᴛɪᴠᴇ")
                            elif cmd.startswith("mimicadd"):
                            	if msg._from in admin:
                            		targets = []
                            		key = eval(msg.contentMetadata["MENTION"])
                            		key["MENTIONEES"][0]["M"]
                            		for x in key["MENTIONEES"]:
                                		targets.append(x["M"])
                            		for target in targets:
                                		try:
                                			wait["mimic"]["target"][target] = True
                                			ririn.sendMessage(msg.to,"ᴛᴀʀɢᴇᴛ ᴀᴅᴅᴇᴅ")
                                			break
                                		except:
                                			ririn.sendMessage(msg.to,"ғᴀɪʟᴇᴅ ᴀᴅᴅᴇᴅ ᴛᴀʀɢᴇᴛ")
                                			break
                                			
                            elif cmd.startswith("mimicdel"):
                            	if msg._from in admin:
                            		targets = []
                            		key = eval(msg.contentMetadata["MENTION"])
                            		key["MENTIONEES"][0]["M"]
                            		for x in key["MENTIONEES"]:
                                		targets.append(x["M"])
                            		for target in targets:
                                		try:
                                			del wait["mimic"]["target"][target]
                                			ririn.sendMessage(msg.to,"ᴛᴀɢᴇᴛ ᴅᴇʟᴇᴛᴇᴅ")
                                			break
                                		except:
                                			ririn.sendMessage(msg.to,"ғᴀɪʟ ᴅᴇʟᴇᴛᴇᴅ ᴛᴀʀɢᴇᴛ")
                                			break
                                    
                            elif cmd == "mimiclist":
                            	if msg._from in admin:
                            		if wait["mimic"]["target"] == {}:
                            			ririn.sendMessage(msg.to,"ɴᴏ ᴛᴀʀɢᴇᴛ")
                            		else:
                            			mc = "╔════[ ·✪·ᴍɪᴍɪᴄ ʟɪsᴛ·✪· ]════╗"
                            			for mi_d in wait["mimic"]["target"]:
                            				mc += "\n╠❂➣ "+ririn.getContact(mi_d).displayName
                            				mc += "\n╚═════[  ✯ ᴅɴᴀ ʙᴏᴛ ✯ ]═════╝"
                            			ririn.sendMessage(msg.to,mc)
                                
                            elif cmd.startswith("mimic"):
                            	if msg._from in admin:
                            		sep = text.split(" ")
                            		mic = text.replace(sep[0] + " ","")
                            		if mic == "on":
                            			if wait["mimic"]["status"] == False:
                            				wait["mimic"]["status"] = True
                            				ririn.sendMessage(msg.to,"ᴍɪᴍɪᴄ ᴏɴ")
                            		elif mic == "off":
                            			if wait["mimic"]["status"] == True:
                            				wait["mimic"]["status"] = False
                            				ririn.sendMessage(msg.to,"ᴍɪᴍɪᴄ ᴏғғ")
#------------------------------------============================------------------------------------#
#======================-----------✰ ᴅɴᴀ ʙᴏᴛ ✰-----------======================#
#------------------------------------============================------------------------------------#
                            elif cmd.startswith("checkwebsite"):
                                try:
                                    sep = text.split(" ")
                                    query = text.replace(sep[0] + " ","")
                                    r = requests.get("http://rahandiapi.herokuapp.com/sswebAPI?key=betakey&link={}".format(urllib.parse.quote(query)))
                                    data = r.text
                                    data = json.loads(data)
                                    ririn.sendImageWithURL(to, data["result"])
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("checkdate"):
                                try:
                                    sep = msg.text.split(" ")
                                    tanggal = msg.text.replace(sep[0] + " ","")
                                    r = requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                                    data=r.text
                                    data=json.loads(data)
                                    ret_ = "[ D A T E ]"
                                    ret_ += "\nDate Of Birth : {}".format(str(data["data"]["lahir"]))
                                    ret_ += "\nAge : {}".format(str(data["data"]["usia"]))
                                    ret_ += "\nBirthday : {}".format(str(data["data"]["ultah"]))
                                    ret_ += "\nZodiak : {}".format(str(data["data"]["zodiak"]))
                                    ririn.sendMessage(msg.to, str(ret_))
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("checkpraytime "):
                                separate = msg.text.split(" ")
                                location = msg.text.replace(separate[0] + " ","")
                                r = requests.get("http://api.corrykalam.net/apisholat.php?lokasi={}".format(location))
                                data = r.text
                                data = json.loads(data)
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                if data[1] != "sᴜʙᴜʜ : " and data[2] != "ᴅᴢᴜʜᴜʀ : " and data[3] != "ᴀsʜᴀʀ : " and data[4] != "ᴍᴀɢʜʀɪʙ : " and data[5] != "ɪsʜᴀ : ":
                                    ret_ = "╔═══[ ᴊᴀᴅᴡᴀʟ sʜᴏʟᴀᴛ ]"
                                    ret_ += "\n╠══[ sᴇᴋɪᴛᴀʀ " + data[0] + " ]"
                                    ret_ += "\n╠❂➣ ᴛᴀɴɢɢᴀʟ : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                    ret_ += "\n╠❂➣ ᴊᴀᴍ : " + datetime.strftime(timeNow,'%H:%M:%S')
                                    ret_ += "\n╠❂➣ " + data[1]
                                    ret_ += "\n╠❂➣ " + data[2]
                                    ret_ += "\n╠❂➣ " + data[3]
                                    ret_ += "\n╠❂➣ " + data[4]
                                    ret_ += "\n╠❂➣ " + data[5]
                                    ret_ += "\n╚════[ ✯ ᴅɴᴀ ʙᴏᴛ ✯ ]"
                                    ririn.sendMessage(msg.to, str(ret_))
                            elif cmd.startswith("checkweather "):
                                try:
                                    sep = text.split(" ")
                                    location = text.replace(sep[0] + " ","")
                                    r = requests.get("http://api.corrykalam.net/apicuaca.php?kota={}".format(location))
                                    data = r.text
                                    data = json.loads(data)
                                    tz = pytz.timezone("Asia/Makassar")
                                    timeNow = datetime.now(tz=tz)
                                    if "result" not in data:
                                        ret_ = "╔═══[ ᴡᴇᴀᴛʜᴇʀ sᴛᴀᴛᴜs ]"
                                        ret_ += "\n╠❂➣ ʟᴏᴄᴀᴛɪᴏɴ : " + data[0].replace("Temperatur di kota ","")
                                        ret_ += "\n╠❂➣ sᴜʜᴜ : " + data[1].replace("Suhu : ","") + "°ᴄ"
                                        ret_ += "\n╠❂➣ ᴋᴇʟᴇᴍʙᴀʙᴀɴ : " + data[2].replace("Kelembaban : ","") + "%"
                                        ret_ += "\n╠❂➣ ᴛᴇᴋᴀɴᴀɴ ᴜᴅᴀʀᴀ : " + data[3].replace("Tekanan udara : ","") + "ʜᴘᴀ "
                                        ret_ += "\n╠❂➣ ᴋᴇᴄᴇᴘᴀᴛᴀɴ ᴀɴɢɪɴ : " + data[4].replace("Kecepatan angin : ","") + "ᴍ/s"
                                        ret_ += "\n╠════[ ᴛɪᴍᴇ sᴛᴀᴛᴜs ]"
                                        ret_ += "\n╠❂➣ ᴛᴀɴɢɢᴀʟ : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                        ret_ += "\n╠❂➣ ᴊᴀᴍ : " + datetime.strftime(timeNow,'%H:%M:%S') + " ᴡɪʙ"
                                        ret_ += "\n╚════[ ✯ ᴅɴᴀ ʙᴏᴛ ✯ ]"
                                        ririn.sendMessage(msg.to, str(ret_))
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("checklocation "):
                                try:
                                    sep = text.split(" ")
                                    location = text.replace(sep[0] + " ","")
                                    r = requests.get("http://api.corrykalam.net/apiloc.php?lokasi={}".format(location))
                                    data = r.text
                                    data = json.loads(data)
                                    if data[0] != "" and data[1] != "" and data[2] != "":
                                        link = "https://www.google.co.id/maps/@{},{},15z".format(str(data[1]), str(data[2]))
                                        ret_ = "╔═══[ ʟᴏᴄᴀᴛɪᴏɴ sᴛᴀᴛᴜs ]"
                                        ret_ += "\n╠❂➣ ʟᴏᴄᴀᴛɪᴏɴ : " + data[0]
                                        ret_ += "\n╠❂➣  ɢᴏᴏɢʟᴇ ᴍᴀᴘs : " + link
                                        ret_ += "\n╚════[ ✯ ᴅɴᴀ ʙᴏᴛ ✯ ]"
                                        ririn.sendMessage(msg.to, str(ret_))
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("instainfo"):
                                try:
                                    sep = text.split(" ")
                                    search = text.replace(sep[0] + " ","")
                                    r = requests.get("https://www.instagram.com/{}/?__a=1".format(search))
                                    data = r.text
                                    data = json.loads(data)
                                    if data != []:
                                        ret_ = "╔══[ Profile Instagram ]"
                                        ret_ += "\n╠ Nama : {}".format(str(data["graphql"]["user"]["full_name"]))
                                        ret_ += "\n╠ Username : {}".format(str(data["graphql"]["user"]["username"]))
                                        ret_ += "\n╠ Bio : {}".format(str(data["graphql"]["user"]["biography"]))
                                        ret_ += "\n╠ Pengikut : {}".format(str(data["graphql"]["user"]["edge_followed_by"]["count"]))
                                        ret_ += "\n╠ Diikuti : {}".format(str(data["graphql"]["user"]["edge_follow"]["count"]))
                                        if data["graphql"]["user"]["is_verified"] == True:
                                            ret_ += "\n╠ Verifikasi : Sudah"
                                        else:
                                            ret_ += "\n╠ Verifikasi : Belum"
                                        if data["graphql"]["user"]["is_private"] == True:
                                            ret_ += "\n╠ Akun Pribadi : Iya"
                                        else:
                                            ret_ += "\n╠ Akun Pribadi : Tidak"
                                        ret_ += "\n╠ Total Post : {}".format(str(data["graphql"]["user"]["edge_owner_to_timeline_media"]["count"]))
                                        ret_ += "\n╚══[ https://www.instagram.com/{} ]".format(search)
                                        path = data["graphql"]["user"]["profile_pic_url_hd"]
                                        ririn.sendImageWithURL(to, str(path))
                                        ririn.sendMessage(msg.to, str(ret_))
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("instapost"):
                                try:
                                    sep = text.split(" ")
                                    text = text.replace(sep[0] + " ","")   
                                    cond = text.split("|")
                                    username = cond[0]
                                    no = cond[1] 
                                    r = requests.get("http://rahandiapi.herokuapp.com/instapost/{}/{}?key=betakey".format(str(username), str(no)))
                                    data = r.text
                                    data = json.loads(data)
                                    if data["find"] == True:
                                        if data["media"]["mediatype"] == 1:
                                            ririn.sendImageWithURL(msg.to, str(data["media"]["url"]))
                                        if data["media"]["mediatype"] == 2:
                                            ririn.sendVideoWithURL(msg.to, str(data["media"]["url"]))
                                        ret_ = "╔══[ Info Post ]"
                                        ret_ += "\n╠ Jumlah Like : {}".format(str(data["media"]["like_count"]))
                                        ret_ += "\n╠ Jumlah Comment : {}".format(str(data["media"]["comment_count"]))
                                        ret_ += "\n╚══[ Caption ]\n{}".format(str(data["media"]["caption"]))
                                        ririn.sendMessage(msg.to, str(ret_))
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("instastory"):
                                try:
                                    sep = text.split(" ")
                                    text = text.replace(sep[0] + " ","")
                                    cond = text.split("|")
                                    search = str(cond[0])
                                    if len(cond) == 2:
                                        r = requests.get("http://rahandiapi.herokuapp.com/instastory/{}?key=betakey".format(search))
                                        data = r.text
                                        data = json.loads(data)
                                        if data["url"] != []:
                                            num = int(cond[1])
                                            if num <= len(data["url"]):
                                                search = data["url"][num - 1]
                                                if search["tipe"] == 1:
                                                    ririn.sendImageWithURL(to, str(search["link"]))
                                                if search["tipe"] == 2:
                                                    ririn.sendVideoWithURL(to, str(search["link"]))
                                except Exception as error:
                                    logError(error)
                                    
                            elif cmd.startswith("say-"):
                                sep = text.split("-")
                                sep = sep[1].split(" ")
                                lang = sep[0]
                                say = text.replace("say-" + lang + " ","")
                                if lang not in list_language["list_textToSpeech"]:
                                    return ririn.sendMessage(msg.to, "ʟᴀɴɢᴜᴀɢᴇ ɴᴏᴛ ғᴏᴜɴᴅ")
                                tts = gTTS(text=say, lang=lang)
                                tts.save("hasil.mp3")
                                ririn.sendAudio(to,"hasil.mp3")
                                
                            elif cmd.startswith("searchimage"):
                                try:
                                    separate = msg.text.split(" ")
                                    search = msg.text.replace(separate[0] + " ","")
                                    r = requests.get("http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(search))
                                    data = r.text
                                    data = json.loads(data)
                                    if data["result"] != []:
                                        items = data["result"]
                                        path = random.choice(items)
                                        a = items.index(path)
                                        b = len(items)
                                        ririn.sendImageWithURL(to, str(path))
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("searchmusic "):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split("|")
                                search = str(cond[0])
                                result = requests.get("http://api.ntcorp.us/joox/search?q={}".format(str(search)))
                                data = result.text
                                data = json.loads(data)
                                if len(cond) == 1:
                                    num = 0
                                    ret_ = "╔══[ ʀᴇsᴜʟᴛ ᴍᴜsɪᴄ ]"
                                    for music in data["result"]:
                                        num += 1
                                        ret_ += "\n╠ {}. {}".format(str(num), str(music["single"]))
                                    ret_ += "\n╚══[ ᴛᴏᴛᴀʟ {} ᴍᴜsɪᴄ ] ".format(str(len(data["result"])))
                                    ret_ += "\n\nᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ ᴅᴇᴛᴀɪʟs ᴍᴜsɪᴄ, sɪʟᴀʜᴋᴀɴ ɢᴜɴᴀᴋᴀɴ ᴄᴏᴍᴍᴀɴᴅ {}sᴇᴀʀᴄʜᴍᴜsɪᴄ {}|「ɴᴜᴍʙᴇʀ」".format(str(setKey), str(search))
                                    ririn.sendMessage(msg.to, str(ret_))
                                elif len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(data["result"]):
                                        music = data["result"][num - 1]
                                        result = requests.get("http://api.ntcorp.us/joox/song_info?sid={}".format(str(music["sid"])))
                                        data = result.text
                                        data = json.loads(data)
                                        if data["result"] != []:
                                            ret_ = "╔══════[ ᴍᴜsɪᴄ ]"
                                            ret_ += "\n╠❂➣ ᴛɪᴛʟᴇ : {}".format(str(data["result"]["song"]))
                                            ret_ += "\n╠❂➣ ᴀʟʙᴜᴍ : {}".format(str(data["result"]["album"]))
                                            ret_ += "\n╠❂➣ sɪᴢᴇ : {}".format(str(data["result"]["size"]))
                                            ret_ += "\n╠❂➣ ʟɪɴᴋ :  {}".format(str(data["result"]["mp3"][0]))
                                            ret_ += "\n╚════[ ✯ ᴅɴᴀ ʙᴏᴛ ✯ ]"
                                            ririn.sendImageWithURL(to, str(data["result"]["img"]))
                                            ririn.sendMessage(msg.to, str(ret_))
                                            ririn.sendAudioWithURL(to, str(data["result"]["mp3"][0]))
                            elif cmd.startswith("searchlyric"):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split("|")
                                search = cond[0]
                                api = requests.get("http://api.secold.com/joox/cari/{}".format(str(search)))
                                data = api.text
                                data = json.loads(data)
                                if len(cond) == 1:
                                    num = 0
                                    ret_ = "╔══[ ʀᴇsᴜʟᴛ ʟʏʀɪᴄ ]"
                                    for lyric in data["results"]:
                                        num += 1
                                        ret_ += "\n╠❂➣ {}. {}".format(str(num), str(lyric["single"]))
                                    ret_ += "\n╚══[ ᴛᴏᴛᴀʟ {} ᴍᴜsɪᴄ ]".format(str(len(data["results"])))
                                    ret_ += "\n\nᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ ᴅᴇᴛᴀɪʟs ʟʏʀɪᴄ, sɪʟᴀʜᴋᴀɴ ɢᴜɴᴀᴋᴀɴ ᴄᴏᴍᴍᴀɴᴅ {}sᴇᴀʀᴄʜʟʏʀɪᴄ {}|「ɴᴜᴍʙᴇʀ」".format(str(setKey), str(search))
                                    ririn.sendMessage(msg.to, str(ret_))
                                elif len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(data["results"]):
                                        lyric = data["results"][num - 1]
                                        api = requests.get("http://api.secold.com/joox/sid/{}".format(str(lyric["songid"])))
                                        data = api.text
                                        data = json.loads(data)
                                        lyrics = data["results"]["lyric"]
                                        lyric = lyrics.replace('ti:','Title - ')
                                        lyric = lyric.replace('ar:','Artist - ')
                                        lyric = lyric.replace('al:','Album - ')
                                        removeString = "[1234567890.:]"
                                        for char in removeString:
                                            lyric = lyric.replace(char,'')
                                        ririn.sendMessage(msg.to, str(lyric))
                            elif cmd.startswith("searchyoutube"):
                                sep = text.split(" ")
                                search = text.replace(sep[0] + " ","")
                                params = {"search_query": search}
                                r = requests.get("https://www.youtube.com/results", params = params)
                                soup = BeautifulSoup(r.content, "html5lib")
                                ret_ = "╔══[ ʀᴇsᴜʟᴛ ʏᴏᴜᴛᴜʙᴇ ]"
                                datas = []
                                for data in soup.select(".yt-lockup-title > a[title]"):
                                    if "&lists" not in data["href"]:
                                        datas.append(data)
                                for data in datas:
                                    ret_ += "\n╠❂➣{} ]".format(str(data["title"]))
                                    ret_ += "\n╠❂ https://www.youtube.com{}".format(str(data["href"]))
                                ret_ += "\n╚══[ ᴛᴏᴛᴀʟ {} ᴠɪᴅᴇᴏ ]".format(len(datas))
                                ririn.sendMessage(msg.to, str(ret_))
                            elif cmd.startswith("tr-"):
                                sep = text.split("-")
                                sep = sep[1].split(" ")
                                lang = sep[0]
                                say = text.replace("tr-" + lang + " ","")
                                if lang not in list_language["list_translate"]:
                                    return ririn.sendMessage(msg.to, "Language not found")
                                translator = Translator()
                                hasil = translator.translate(say, dest=lang)
                                A = hasil.text
                                ririn.sendMessage(msg.to, str(A))
#------------------------------------============================------------------------------------#
#======================-----------✰ ᴅɴᴀ ʙᴏᴛ ✰-----------======================#
#------------------------------------============================------------------------------------#
                        if text.lower() == "mykey":
                        	if msg._from in admin:
                        		ririn.sendMessage(msg.to, "ᴋᴇʏᴄᴏᴍᴍᴀɴᴅ sᴀᴀᴛ ɪɴɪ [ {} ]".format(str(wait["keyCommand"])))
                        elif text.lower() == "setkey on":
                        	if msg._from in admin:
                        		wait["setKey"] = True
                        		ririn.sendMessage(msg.to, "ʙᴇʀʜᴀsɪʟ ᴍᴇɴɢᴀᴋᴛɪғᴋᴀɴ sᴇᴛᴋᴇʏ")
                        elif text.lower() == "setkey off":
                        	if msg._from in admin:
                        		wait["setKey"] = False
                        		ririn.sendMessage(msg.to, "ʙᴇʀʜᴀsɪʟ ᴍᴇɴᴏɴᴀᴋᴛɪғᴋᴀɴ sᴇᴛᴋᴇʏ")
#------------------------------------============================------------------------------------#
#======================-----------✰ ᴅɴᴀ ʙᴏᴛ ✰-----------======================#
#------------------------------------============================------------------------------------#
                    elif msg.contentType == 1:
                        if wait["changePictureProfile"] == True:
                            path = ririn.downloadObjectMsg(msg_id)
                            wait["changePictureProfile"] = False
                            ririn.updateProfilePicture(path)
                            ririn.sendMessage(msg.to, "sᴜᴄᴄᴇs ᴄʜᴀɴɢᴇ ᴘʜᴏᴛᴏ ᴘʀᴏғɪʟᴇ")
                        if msg.toType == 2:
                            if to in wait["changeGroupPicture"]:
                                path = ririn.downloadObjectMsg(msg_id)
                                wait["changeGroupPicture"].remove(to)
                                ririn.updateGroupPicture(to, path)
                                ririn.sendMessage(msg.to, "sᴜᴄᴄᴇs ᴄʜᴀɴɢᴇ ᴘʜᴏᴛᴏ ɢʀᴏᴜᴘ")
                    elif msg.contentType == 7:
                        if wait["checkSticker"] == True:
                            stk_id = msg.contentMetadata['STKID']
                            stk_ver = msg.contentMetadata['STKVER']
                            pkg_id = msg.contentMetadata['STKPKGID']
                            ret_ = "╔════[ sᴛɪᴄᴋᴇʀ ɪɴғᴏ ] "
                            ret_ += "\n╠❂➣ sᴛɪᴄᴋᴇʀ ɪᴅ : {}".format(stk_id)
                            ret_ += "\n╠❂➣ sᴛɪᴄᴋᴇʀ ᴘᴀᴄᴋᴀɢᴇs ɪᴅ : {}".format(pkg_id)
                            ret_ += "\n╠❂➣ sᴛɪᴄᴋᴇʀ ᴠᴇʀsɪᴏɴ : {}".format(stk_ver)
                            ret_ += "\n╠❂➣ sᴛɪᴄᴋᴇʀ ᴜʀʟ : line://shop/detail/{}".format(pkg_id)
                            ret_ += "\n╚════[ ✯ ᴅɴᴀ ʙᴏᴛ ✯ ]"
                            ririn.sendMessage(msg.to, str(ret_))
                    elif msg.contentType == 13:
                        if wait["checkContact"] == True:
                            try:
                                contact = ririn.getContact(msg.contentMetadata["mid"])
                                if ririn != None:
                                    cover = ririn.getProfileCoverURL(msg.contentMetadata["mid"])
                                else:
                                    cover = "Tidak dapat masuk di line channel"
                                path = "http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                                try:
                                    ririn.sendImageWithURL(to, str(path))
                                except:
                                    pass
                                ret_ = "╔═══[ ᴅᴇᴛᴀɪʟs ᴄᴏɴᴛᴀᴄᴛ ]"
                                ret_ += "\n╠❂➣ ɴᴀᴍᴀ : {}".format(str(contact.displayName))
                                ret_ += "\n╠❂➣ ᴍɪᴅ : {}".format(str(msg.contentMetadata["mid"]))
                                ret_ += "\n╠❂➣ ʙɪᴏ : {}".format(str(contact.statusMessage))
                                ret_ += "\n╠❂➣ ɢᴀᴍʙᴀʀ ᴘʀᴏғɪʟᴇ : http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                                ret_ += "\n╠❂➣ ɢᴀᴍʙᴀʀ ᴄᴏᴠᴇʀ : {}".format(str(cover))
                                ret_ += "\n╚════[ ✯ ᴅɴᴀ ʙᴏᴛ ✯ ]"
                                ririn.sendMessage(msg.to, str(ret_))
                            except:
                                ririn.sendMessage(msg.to, "ᴋᴏɴᴛᴀᴋ ᴛɪᴅᴀᴋ ᴠᴀʟɪᴅ")
                    elif msg.contentType == 16:
                        if wait["checkPost"] == True:
                            try:
                                ret_ = "╔════[ ᴅᴇᴛᴀɪʟs ᴘᴏsᴛ ]"
                                if msg.contentMetadata["serviceType"] == "GB":
                                    contact = ririn.getContact(sender)
                                    auth = "\n╠❂➣ ᴀᴜᴛʜᴏʀ : {}".format(str(contact.displayName))
                                else:
                                    auth = "\n╠❂➣ ᴀᴜᴛʜᴏʀ : {}".format(str(msg.contentMetadata["serviceName"]))
                                purl = "\n╠❂➣ ᴜʀʟ : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                                ret_ += auth
                                ret_ += purl
                                if "mediaOid" in msg.contentMetadata:
                                    object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                    if msg.contentMetadata["mediaType"] == "V":
                                        if msg.contentMetadata["serviceType"] == "GB":
                                            ourl = "\n╠❂➣ ᴏʙᴊᴇᴄᴛ ᴜʀʟ : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                            murl = "\n╠❂➣ ᴍᴇᴅɪᴀ ᴜʀʟ : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                        else:
                                            ourl = "\n╠❂➣ ᴏʙᴊᴇᴄᴛ ᴜʀʟ : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                            murl = "\n╠❂➣ ᴍᴇᴅɪᴀ ᴜʀʟ : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                        ret_ += murl
                                    else:
                                        if msg.contentMetadata["serviceType"] == "GB":
                                            ourl = "\n╠❂➣ ᴏʙᴊᴇᴄᴛ ᴜʀʟ : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                        else:
                                            ourl = "\n╠❂➣ ᴏʙᴊᴇᴄᴛ ᴜʀʟ : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                    ret_ += ourl
                                if "stickerId" in msg.contentMetadata:
                                    stck = "\n╠❂➣ sᴛɪᴄᴋᴇʀ : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                    ret_ += stck
                                if "text" in msg.contentMetadata:
                                    text = "\n╠❂➣ ɴᴏᴛᴇ : {}".format(str(msg.contentMetadata["text"]))
                                    ret_ += text
                                ret_ += "\n╚════[ ✯ ᴅɴᴀ ʙᴏᴛ ✯ ]"
                                ririn.sendMessage(msg.to, str(ret_))
                            except:
                                ririn.sendMessage(msg.to, "ɪɴᴠᴀʟɪᴅ ᴘᴏsᴛ")
            except Exception as error:
                logError(error)
                traceback.print_tb(error.__traceback__)
                
        if op.type == 26:
            msg = op.message
            if wait["autoResponPc"] == True:
                if msg.toType == 0:
                    ririn.sendChatChecked(msg._from,msg.id)
                    contact = ririn.getContact(msg._from)
                    cName = contact.displayName
                    balas = ["╔════════════════════╗\n                   「ᴀᴜᴛᴏ ʀᴇᴘʟʏ」\n                             ʙʏ:\n                    ✰ ᴅɴᴀ ʙᴏᴛ ✰\n╚════════════════════╝\n\nʜᴀʟʟᴏ 「" + cName + "」\nᴍᴏʜᴏɴ ᴍᴀᴀғ sᴀʏᴀ sᴇᴅᴀɴɢ sɪʙᴜᴋ, ɪɴɪ ᴀᴅᴀʟᴀʜ ᴘᴇsᴀɴ ᴏᴛᴏᴍᴀᴛɪs, ᴊɪᴋᴀ ᴀᴅᴀ ʏᴀɴɢ ᴘᴇɴᴛɪɴɢ ᴍᴏʜᴏɴ ʜᴜʙᴜɴɢɪ sᴀʏᴀ ɴᴀɴᴛɪ, ᴛᴇʀɪᴍᴀᴋᴀsɪʜ...","╔════════════════════╗\n                   「ᴀᴜᴛᴏ ʀᴇᴘʟʏ」\n                             ʙʏ:\n                    ✰ ᴅɴᴀ ʙᴏᴛ ✰\n╚════════════════════╝\n\nʜᴀʟʟᴏ 「" + cName + "」\nsᴀʏᴀ ʟᴀɢɪ sɪʙᴜᴋ ʏᴀ ᴋᴀᴋ ᴊᴀɴɢᴀɴ ᴅɪɢᴀɴɢɢᴜ","╔════════════════════╗\n                   「ᴀᴜᴛᴏ ʀᴇᴘʟʏ」\n                             ʙʏ:\n                    ✰ ᴅɴᴀ ʙᴏᴛ ✰\n╚════════════════════╝\n\nʜᴀʟʟᴏ 「" + cName + "」\nsᴀʏᴀ sᴇᴅᴀɴɢ ᴛɪᴅᴜʀ ᴋᴀᴋ"]
                    dee = "" + random.choice(balas)
                    ririn.sendImageWithURL(msg._from, "http://dl.profile.line-cdn.net{}".format(contact.picturePath))
                    ririn.sendMessage(msg._from,dee)
                    
        if op.type == 26:
            msg = op.message
            if wait["removechat"] == True:
            	try:
            		print ("[ 26 ] Remove Chat")
            		if msg.toType == 0:
            			ririn.removeAllMessages(op.param2)
            			dna1.removeAllMessages(op.param2)
            			dna2.removeAllMessages(op.param2)
            			dna3.removeAllMessages(op.param2)
            			dna4.removeAllMessages(op.param2)
            			dna5.removeAllMessages(op.param2)
            			dna6.removeAllMessages(op.param2)
            			dna7.removeAllMessages(op.param2)
            			dna8.removeAllMessages(op.param2)
            			dna9.removeAllMessages(op.param2)
            			ririn.sendMessage(msg.to, "sᴜᴄᴄᴇs")
            		else:
            			ririn.removeAllMessages(op.param2)
            			dna1.removeAllMessages(op.param2)
            			dna2.removeAllMessages(op.param2)
            			dna3.removeAllMessages(op.param2)
            			dna4.removeAllMessages(op.param2)
            			dna5.removeAllMessages(op.param2)
            			dna6.removeAllMessages(op.param2)
            			dna7.removeAllMessages(op.param2)
            			dna8.removeAllMessages(op.param2)
            			dna9.removeAllMessages(op.param2)
            			ririn.sendMessage(msg.to, "sᴜᴄᴄᴇs")
            	except Exception as error:
            		logError(error)
            		ririn.sendMessage(msg.to, "ᴇʀʀᴏʀ")
            		print ("[ 26 ] ERROR")
                
        if op.type == 26:
            try:
                print ("[ 26 ] RECIEVE MESSAGE")
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                        if sender != ririn.profile.mid:
                            to = sender
                        else:
                            to = receiver
                    elif msg.toType == 1:
                        to = receiver
                    elif msg.toType == 2:
                        to = receiver
                    if wait["autoRead"] == True:
                        ririn.sendChatChecked(to, msg_id)
                    if to in read["readPoint"]:
                        if sender not in read["ROM"][to]:
                            read["ROM"][to][sender] = True
                    if sender in wait["mimic"]["target"] and wait["mimic"]["status"] == True and wait["mimic"]["target"][sender] == True:
                        text = msg.text
                        if text is not None:
                            ririn.sendMessage(msg.to,text)
                    if wait["unsendMessage"] == True:
                        try:
                            msg = op.message
                            if msg.toType == 0:
                                ririn.log("[{} : {}]".format(str(msg._from), str(msg.text)))
                            else:
                                ririn.log("[{} : {}]".format(str(msg.to), str(msg.text)))
                                msg_dict[msg.id] = {"text": msg.text, "from": msg._from, "createdTime": msg.createdTime, "contentType": msg.contentType, "contentMetadata": msg.contentMetadata}
                        except Exception as error:
                            logError(error)
                    if msg.contentType == 0:
                        if text is None:
                            return
                        if "/ti/g/" in msg.text.lower():
                            if wait["autoJoinTicket"] == True:
                                link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                links = link_re.findall(text)
                                n_links = []
                                for l in links:
                                    if l not in n_links:
                                        n_links.append(l)
                                for ticket_id in n_links:
                                    group = ririn.findGroupByTicket(ticket_id)
                                    ririn.acceptGroupInvitationByTicket(group.id,ticket_id)
                                    ririn.sendMessage(msg.to, "sᴜᴄᴄᴇssғᴜʟʟʏ ᴇɴᴛᴇʀᴇᴅ ᴛʜᴇ ɢʀᴏᴜᴘ %s" % str(group.name))
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if ririnMid in mention["M"]:
                                    if wait["autoRespon"] == True:
                                    	ririn.sendChatChecked(msg._from,msg.id)
                                    	contact = ririn.getContact(msg._from)
                                    	ririn.sendImageWithURL(msg._from, "http://dl.profile.line-cdn.net{}".format(contact.picturePath))
                                    	sendMention(sender, "ᴏɪ ᴍʙʟᴏ @!      ,\nɴɢᴀᴘᴀɪɴ ᴛᴀɢ ᴛᴀɢ ɢᴡ", [sender])
                                    break
            except Exception as error:
                logError(error)
                traceback.print_tb(error.__traceback__)
                
        if op.type == 65:
            print ("[ 65 ] NOTIFIED DESTROY MESSAGE")
            if wait["unsendMessage"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                            contact = ririn.getContact(msg_dict[msg_id]["from"])
                            if contact.displayNameOverridden != None:
                                name_ = contact.displayNameOverridden
                            else:
                                name_ = contact.displayName
                                ret_ = "sᴇɴᴅ ᴍᴇssᴀɢᴇ ᴄᴀɴᴄᴇʟʟᴇᴅ."
                                ret_ += "\nsᴇɴᴅᴇʀ : @!      "
                                ret_ += "\nsᴇɴᴅ ᴀᴛ : {}".format(str(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"]))))
                                ret_ += "\nᴛʏᴘᴇ : {}".format(str(Type._VALUES_TO_NAMES[msg_dict[msg_id]["contentType"]]))
                                ret_ += "\nᴛᴇxᴛ : {}".format(str(msg_dict[msg_id]["text"]))
                                sendMention(at, str(ret_), [contact.mid])
                            del msg_dict[msg_id]
                        else:
                            ririn.sendMessage(at,"sᴇɴᴛᴍᴇssᴀɢᴇ ᴄᴀɴᴄᴇʟʟᴇᴅ,ʙᴜᴛ ɪ ᴅɪᴅɴ'ᴛ ʜᴀᴠᴇ ʟᴏɢ ᴅᴀᴛᴀ.\nsᴏʀʀʏ > <")
                except Exception as error:
                    logError(error)
                    traceback.print_tb(error.__traceback__)
                    
        if op.type == 55:
        	try:
        		group_id = op.param1
        		user_id=op.param2
        		subprocess.Popen('echo "'+ user_id+'|'+str(op.createdTime)+'" >> dataSeen/%s.txt' % group_id, shell=True, stdout=subprocess.PIPE, )
        	except Exception as e:
        		print(e)
	      
        if op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = ririn.getContact(op.param2).displayName
                            dan = ririn.getContact(op.param2)
                            tgb = ririn.getGroup(op.param1)
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n• " + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        sendMention(op.param1, "ᴡᴏʏ ☞ @!       ☜\nᴅɪ {} ᴋᴏᴋ ᴅɪᴇᴍ ᴅɪᴇᴍ ʙᴀᴇ...\nsɪɴɪ ɪᴋᴜᴛ ɴɢᴏᴘɪ".format(str(tgb.name)),[op.param2])
                                        ririn.sendContact(op.param1, op.param2)
                                        ririn.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath))
                                    else:
                                        sendMention(op.param1, "ᴍʙʟᴏ ☞ @!       ☜\nɴɢɪɴᴛɪᴘ ᴅᴏᴀɴɢ ʟᴜ ᴅɪ {} \nsɪɴɪ ɢᴀʙᴜɴɢ ᴍᴀ ᴋɪᴛᴀ".format(str(tgb.name)),[op.param2])
                                        ririn.sendContact(op.param1, op.param2)
                                        ririn.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath))
                                else:
                                    sendMention(op.param1, "ʜɪʟɪʜ ☞ @!       ☜\nɴɢᴀᴘᴀɪɴ ʟᴜ...\nɢᴀʙᴜɴɢ ᴄʜᴀᴛ sɪɴɪ ᴅɪ {} ".format(str(tgb.name)),[op.param2])
                                    ririn.sendContact(op.param1, op.param2)
                                    ririn.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath))
                        else:
                            pass
                    else:
                        pass
                except:
                    pass

        else:
            pass
                
        if op.type == 55:
            print ("[ 55 ] NOTIFIED READ MESSAGE")
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                else:
                   pass
            except Exception as error:
                logError(error)
                traceback.print_tb(error.__traceback__)
    except Exception as error:
        logError(error)
        traceback.print_tb(error.__traceback__)

while True:
    try:
        delete_log()
        ops = ririnPoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                ririnBot(op)
                ririnPoll.setRevision(op.revision)
    except Exception as error:
        logError(error)
        
def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")
atexit.register(atend)
