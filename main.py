"""main function"""
from dumpparser import DumpParser
from books_with_list import BooksWithList

def main():
    """
    The main function

    Prints the percentage of books with a charcters list
    Prints the the Book Dataclasses
    """

    parser = DumpParser()
    books_list = parser.import_list()
    books_output = parser.get_book()

    percent = BooksWithList().percent_of_books(books_list)
    print("%d %% of the books have a characters list." % percent)

    for book in books_output:
        print(book)

if __name__ == "__main__":
    main()
