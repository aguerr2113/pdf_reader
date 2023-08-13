import re
from PyPDF2 import PdfReader

def extract_text(pdf_file):
    with open(pdf_file,'rb') as pdf:
        reader = PdfReader(pdf, strict=False)
        print('Pages:',len(reader.pages))
        print('-'*10)
        pdf_text = [page.extract_text() for page in reader.pages]
        return pdf_text
    
def main():
    extracted_text = extract_text('sample.pdf')
    with open('output.txt', 'w', encoding='utf-8') as file:
        for page in extracted_text:
            print(page)
            file.write(page)
if __name__ == '__main__':
    main()