import re

text = " Nome: Wanderley Silva, Data de Nascimento: 2/6/1956, Email: wanderley@email.com.br, Nome: MarySilva, Data de Nascimento: 1/07/1943, Email: mary@email.com.br"

# Expresão regular
pattern_name = re.compile(r'Nome: ([\w\s]+)')
pattern_date = re.compile(r'(?P<dia>\d{1,2})/(?P<mês>\d{1,2})/(?P<ano>\d{2,4})')
pattern_email = re.compile(r'([\w_\.\d]+@\w+[(\.com)(\.br)]+)')

# result = pattern_name.findall(text)
result = pattern_date.search(text)
# result = pattern_email.findall(text)
# print(result.group('dia'))
# print(result.group('mês'))
# print(result.group('ano'))
# print(result.groupdict())


class Extractor:

    def __init__(self, text: str):
        self.text = text
        self.pattern_name = re.compile(r'Nome: ([\w\s]+)')
        self.pattern_date = re.compile(r'(?P<dia>\d{1,2})/(?P<mês>\d{1,2})/(?P<ano>\d{2,4})')
        self.pattern_email = re.compile(r'([\w_\.\d]+@\w+[(\.com)(\.br)]+)')
        
    def get_name(self) -> list:
        return self.pattern_name.findall(self.text)
    
    def get_date(self) -> list:
        groups = self.pattern_date.search(self.text)
        self.day = groups.group('dia')
        self.month = groups.group('mês')
        self.year = groups.group('ano')

        return self.pattern_date.findall(self.text)
    
    def get_email(self) -> list:
        return self.pattern_email.findall(self.text)


extractor = Extractor(text)

name = extractor.get_date()
print(name)

print(extractor.day)
print(extractor.month)
print(extractor.year)
