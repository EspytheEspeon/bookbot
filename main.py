#get_book_text function: takes in file name, returns string
def get_book_text(f):
    file_contents = f.read()
    return file_contents

#Import call for the function in stats.py
from stats import get_words


#main
with open("books/frankenstein.txt") as f:
    book1 = get_book_text(f)
    book2 = get_words(book1)

print(f"{book2} words found in the document" )

