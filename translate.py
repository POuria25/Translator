# Import necessary libraries
from encodings.utf_8_sig import encode
from queue import Empty
from googletrans import Translator
import time
import math


POuria = """
 *******    *******                  **             **   **             **                           **
/**////**  **/////**                //             /**  **             /**                          ///
/**   /** **     //** **   ** ****** **  ******    /** **    ******   ******  ******  **   ** ****** **  ******   *******
/******* /**      /**/**  /**//**//*/** //////**   /****    //////** ///**/  **////**/**  /**////** /** //////** //**///**
/**////  /**      /**/**  /** /** / /**  *******   /**/**    *******   /**  /**   /**/**  /**   **  /**  *******  /**  /**
/**      //**     ** /**  /** /**   /** **////**   /**//**  **////**   /**  /**   /**/**  /**  **   /** **////**  /**  /**
/**       //*******  //******/***   /**//********  /** //**//********  //** //****** //****** ******/**//******** ***  /**
//         ///////    ////// ///    //  ////////   //   //  ////////    //   //////   ////// ////// //  //////// ///   //
"""


# Define a dictionary of languages
LANGUAGES = {
    'af': 'afrikaans', 'sq': 'albanian', 'am': 'amharic', 'ar': 'arabic', 'hy': 'armenian', 'az': 'azerbaijani', 'eu': 'basque',
    'be': 'belarusian', 'bn': 'bengali', 'bs': 'bosnian', 'bg': 'bulgarian', 'ca': 'catalan', 'ceb': 'cebuano', 'ny': 'chichewa',
    'zh-cn': 'chinese (simplified)', 'zh-tw': 'chinese (traditional)', 'co': 'corsican', 'hr': 'croatian', 'cs': 'czech', 'da': 'danish',
    'nl': 'dutch', 'en': 'english', 'eo': 'esperanto', 'et': 'estonian', 'tl': 'filipino', 'fi': 'finnish', 'fr': 'french', 'fy': 'frisian',
    'gl': 'galician', 'ka': 'georgian', 'de': 'german', 'el': 'greek', 'gu': 'gujarati', 'ht': 'haitian creole', 'ha': 'hausa', 'haw': 'hawaiian',
    'iw': 'hebrew', 'he': 'hebrew', 'hi': 'hindi', 'hmn': 'hmong', 'hu': 'hungarian', 'is': 'icelandic', 'ig': 'igbo', 'id': 'indonesian',
    'ga': 'irish', 'it': 'italian', 'ja': 'japanese', 'jw': 'javanese', 'kn': 'kannada', 'kk': 'kazakh', 'km': 'khmer',
    'ko': 'korean', 'ku': 'kurdish (kurmanji)', 'ky': 'kyrgyz', 'lo': 'lao', 'la': 'latin', 'lv': 'latvian', 'lt': 'lithuanian', 'lb': 'luxembourgish',
    'mk': 'macedonian', 'mg': 'malagasy', 'ms': 'malay', 'ml': 'malayalam', 'mt': 'maltese', 'mi': 'maori', 'mr': 'marathi', 'mn': 'mongolian',
    'my': 'myanmar (burmese)', 'ne': 'nepali', 'no': 'norwegian', 'or': 'odia', 'ps': 'pashto', 'fa': 'persian', 'pl': 'polish', 'pt':
    'portuguese', 'pa': 'punjabi', 'ro': 'romanian', 'ru': 'russian', 'sm': 'samoan', 'gd': 'scots gaelic', 'sr': 'serbian', 'st': 'sesotho',
    'sn': 'shona', 'sd': 'sindhi', 'si': 'sinhala', 'sk': 'slovak', 'sl': 'slovenian', 'so': 'somali', 'es': 'spanish', 'su': 'sundanese',
    'sw': 'swahili', 'sv': 'swedish', 'tg': 'tajik', 'ta': 'tamil', 'te': 'telugu', 'th': 'thai', 'tr': 'turkish',
    'uk': 'ukrainian', 'ur': 'urdu', 'ug': 'uyghur', 'uz': 'uzbek', 'vi': 'vietnamese', 'cy': 'welsh', 'xh': 'xhosa', 'yi': 'yiddish', 'yo':
    'yoruba', 'zu': 'zulu'
}

