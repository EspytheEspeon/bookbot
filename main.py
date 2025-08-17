#get_book_text function: takes in file name, returns string
def get_book_text(f):
    file_contents = f.read()
    return file_contents

#Import call for the function in stats.py for get_words
from stats import get_words

#Import call for the function in stats.py for get_characters
from stats import get_characters

#Import call for the function in stats.py for get_report
from stats import get_report

#main
with open("books/frankenstein.txt") as f:
    book1 = get_book_text(f)
    book2 = get_words(book1)
    book3 = get_characters(book1)
    book4 = get_report(book3)

#print(f"{book2} words found in the document" )
print(f"{book2} words found in the document" )

#print a dictionary of each character and how many times it appears in the book
#print(book3)

#print a list of the dictionary entries sorted by the value of the entries
print(book4)

print("=========== Bookbot ============")
print("Analyzing book found at books/frankenstein.txt...")
print("---------- Word Count ----------")
print(f"Found {book2} total words")
print("---------- Character Count -----")
for i in book4:
    print (f"{i['letter']}: {i['value']}")
print("=========== End ===========")