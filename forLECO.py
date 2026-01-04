import requests
import ssl
from bs4 import BeautifulSoup

# SSL Certificate error ignore
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

print('LECO CLI Application')

user = input('\nPlease enter your LECO Account No [Defualt: 0208066xxx]: ')
if len(user) < 1:
    user = '0208066xxx'

url = 'http://lecoapp.leco.lk:8091/LecoWebViews/Outage2022'
d = {'username': user}

print('Retrieving data from ', url)
htm = requests.post(url, data=d).text
soup = BeautifulSoup(htm, 'html.parser')

uname_html = soup('h4')
uname_html = list(uname_html)

print('\nWelcome!')
uname_li = str(uname_html[0]).split(' ')
skip_characters = ['<h4>\n<span>', '</span>\n</h4>', '<spin>', '<h4>', '</spin>', '</h4>']
for i in uname_li:
    if i in skip_characters:
        continue
    print(i.strip(), end=' ')

print('\n')
tds = soup('td')
for td in tds:
    try:
        print(td.contents[0])
    except:
        print()

print('(c)2022 W!')
