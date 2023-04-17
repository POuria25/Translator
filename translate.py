from encodings.utf_8_sig import encode
from googletrans import Translator
import time
import math

LANGUAGES = {'af': 'afrikaans', 'sq': 'albanian', 'am': 'amharic', 'ar': 'arabic', 'hy': 'armenian', 'az': 'azerbaijani', 'eu': 
'basque', 'be': 'belarusian', 'bn': 'bengali', 'bs': 'bosnian', 'bg': 'bulgarian', 'ca': 'catalan', 'ceb': 'cebuano', 'ny': 'chichewa', 
'zh-cn': 'chinese (simplified)', 'zh-tw': 'chinese (traditional)', 'co': 'corsican', 'hr': 'croatian', 'cs': 'czech', 'da': 'danish', 
'nl': 'dutch', 'en': 'english', 'eo': 'esperanto', 'et': 'estonian', 'tl': 'filipino', 'fi': 'finnish', 'fr': 'french', 'fy': 'frisian', 
'gl': 'galician', 'ka': 'georgian', 'de': 'german', 'el': 'greek', 'gu': 'gujarati', 'ht': 'haitian creole', 'ha': 'hausa', 'haw': 'hawaiian',
'iw': 'hebrew', 'he': 'hebrew', 'hi': 'hindi', 'hmn': 'hmong', 'hu': 'hungarian', 'is': 'icelandic', 'ig': 'igbo', 'id': 
'indonesian', 'ga': 'irish', 'it': 'italian', 'ja': 'japanese', 'jw': 'javanese', 'kn': 'kannada', 'kk': 'kazakh', 'km': 'khmer', 
'ko': 'korean', 'ku': 'kurdish (kurmanji)', 'ky': 'kyrgyz', 'lo': 'lao', 'la': 'latin', 'lv': 'latvian', 'lt': 'lithuanian', 'lb': 'luxembourgish', 
'mk': 'macedonian', 'mg': 'malagasy', 'ms': 'malay', 'ml': 'malayalam', 'mt': 'maltese', 'mi': 'maori', 'mr': 'marathi', 'mn': 'mongolian', 
'my': 'myanmar (burmese)', 'ne': 'nepali', 'no': 'norwegian', 'or': 'odia', 'ps': 'pashto', 'fa': 'persian', 'pl': 'polish', 'pt': 
'portuguese', 'pa': 'punjabi', 'ro': 'romanian', 'ru': 'russian', 'sm': 'samoan', 'gd': 'scots gaelic', 'sr': 'serbian', 'st': 'sesotho', 
'sn': 'shona', 'sd': 'sindhi', 'si': 'sinhala', 'sk': 'slovak', 'sl': 'slovenian', 'so': 'somali', 'es': 'spanish', 'su': 'sundanese', 
'sw': 'swahili', 'sv': 'swedish', 'tg': 'tajik', 'ta': 'tamil', 'te': 'telugu', 'th': 'thai', 'tr': 'turkish', 
'uk': 'ukrainian', 'ur': 'urdu', 'ug': 'uyghur', 'uz': 'uzbek', 'vi': 'vietnamese', 'cy': 'welsh', 'xh': 'xhosa', 'yi': 'yiddish', 'yo': 
'yoruba', 'zu': 'zulu'}


def translator(text, fromLang, toLang):

    translator = Translator()

    return translator.translate(text, src=fromLang, dest=toLang ).text

def readFile(fileName):
    try:
        with open(fileName) as opfr:
            content = opfr.readlines()
    finally:
        opfr.close()
    
    return content          

def display(fileName, fromLang, toLang):
    
    text = readFile(fileName)    
    print(text[0])
    print(text[1])

    for i in range(2,len(text)):

        print([i],". ",text[i])
        print("                             ",translator(text[i], fromLang, toLang))
        print("\n")

def writeFile(fileName, fromLang, toLang):

    start = time.time()

    try:
        opfw = open(LANGUAGES[fromLang].capitalize+" vocabularies translated to french & "+LANGUAGES[toLang].capitalize+".txt", "w")
        text = readFile(fileName)
        
        print(text[0], end='      ', file = opfw)
        print(text[1],"(translated in", LANGUAGES[toLang] ,")", end='      ', file = opfw)
        print("\n", file=opfw)

        if(toLang == 'fa'):
            for i in range(2,len(text)): 
                str = "" 
                for word in text[i].split():
                    if "." not in word:
                        str += word + " "
                    else:
                        break 

                print([i-1],". ",text[i], end='      ', file = opfw)
                print("        ",translator(str, fromLang, toLang),    "                      ",file = opfw)
                print("                      ",translator(str, fromLang, "de"),file = opfw)
                print("\n", file=opfw)       
        else:
            for i in range(2,len(text)): 
                           
                print([i-1],". ",text[i], end='      ', file = opfw)
                print("        ",translator(text[i], fromLang, toLang),"                      ",translator(text[i], fromLang, "de"),file = opfw)
                print("        ",translator(text[i], fromLang, "de"),file = opfw)
                print("\n", file=opfw)
            
    finally:
        opfw.close()
    # record end time
    end = time.time()
    tmp = ((end-start)/60)
    sec, minute = math.modf(tmp)
    print("The excution time is",minute,'m  :',"{:.2f}".format(sec*10), 's ')       


fileName = input("Enter the file name to read : \n")
fromLang = input("Source language : ") 
toLang = input("Target language : ")

writeFile(fileName, fromLang, toLang)