# Function to translate text from one language to another
def translator(text, fromLang, toLang):
    translator = Translator()
    return translator.translate(text, src=fromLang, dest=toLang).text

# Function to read the content of a file
def readFile(fileName):
    if not fileName.endswith(".txt"):
        fileName += ".txt"
    try:
        with open(fileName) as opfr:
            content = opfr.readlines()
    finally:
        opfr.close()
    return content

# Function to write translations to a file
def writeFile(fileName: str, fromLang: str, toLang1: str, toLang2: str) -> None:
    start = time.time()
    opfw = None

    try:
        # Open a file for writing translations
        output_file_name = LANGUAGES[fromLang].capitalize() + " vocabularies translated to " + LANGUAGES[toLang1].capitalize()
        if toLang2:
            output_file_name += " and " + LANGUAGES[toLang2].capitalize()
        output_file_name += ".txt"
        opfw = open(output_file_name, "w", encoding="utf-8")

        text = readFile(fileName)

        # Calculate the maximum English word length
        max_english_length = max(len(text[i].split()[0]) for i in range(2, len(text)))

        # Define widths for columns
        col1_width = max_english_length + 5
        col2_width = 25  # Adjust the width
        col3_width = 25  # Adjust the width

        # Write headers to the output file
        opfw.write(text[0].ljust(col1_width) + text[1].ljust(col2_width) + "(All these words are translated in " + LANGUAGES[toLang1].capitalize())
        if toLang2:
            opfw.write(" and " + LANGUAGES[toLang2].capitalize())
        opfw.write(")\n\n")

        # Translate and write each word and its translation
        for i in range(2, len(text)):
            words = text[i].split()
            english_word = " ".join(words[:-1])
            translation1 = translator(words[0], fromLang, toLang1)
            padding1 = " " * (max_english_length - len(english_word) + 20)  # Adjust padding

            # Check if toLang2 is not empty before assigning padding2
            if toLang2:
                translation2 = translator(words[0], fromLang, toLang2)
                padding2 = " " * (len(translation1) + 5)  # Adjust padding
            else:
                translation2 = ""  # Initialize translation2 as an empty string
                padding2 = ""  # Initialize padding2 as an empty string

            opfw.write(f"[{i-1}] .  {english_word} {padding1} {translation1} {padding2} {translation2} \n\n")

    finally:
        if opfw:
            opfw.close()

    # Record end time
    end = time.time()
    tmp = ((end - start) / 60)
    sec, minute = math.modf(tmp)
    print("The execution time is", minute, 'm  :', "{:.2f}".format(sec * 10), 's ')

# Main program

def main():
    dic = """
               __             __
    ________  |__|       __  |__|
    \______ \  __  _____|  |_ __  ____   ____ _____ _______ __ __
     |    |  \|  |/ ___\   __\  |/  _ \ /    \\__  \\_  __ <  |  |
     |    `   \  \  \___|  | |  (  <_> )   |  \/ __ \|  | \/\__  |
    /_________/__|\_____>__| |__|\____/|___|__(______/__|      / |
                                                            __/  |
                                                            \    |
                                                             \_ /
"""

    print(dic)
    print("To Know About Or How To Use This Program Write [about] Instead Of Filename")
    fileName = input("Enter the vocabulary file name : \n")
    if fileName == "about":
        print("\nThis program will translate a vocabulary list into 2 languages")
        print("give a file name, the file must be in txt format")
        print("This program is made by\n" + POuria + "\n\n\n")
        exit(0)
    fromLang = input("Source language : ")
    if fromLang == "":
        fromLang = "en"
    toLang1 = input("The first language : ")
    toLang2 = input("The second language : ")
    if fromLang == "":
        fromLang = ""

    writeFile(fileName, fromLang, toLang1, toLang2)

if __name__ == "__main__":
    main()
