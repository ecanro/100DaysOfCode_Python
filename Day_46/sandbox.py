from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import config

URL = "https://www.billboard.com/charts/hot-100"
date = input("Which year do you want to travel to?, Insert a date in this format: YYYY-MM-DD:\n ")

response = requests.get(url=f"{URL}/{date}")
soup = BeautifulSoup(response.text, "html.parser")
# print(soup.prettify())
song_names_tags = soup.findAll(name="span", class_="chart-element__information__song")[:100]
song_names = [song.getText() for song in song_names_tags]
# print(song_names)

# Spotify authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=config.sp_ID,
        client_secret=config.sp_Secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
print(user_id)

#Searching Spotify for songs by title
song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

# Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)