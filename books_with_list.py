import re

class books_with_list():
    
    def percent_of_books(self, books_list):
        REGEX_CHARACTERS_LIST = re.compile(r'(\\n={2,}[\w\s]*[Cc]haracters\s*={2,}\\n)(.+?)(?=\\n\\n==[^=]+==\\n)')

        has_list = 0

        for book in books_list:
            if re.findall(REGEX_CHARACTERS_LIST, str(book)):
                has_list += 1
        
        percent = has_list/len(books_list) * 100
        
        return percent