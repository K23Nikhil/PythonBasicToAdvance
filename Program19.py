import requests as re
import bs4 
import urllib3


url = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"
getHtml = re.get(url)
html = getHtml.text
htmlPage = bs4.BeautifulSoup(html)
for i in htmlPage.find_all('ul', class_ = 'internal-recirc__items'):
    for j  in i.find_all('a', class_ = 'internal-recirc__link' ):
        print("Post URL:", j['href'], "Post Title:", j.find('span', class_ ='internal-recirc__title').text, "Post Description: ", j.find('span', class_ = 'internal-recirc__title').text)
        
