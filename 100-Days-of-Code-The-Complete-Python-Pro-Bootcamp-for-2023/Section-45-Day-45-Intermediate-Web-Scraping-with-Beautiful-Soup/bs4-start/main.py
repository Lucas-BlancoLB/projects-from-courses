import requests
from bs4 import BeautifulSoup


r = requests.get(url="https://news.ycombinator.com/").text

soup = BeautifulSoup(r, "html.parser")
# print(soup.find(class_='titleline'))
article_texts = [[x.find(class_="titleline").find("a").text,
                  x.find(class_="titleline").find('a').get('href')
                  ] for x in soup.find_all(class_="athing" )]

print(article_texts)

article_upvotes = [y.getText() for y in soup.find_all(name='span', class_='score') ]


print(article_upvotes)
articles = [text.append(article_upvotes[i]) for i, text in enumerate(article_texts)]

print(articles)

class_="athing"
# class_="titleline"


#
###
#


# with open("website.html", encoding="utf-8") as file:
#     html = file.read()
#     # print(html)
#
# soup = BeautifulSoup(html, "html.parser")
# print(soup.title, "|" ,soup.title.name, "|", soup.title.string, '\n')
# print(soup.p, '\n')  # it prints the first p founded
# # print(soup.prettify())  # helps visualize with an indentation
#
# all_anchor = soup.findAll("a")  # held all wanted items and put it in a list
# print(all_anchor, '\n')
# for anchor in all_anchor:
#     print(anchor.name, '|', anchor.string, '|', anchor.get("href"))
#
# paragraph = soup.find('p')  # look for the first item
# print('\n', paragraph, ' -|- ', paragraph.em, ' -|- ', paragraph.em.text, '\n', ' -|- ',f'href={paragraph.a.get("href")}')
#
# seaction_heading = soup.find(name='h3', class_="heading")
# print('\n',seaction_heading.get("class"))
#
# company_url = soup.select_one(selector='p a')  # select_one: an anchor inside paragraph
# print('\n', company_url)
#
# headings = soup.select('.heading')  # .SOMETHING denotes a class, while #SOMETHING signifies an id in HTML and CSS
# print('\n', headings)
