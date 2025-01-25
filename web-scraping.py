import requests
from bs4 import BeautifulSoup
import re

def main():
    res = requests.get("https://news.ycombinator.com/news")
    html = BeautifulSoup(res.text, "html.parser")
    titles_scores = html.select(".subtext .subline .score")
    titles_tr = html.select(".athing")

    score_above_100 = []
    scores = []
    for item in titles_scores:
        
        if re.match(r"[1-9]\d\d points", item.text):
            
            score_above_100.append(item)
            scores.append(item.text)

    ids = []
    for i in score_above_100:
        id_news = i.get("id")[6:]
        ids.append(id_news)

    titles_of_interest = []
    for id in range(len(ids)):

        for title in titles_tr:
            if ids[id] == title.get('id'):
                item = title.select(".titleline > a")[0]
                title_article, link = item.get("href"), item.text

                titles_of_interest.append([title_article, link, scores[id]])
                break
    
    for i in titles_of_interest:
        print(i)

if __name__ == "__main__":
    main()