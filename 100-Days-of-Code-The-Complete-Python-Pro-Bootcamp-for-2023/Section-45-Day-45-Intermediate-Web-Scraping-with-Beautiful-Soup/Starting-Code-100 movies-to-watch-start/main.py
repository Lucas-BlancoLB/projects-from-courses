import requests
from bs4 import BeautifulSoup
import html

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇


r = requests.get(URL).text
soup = BeautifulSoup(r, "html.parser")
top_100_movies = [html.unescape(movie.text).encode('latin1').decode('utf-8')
                  for movie in soup.find_all(name='h3', class_="title")][::-1]
string = ''
for i in range(len(top_100_movies)):
    string += f"{top_100_movies[i]}\n"

with open('text.txt', mode="w", encoding='utf-8') as file:
    file.write(string.strip())