import argparse
import os
from bs4 import UnicodeDammit
import csv
from PyPDF2 import PdfFileReader
import docx
def search_text(filename, search):

    with open(filename, 'rb') as file:
        content = file.read(1024)

    suggestion = UnicodeDammit(content)
    encoding = suggestion.original_encoding

    with open(filename, encoding=encoding) as en_file:
        for line in en_file:
            if search.lower() in line.lower():
                return True

    return False


def search_csv(filename, search):
    with open(filename) as file:
        content = csv.reader(file)

        for row in content:
            for r in row:
                if search.lower() in str(r).lower():
                    return True

    return False


def search_pdf(filename, search):

    with open(filename, 'rb') as file:
        document = PdfFileReader(file)
        if document.isEncrypted:
            return False
        for i in range(document.numPages):
            text = document.pages[i].extractText()
            if search.lower() in text.lower():
                return True

    return False


def search_docx(filename, search):
    doc = docx.Document(filename)
    for pagraph in doc.paragraphs:
        if search.lower() in pagraph.text.lower():
            return True
    return False


def main(search):
    for root, dirs, files in os.walk('documents'):
        for file in files:
            file_full_path = os.path.join(root, file)
            if file.endswith(".txt"):
                if search_text(file_full_path, search):
                    print(f"Word found in {file_full_path}")
            elif file.endswith(".csv"):
                if search_csv(file_full_path, search):
                    print(f"Word found in {file_full_path}")
            elif file.endswith(".pdf"):
                if search_pdf(file_full_path, search):
                    print(f"Word found in {file_full_path}")
            elif file.endswith(".docx"):
                if search_docx(file_full_path, search):
                    print(f"Word found in {file_full_path}")
            else:
                pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', type=str, help="Word to search")
    args = parser.parse_args()
    try:
        main(args.w)
    except Exception as err:
        print("Error run script",err)
        exit(1)