from pymupdf import open
import re
from typing import List
from pathlib import Path

def extract_paragraphs(pdf_path: str) -> List[str]:

    """ this function takes a pdf file path as input and returns a array of its paragraphs """
    doc = open(pdf_path)
    paragraphs = []
    for page in doc:
       # get blocks from the page
       blocks = page.get_text("blocks")

       blocks = sorted(blocks, key=lambda b: (b[1], b[0]))

       for block in blocks:
           text = block[4]

           #Replace the line breaks inside a paragraph with a sapce
           text = re.sub(r"\r+", " ", text).strip()

           if text:
                paragraphs.append(text)

    return paragraphs

print(len(extract_paragraphs("../pdfs/Rag_Test.pdf")))