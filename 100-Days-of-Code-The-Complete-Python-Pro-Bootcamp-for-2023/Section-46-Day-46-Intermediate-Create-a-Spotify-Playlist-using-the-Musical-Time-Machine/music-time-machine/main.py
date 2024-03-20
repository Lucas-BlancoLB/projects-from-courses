import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime as dt
import spotipy
from spotipy.oauth2 import SpotifyOAuth


URL = "https://www.billboard.com/charts/hot-100/"

def check_date(text):
    pattern = r'^(19(5[8-9]|[6-9][0-9])|20[0-9][0-9])-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$'
    if re.match(pattern, text):
        return text
    else:
        raise ValueError(f'Wrong data format. {text}')


print("Type a full date in this format YYYY-MM-DD")
input_date = '2024-01-01'  # check_date(input("Which year do you want to travel to: "))


current_date = dt.now().strftime('%Y-%m-%d')
print(current_date)

if input_date <= current_date:
    print(f"{URL}{input_date}")

    r = requests.get(f"{URL}{input_date}").text
    soup = BeautifulSoup(r, "html.parser")

    top_songs = [x.get_text().strip() for x in soup.select(selector='li h3', class_='c-title')][:100]
    print(top_songs)

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-modify-private",
            redirect_uri="http://example.com", client_id='YOUR_UNIQUE_CLIENT_ID',
            client_secret='YOUR_UNIQUE_CLIENT_SECRET', show_dialog=True,
            cache_path ="token.txt", username='YOUR_SPOTIFY_DISPLAY_NAME'))

    user_id = sp.current_user()["id"]
    # print(user_id)

    spotify_songs = []
    for song in top_songs:
        search = sp.search(q=f"track:{song} year:{input_date[:4]}")
        print(search)
        try:
            uri = search['tracks']['items'][0]['uri']
            spotify_songs.append(uri)
        except IndexError:
            print(f"{song} not found on Spotify. Skipping.")

    new_playlist = sp.user_playlist_create(user=user_id, name=f"{input_date}music's from Billboard 100", public=False)
    print(new_playlist)
    sp.playlist_add_items(playlist_id=new_playlist["id"], items=spotify_songs)

else:
    raise ValueError(f"The date has passed the current date. {input_date}")