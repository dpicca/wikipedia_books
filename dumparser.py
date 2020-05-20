import re
from Character import Character

class DumpParser():

    def check_characters(self, markdown):
        global characters
        characters = {}
        
        REGEX_CHARACTERS_LIST = re.compile(r'(\\n={2,}[\w\s]*[Cc]haracters\s*={2,}\\n)(.+?)(?=\\n\\n==[^=]+==\\n)')
        REGEX_CHARACTER_DESC = re.compile(r"(\\'\\'\\'|\s*|===|)(.+?)(\\'\\'\\'|\s*|===)(:\s|\n|-\s|,\s)(.+?)(\\n\*|\\n\\n|\\n,)")
        
        for match in re.finditer(REGEX_CHARACTERS_LIST, markdown):
            markdown = match.group(2)
            
        for match in re.finditer(REGEX_CHARACTER_DESC, markdown):
            
            name = match.group(2)
            name = re.sub(r'\\+\'|\\n|\*|\[\]', r'', name)

            description = match.group(5)
            description = re.sub(r'\[\]', r'', description)
            
            characters[name] = description

        def get_charaters():
            return [Character(key, item) for key, item in characters.items()]
        
        characters_list = get_charaters()

        return characters_list