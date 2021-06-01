#!/usr/bin/env python3

from urllib.request import Request, urlopen 

url = "https://www.cheollimacivildefense.org/"
user_agent = "Mozilla/5.0"
req = Request(url, headers = {"User-Agent": user_agent})
page = urlopen(req)
html_bytes = page.read()
html = html_bytes.decode("utf-8")

file_name = "site.txt"
try:
    file = open(file_name, "r")
except:
    file = open(file_name,  "w")
    file.close()
    file = open(file_name, "r")

old_html = file.read()
file.close()

compare = old_html == html

if compare:
    print("No changes detected")
else: 
    file = open(file_name, "w")
    file.write(html)
    file.close()
    print("Changes detected")