""" Contains the class fetching the characters and their description"""

import re
import json
from Character import Character
from Book import Book

class DumpParser():
    """
    The class that fetches the characters and their description and puts them in in a Dataclass

    Example
    -------
    ::
        form dumpparser import DumpParser

        parser = DumpParser()
        books_list = parser.import_list()
        books_output = parser.get_book()

        Book(Title='Dracula', Author='Bram Stoker', 
            Characters=[Character(Character='Count Dracula', Description='A Transylvanian noble who has purchased a house in London.'),
            Character(Character='Lucy Westenra', Description="A 19-year-old aristocrat; Mina's best friend; Arthur's fiancée and Dracula's first victim. "),
            Character(Character='John Seward', Description="A doctor; one of Lucy's suitors and a former student of Van Helsing."),
            Character(Character='Quincey Morris', Description="An American cowboy and explorer; and one of Lucy's suitors.")])

    """

    def import_list(self):
        """
        imports the json list.

        Returns
        -------
        books_list: str
            A list of every json entry
        """
        books_list = []

        with open('test.json', 'r') as json_list:
            for row in json_list:
                book = json.loads(row)
                books_list.append(book)
        
        return books_list

    def check_characters(self, markdown):
        """
        Matches the characters and description for book.

        Parameters
        ----------
        markdown = str
            a string of every book the books_list
        
        Returns
        -------
        get_characters(): list
            a list of every Dataclass Character for a book

        """
        characters = {}

        regex_charac_list = re.compile(r"""(\\n={2,}[\w\s]*[Cc]haracters\s*={2,}\\n)
                                                (.+?)(?=\\n\\n==[^=]+==\\n)""", re.X)
        regex_charac_v1 = re.compile(r"(\\'\\'\\')(.+?)(\\'\\'\\'\s?)(:\s|–\s|-\s|,\s|\\n|\s)(.+?)(\\n\*?)")
        regex_charac_v2 = re.compile(r"(===)(.+?)(===)(\\n)(.+?)(\\n\\n)")
        regex_charac_v3 = re.compile(r"(\\n\*\s?)(.+?)(:\s|–\s|-\s|,\s|&ndash;)(.+?)(\\n\*|\\n;)")
        regex_charac_v4 = re.compile(r"(\\n;)(.+?)(\\n)(.+?)(\\n)")

        if bool(re.search(regex_charac_list, markdown)):
            for match in re.finditer(regex_charac_list, markdown):
                markdown = match.group(2)

            for match in re.finditer(regex_charac_v1, markdown):

                name = match.group(2)
                name = re.sub(r'\\+\'', r'', name)
                name = re.sub(r'\[\[|\]\]', r'', name)

                description = match.group(5)
                description = re.sub(r'\[\[|\]\]', r'', description)
                description = re.sub(r'\\+\'', r'', description)
                description = re.sub(r'\\+', r'', description)
                description = re.sub(r'<.+?>', r'', description)
                description = re.sub(r'{{.+?}}', r'', description)

                characters[name] = description

            for match in re.finditer(regex_charac_v2, markdown):

                name = match.group(2)
                name = re.sub(r'\\+\'', r'', name)
                name = re.sub(r'\[\[|\]\]', r'', name)

                description = match.group(5)
                description = re.sub(r'\[\[|\]\]', r'', description)
                description = re.sub(r'\\+\'', r'', description)
                description = re.sub(r'\\+', r'', description)
                description = re.sub(r'<.+?>', r'', description)
                description = re.sub(r'{{.+?}}', r'', description)

                characters[name] = description

            for match in re.finditer(regex_charac_v3, markdown):

                name = match.group(2)
                name = re.sub(r'\\+\'', r'', name)
                name = re.sub(r'\[\[|\]\]', r'', name)

                description = match.group(4)
                description = re.sub(r'\[\[|\]\]', r'', description)
                description = re.sub(r'\\+\'', r'', description)
                description = re.sub(r'\\+', r'', description)
                description = re.sub(r'<.+?>', r'', description)
                description = re.sub(r'{{.+?}}', r'', description)

                characters[name] = description
            
            for match in re.finditer(regex_charac_v4, markdown):

                name = match.group(2)
                name = re.sub(r'\\+\'', r'', name)
                name = re.sub(r'\[\[|\]\]', r'', name)

                description = match.group(4)
                description = re.sub(r'\[\[|\]\]', r'', description)
                description = re.sub(r'\\+\'', r'', description)
                description = re.sub(r'\\+', r'', description)
                description = re.sub(r'<.+?>', r'', description)
                description = re.sub(r'{{.+?}}', r'', description)

                characters[name] = description

            def get_characters():
                """
                creates Dataclasses Character for every character and puts them in a list

                Returns
                -------
                :list
                    a list of every Dataclass Character for a book
                
                Example
                -------
                ::

                    [Character(Character='Princess Irulan ', Description='princess-consort of Emperor Paul Atreides'),
                     Character(Character='Alia Atreides|Alia ', Description="Paul's sister, born with prescient awareness, a reverend mother"),
                     Character(Character='Guild Navigator#Edric|Edric ', Description='a prescient guild navigator and conspirator'),
                     Character(Character='Hayt ', Description="a revived Tleilaxu ghola of Paul's childhood teacher, Duncan Idaho")])
                """
                return [Character(key, item) for key, item in characters.items()]

            return get_characters()

    def get_book(self):
        """
        Function that creates and fills the Book Dataclass

        Returns
        -------
        books_output:list
            a list of every Book Dataclass created from the json file
        
        Example
        -------
        ::
            Book(Title='Flash Crowd', Author='None', Characters=[Character(Character='George Lincoln Bailey ', Description='CBA editor'), 
                Character(Character='Janice Wolfe ', Description='friend of Jerryberry'), 
                Character(Character='Gregory Scheffer ', Description='customs guard.'), 
                Character(Character='Harry McCord ', Description='former Los Angeles Police Department Chief. ')])
            Book(Title='Fourier analysis', Author='None', Characters=None)  
        """

        parser = DumpParser()
        books_list = parser.import_list()

        regex_title = re.compile(r'([\'\"]title[\'\"]: [\'\"])(.+?)([\'\"],)')
        regex_author = re.compile(r'([\'\"]author[\'\"]: ([\'\"]http:\/\/dbpedia\.org\/resource\/)?)(.+?)(?=[\'\"]?,)')
        books_output = []

        for book in books_list:
        
            title = re.search(regex_title, str(book))
            title = title.group(2)

            author = re.search(regex_author, str(book))
            author = author.group(3)
            author = re.sub(r'_', r' ', author)

            markdown = str(book)
            characters_list = parser.check_characters(markdown)

            books_output.append(Book(title, author, characters_list))

        return books_output