from Character import Character
from Book import Book
from dumparser import DumpParser
from books_with_list import books_with_list

from pathlib import Path #provisoire
import re
import json

def main():

    books_list = []

    with open('test.json', 'r') as json_list:
        for row in json_list:
            book = json.loads(row)
            books_list.append(book)
    
    list_percentage = books_with_list()
    percent = list_percentage.percent_of_books(books_list)
    print("%d %% of books have a characters list." % percent)

    REGEX_TITLE = re.compile(r'(\'title\': \')(.+?)(\',)')
    REGEX_AUTHOR = re.compile(r'(\'author\': (\'http:\/\/dbpedia\.org\/resource\/)?)(.+?)(?=\'?,)')
    books_output = []

    for book in books_list:

        title = re.search(REGEX_TITLE, str(book))
        title = title.group(2)
        author = re.search(REGEX_AUTHOR, str(book))
        author = author.group(3)

        parser = DumpParser()
        markdown = str(book)
        characters_list = parser.check_characters(markdown)
        
        books_output.append(Book(title, author, characters_list))
    
    #provisoire
    output_path = Path("books.txt")
    with output_path.open(mode="w", encoding="utf-8") as books_text:
        for book in books_output:
            books_text.write("\n" + str(book))

if __name__ == "__main__":
    main()