""" Contains the class that counts the proportion of books with a character list"""

import re

class BooksWithList():
    """
    Counts the proportion of books with a character list
    """
    def percent_of_books(self, books_list):
        """
        Counts the proportion of books with a character list

        Parameters
        ----------
        books_list: list
            a list of all the books in the json file

        Returns
        -------
        percent: int
            the percentage of books with a characters list
        """
        regex_charac_list = re.compile(r"""(\\n={2,}[\w\s]*[Cc]haracters\s*={2,}\\n)
                                            (.+?)(?=\\n\\n==[^=]+==\\n)""", re.X)

        has_list = 0

        for book in books_list:
            if re.findall(regex_charac_list, str(book)):
                has_list += 1

        percent = has_list/len(books_list) * 100

        return percent
