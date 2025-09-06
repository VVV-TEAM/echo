import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

with open("./keys.json") as file:
    data = json.load(file)

Spotify_client_ID = data["Spotify_client_ID"]
Spotify_client_secret_ID = data["Spotify_client_secret_ID"]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=Spotify_client_ID,
    client_secret=Spotify_client_secret_ID,
    redirect_uri="http://127.0.0.1:5000/callback/",
    scope="user-read-playback-state user-modify-playback-state "
          "playlist-modify-public playlist-modify-private "
          "user-library-read user-library-modify"
))

def search_music(query):
    result = sp.search(q=query, type="track", limit=1)
    track = result['tracks']['items'][0]
    print(f"found: {track['name']} - {track['artists'][0]['name']}")
    track_uri = track['uri']
    return track_uri

def choice_devices():
    devices = sp.devices()
    device_id = devices['devices'][0]['id']
    return device_id

def play_music(device_id, track_uri):
    sp.start_playback(device_id=device_id, uris=[track_uri])

def stop_play(device_id):
    sp.pause_playback(device_id=device_id)

def start_play(device_id):
    sp.start_playback(device_id=device_id)

def next_song(device_id):
    sp.next_track(device_id=device_id)

def previous_song(device_id):
    sp.previous_track(device_id=device_id)

def set_volume(volume, device_id):
    sp.volume(volume, device_id=device_id)

def what_play():
    current = sp.current_playback()
    if current:
        w_p = f"{current['item']['name']} - {current['item']['artists'][0]['name']}"
    else:
        w_p = "Nothing now playing"

    return w_p