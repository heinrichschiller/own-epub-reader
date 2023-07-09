# This Python file uses the following encoding: utf-8
import ebooklib

from ebooklib import epub

class EpubReader:
    def __init__(self):
        pass

    def read_epub(self, book_path):
       book = epub.read_epub(book_path)
       book_content = ""
       for item in book.get_items():
           if item.get_type() == ebooklib.ITEM_DOCUMENT:
               book_content += item.get_content().decode("utf-8")

       return book_content
