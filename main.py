#get_book_text function: takes in file name, returns string
def get_book_text(f):
    file_contents = f.read()
    return file_contents

#Import call for the function in stats.py for get_words
from stats import get_words

#Import call for the function in stats.py for get_characters
from stats import get_characters

#main
with open("books/frankenstein.txt") as f:
    book1 = get_book_text(f)
    book2 = get_words(book1)
    book3 = get_characters(book1)

#print(f"{book2} words found in the document" )
print(f"{book2} words found in the document" )

#print a dictionary of each character and how many times it appears in the book
print(book3)