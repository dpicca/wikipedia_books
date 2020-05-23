import re
from Character import Character

class DumpParser():

    def check_characters(self, markdown):
        characters = {}

        regex_charac_list = re.compile(r"""(\\n={2,}[\w\s]*[Cc]haracters\s*={2,}\\n)
                                                (.+?)(?=\\n\\n==[^=]+==\\n)""", re.X)
        regex_charac_v1 = re.compile(r"(\\'\\'\\')(.+?)(\\'\\'\\'\s?)(:\s|–\s|-\s|,\s)(.+?)(\\n\*)")
        regex_charac_v2 = re.compile(r"(===)(.+?)(===)(\n)(.+?)(\\n\\n)")
        regex_charac_v3 = re.compile(r"(\\s\*)(.+?)(:\s)(.+?)(\\n\*|\\n;)")

        if bool(re.search(regex_charac_list, markdown)):
            for match in re.finditer(regex_charac_list, markdown):
                markdown = match.group(2)

            for match in re.finditer(regex_charac_v1, markdown):

                name = match.group(2)

                name = re.sub(r'\\+\'', r'', name)
                name = re.sub(r'\[\[|\]\]', r'', name)

                description = match.group(5)

                description = re.sub(r'\[\[|\]\]', r'', description)
                description = re.sub(r'\\+', r'', description)
                description = re.sub(r'<.+?>', r'', description)
                description = re.sub(r'{{.+?}}', r'', description)

                characters[name] = description

            for match in re.finditer(regex_charac_v2, markdown):

                name = match.group(2)
                name = re.sub(r'\[\[|\]\]', r'', name)

                description = match.group(5)
                description = re.sub(r'\[\[|\]\]', r'', description)
                description = re.sub(r'\\+', r'', description)
                description = re.sub(r'<.+?>', r'', description)
                description = re.sub(r'{{.+?}}', r'', description)

                characters[name] = description

            for match in re.finditer(regex_charac_v3, markdown):

                name = match.group(2)
                name = re.sub(r'\[\[|\]\]', r'', name)

                description = match.group(4)
                description = re.sub(r'\[\[|\]\]', r'', description)
                description = re.sub(r'\\+', r'', description)
                description = re.sub(r'<.+?>', r'', description)
                description = re.sub(r'{{.+?}}', r'', description)

                characters[name] = description

            def get_characters():
                return [Character(key, item) for key, item in characters.items()]

            return get_characters()
