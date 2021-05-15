import requests,bs4
from bs4 import BeautifulSoup as bSoup
from colorama import Fore , init
init()
lg = Fore.LIGHTGREEN_EX    
ly = Fore.LIGHTYELLOW_EX
lr = Fore.LIGHTRED_EX
lc = Fore.LIGHTCYAN_EX
dc = Fore.CYAN

banner = """
 █▄█ ▀█▀   ▀█▀ ▄▀█ █▀▀   █▀▀ █ █▄ █ █▀▄ █▀▀ █▀█
  █   █     █  █▀█ █▄█   █▀  █ █ ▀█ █▄▀ ██▄ █▀▄
"""
tagline = """-------------------------------------------------
           [+] Coded by GH0STH4CKER
-------------------------------------------------"""
print(lc+banner,dc+tagline)

url = input('Youtube video link : ')

r = requests.get(url)

page_soup = bSoup(r.text,"html.parser")  

html = page_soup.find_all("meta",{"name":"keywords"})
html2 = page_soup.find_all("meta",{"name":"title"})
html3 = page_soup.find_all("link",{"itemprop":"name"})


cname = html3[0]['content'] 
vname = html2[0]['content'] 
tags = html[0]['content'].split(',') 

print(lc+"\nChannel   : ",cname)
print("Video     : ",vname)
print("\nKeywords  : \n")

for i in tags :
    if i[0] == " " :
        i = i[+1:]
    print(i)

input("")