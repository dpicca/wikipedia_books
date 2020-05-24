""" Contains the class fetching the characters and their description"""

import re
import json
from Character import Character
from Book import Book

class DumpParser():
    """

    """

    def import_list(self):
        books_list = []

        with open('test.json', 'r') as json_list:
            for row in json_list:
                book = json.loads(row)
                books_list.append(book)
        
        return books_list

    def check_characters(self, markdown):
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
                return [Character(key, item) for key, item in characters.items()]

            return get_characters()

    def get_book(self):

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