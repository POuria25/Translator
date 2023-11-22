# Translator

This Python script is a language translation tool that efficiently translates a vocabulary list from one language to two other specified languages. The program utilizes the Google Translate API for language translation.

Here's an overview of the key components:

Libraries:

The script imports necessary libraries such as encode from encodings.utf_8_sig, Empty from queue, Translator from googletrans, time, and math.
Languages Dictionary:

There's a dictionary named LANGUAGES that maps language codes to their corresponding names.
Translation Functions:

The script defines a function called translator that uses the Google Translate API to translate text from one language to another.
Two additional functions, readFile and writeFile, are defined to read the content of a file and write translations to a new file, respectively.
Main Program:

The main program presents a graphical header and prompts the user to enter the vocabulary file name, source language, and two target languages.
If the user enters "about" instead of a filename, it provides information about the program and the creator before exiting.
The program then calls the writeFile function to perform the translations and write the results to an output file.

Usage:

Users can input the vocabulary file name, source language, and two target languages.
The program reads the file, translates each word from the source language to the two target languages, and writes the results to an output file.
The execution time of the program is displayed at the end.
Note: The program is designed to work with text files containing vocabulary lists, and it uses the Google Translate API for language translation. Additionally, it appears that there might be some issues in the input validation part of the code, as fromLang is checked twice without apparent changes. Users should ensure they have the necessary libraries installed and an internet connection to use the Google Translate API.

