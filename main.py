# Program to translate words in a text file based on a bilingual glossary in CSV format

import csv

def translate_words(glossary_file, input_file, output_file):
    glossary = {}
    with open(glossary_file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            glossary[row[0]] = row[1]
    with open(input_file, 'r') as f:
        text = f.read()
    for word in glossary:
        text = text.replace(word, glossary[word])
    with open(output_file, 'w') as f:
        f.write(text)
        
glossary_file = 'glossary.csv'
input_file = 'input.txt'
output_file = 'output.txt'
translate_words(glossary_file, input_file, output_file)
