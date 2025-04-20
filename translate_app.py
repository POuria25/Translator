from deep_translator import GoogleTranslator
import time
import math
import os


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


# Dictionary of supported languages
LANGUAGES = GoogleTranslator(source='auto', target='en').get_supported_languages(as_dict=True)


# Converts language name to its code
def get_lang_code(name):
    for code, lang in LANGUAGES.items():
        if lang.lower() == name.lower():
            return code
    return None

# Translate a word using deep-translator
def translator(text, fromLang, toLang):
    try:
        return GoogleTranslator(source=fromLang, target=toLang).translate(text)
    except Exception as e:
        return f"[Error] {str(e)}"

# Read vocabulary file
def readFile(fileName):
    if not fileName.endswith(".txt"):
        fileName += ".txt"
    with open(fileName, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]
    return lines

# Write translated output to a file
def writeFile(fileName: str, fromLang: str, toLang1: str, toLang2: str) -> None:
    start = time.time()

    lines = readFile(fileName)

    # Output file name
    out_name = f"{LANGUAGES[fromLang].capitalize()} vocabularies translated to {LANGUAGES[toLang1].capitalize()}"
    if toLang2:
        out_name += f" and {LANGUAGES[toLang2].capitalize()}"
    out_name += ".txt"

    with open(out_name, "w", encoding="utf-8") as f:
        max_len = max(len(line.split()[0]) for line in lines[1:])

        header = lines[0]
        f.write(header + "\n\n")
        f.write("Index".ljust(8) + "En".ljust(max_len + 5) + LANGUAGES[toLang1].capitalize().ljust(30))
        if toLang2:
            f.write(LANGUAGES[toLang2].capitalize().ljust(30))
        f.write("\n\n")

        for idx, line in enumerate(lines[1:], start=1):
            parts = line.split()
            if not parts:
                continue
            word = parts[0]
            tr1 = translator(word, fromLang, toLang1)
            tr2 = translator(word, fromLang, toLang2) if toLang2 else ""
            f.write(f"[{idx}]".ljust(8) + word.ljust(max_len + 5) + tr1.ljust(30))
            if toLang2:
                f.write(tr2.ljust(30))
            f.write("\n")

    end = time.time()
    total = end - start
    print(f"\nTranslation completed in {int(total // 60)}m {total % 60:.2f}s")
    print(f"Output saved to '{out_name}'")

# Main interaction logic
def main():
    print("💬 Welcome to the Vocabulary Translator!")
    print("To view instructions, type 'about' as the filename.\n")

    fileName = input("Enter vocabulary filename (e.g., words.txt): ").strip()
    if fileName.lower() == "about":
        print("\nThis tool translates vocabulary lists from one language to up to two other languages.")
        print("Prepare a .txt file where each line contains one English word.")
        print("Example:\n  Hello\n  Apple\n  Love\n")
        print("Made with  ❤️  by POuria Katouzian\n")
        print("💡 For more information, visit: https://github.com/POuria25?tab=repositories")
        return

    fromLangName = input("Enter source language (e.g., English): ").strip().lower()
    toLang1Name = input("Enter first target language (e.g., French): ").strip().lower()
    toLang2Name = input("Enter second target language (optional): ").strip().lower()

    fromLang = get_lang_code(fromLangName) or 'en'
    toLang1 = get_lang_code(toLang1Name)
    toLang2 = get_lang_code(toLang2Name) if toLang2Name else None

    if not toLang1:
        print("❌ Invalid first target language.")
        return
    if toLang2Name and not toLang2:
        print("❌ Invalid second target language.")
        return

    print("🧠")
    writeFile(fileName, fromLang, toLang1, toLang2)
    print("\nTranslation completed successfully ✅!")

if __name__ == "__main__":
    main()
