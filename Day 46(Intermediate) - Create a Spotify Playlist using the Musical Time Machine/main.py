# required imports
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# taking the date from user.
date = input(
    "Which year you want to travel to?Type the date in this format YYYY-MM-DD:"
)

# URL of the website for top 100 songs and also for scrapping
URL = f"https://www.billboard.com/charts/hot-100/{date}/"
# print(URL)
response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

# Scrapping all the songs which was filtered according to the given date.
song_names_spans = soup.find_all(
    "h3",
    class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only",
)
song_list = [song.getText().replace("\n", "") for song in song_names_spans]
# print(song_list)


# using spotipy to access spotify playlist - API
# giving all the basic credentials required as per the documentation.
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="0a637edef25440379bf1e0c109cb8e58",
        client_secret="d1cb426583f841c38d75bd59a38d4b8a",
        show_dialog=True,
        cache_path="token.txt",
    )
)
user_id = sp.current_user()["id"]

# generating song uri from the names of tha song.
song_uris = []
year = date.split("-")[0]
for song in song_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


playlist = sp.user_playlist_create(
    user=user_id, name=f"{date} Billboard 100", public=False
)
# print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
