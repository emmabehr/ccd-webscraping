#!/usr/bin/env python3

from urllib.request import Request, urlopen 

url = "https://www.cheollimacivildefense.org/"
user_agent = "Mozilla/5.0"
req = Request(url, headers = {"User-Agent": user_agent})
page = urlopen(req)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
print(html)