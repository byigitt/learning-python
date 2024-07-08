import requests
from bs4 import BeautifulSoup

username = input("[+] enter your username: ")
url = f"https://last.fm/user/{username}"

print("[?] getting the lastfm page")
page = requests.get(url = url)

print("[?] parsing the page")
soup = BeautifulSoup(page.content, "html.parser")
print("[?] finding about-me-sidebar")
table = soup.find_all("section", class_="about-me-sidebar")
print("[?] getting the text")
biography = table[0].find("p").text
print(f"[+] heres user\'s biography: {biography}")