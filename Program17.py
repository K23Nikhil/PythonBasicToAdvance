import requests as re
from bs4 import BeautifulSoup
data = re.get("https://www.nytimes.com/section/technology")
html = data.text
soup = BeautifulSoup(html)
NewsList = []
NewsSubPost = []
for i in soup.findAll('div', class_ ='css-13mho3u'):
    NewsList.append(i)
    print(i)
    for j in i.findAll('li', class_ ='css-css-ye6x8s'):
        NewsSubPost.append(j)
        #print("Post Description ", j['p'])
        #print(j.text)
        #print("Post URL", j['href'])
        print("Post Title:", j.find('h2').text)
print("News Count", len(NewsList))
print("News SubPost Count", len(NewsSubPost))