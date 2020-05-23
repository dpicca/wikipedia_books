import re

class BooksWithList():

    def percent_of_books(self, books_list):
        regex_charac_list = re.compile(r"""(\\n={2,}[\w\s]*[Cc]haracters\s*={2,}\\n)
                                            (.+?)(?=\\n\\n==[^=]+==\\n)""", re.X)

        has_list = 0

        for book in books_list:
            if re.findall(regex_charac_list, str(book)):
                has_list += 1

        percent = has_list/len(books_list) * 100

        return percent
