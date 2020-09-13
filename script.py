from bs4 import BeautifulSoup
import requests
url = "https://translate.google.com.tr/#view=home&op=translate&sl=auto&tl=fa&text=hello%20how%20are%20you"
r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")
result = soup.find("span", attrs={"class":"translation"})


print(result)