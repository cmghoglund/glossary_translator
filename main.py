# Program to translate words in a text file based on a bilingual glossary in CSV format

import csv

def load_glossary(filename):
    glossary = {}
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            word, translation = row
            glossary[word] = translation
    return glossary

def translate_words(glossary, text):
    translated_text = []
    words = text.split()
    for word in words:
        translation = glossary.get(word)
        if translation:
            translated_text.append(translation)
        else:
            translated_text.append(word)
    return ' '.join(translated_text)

def main():
    glossary_file = input("Enter filename of bilingual glossary (in csv format): ")
    input_file = input("Enter filename of text file to translate: ")
    output_file = input("Enter filename of output translated text file: ")

    glossary = load_glossary(glossary_file)

    with open(input_file, 'r') as f:
        text = f.read()

    translated_text = translate_words(glossary, text)

    with open(output_file, 'w') as f:
        f.write(translated_text)

    print("\nTranslation complete!\n")

if __name__ == "__main__":
    main()
