import requests
from bs4 import BeautifulSoup

def get_data(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    }

    # req = requests.get(url, headers)
    
    # with open("project.html", "w") as file:
    #     file.write(req.text)
    
    with open("project.html") as file:
         src = file.read()
         
    soup = BeautifulSoup(src, "lxml")
    articles = soup.find_all("article", class_="js-load-item")
    # print(articles)
    
    project_urls = []
    for article in articles:
        project_url = article.find("div", class_="item__inner").find("a").get("href")
        project_urls.append(project_url)
    
    for project_url in project_urls:
        req = requests.get(project_url, headers)
        
get_data("https://trends.rbc.ru/trends/tag/educational_startups") 
