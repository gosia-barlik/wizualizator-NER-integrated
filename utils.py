import re
import requests
from bs4 import BeautifulSoup

def get_text_from_pracuj_pl(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    c = soup.find('div', {'class': 'OfferView2j5FqN'})
    plaintext = ''
    if c:
        plaintext = "\n".join(item.strip() for item in c.find_all(text=True))
        plaintext = re.sub('(\n)([a-zżźśćńóąęł])', ' \\2', plaintext)
        plaintext = plaintext.split('\n')
        plaintext = [item for item in plaintext if item != '']
        plaintext = '\n'.join(plaintext)
    else:
        c = soup.find('div', {'class': 'OfferViewgl652f'})
        if c:
            plaintext = "\n".join(item.strip() for item in c.find_all(text=True))
            plaintext = re.sub('(\n)([a-zżźśćńóąęł])', ' \\2', plaintext)
            plaintext = plaintext.split('\n')
            plaintext = [item for item in plaintext if item != '']
            plaintext = '\n'.join(plaintext)
        else:
            c = soup.find('div', {'class': 'OfferView3gNh9o'})
            if c:
                plaintext = "\n".join(item.strip() for item in c.find_all(text=True))
                plaintext = re.sub('(\n)([a-zżźśćńóąęł])', ' \\2', plaintext)
                plaintext = plaintext.split('\n')
                plaintext = [item for item in plaintext if item != '']
                plaintext = '\n'.join(plaintext)
    return plaintext
