#Song search
import Applemusic.py 
import requests

# Constants for Apple Music API
BASE_URL = 'https://api.music.apple.com/v1'
SEARCH_URL = f'{BASE_URL}/catalog/us/search'
HEADERS = {
    'Authorization': 'Bearer YOUR_ACCESS_TOKEN',
    'Music-User-Token': 'YOUR_USER_TOKEN',
}

# Function to search for songs in Apple Music
def search_songs(query):
    params = {
        'term': query,
        'types': 'songs',
        'limit': 10,  # Set the limit of results to 10
    }

    response = requests.get(SEARCH_URL, headers=HEADERS, params=params)

    if response.status_code == 200:
        data = response.json()
        songs = data.get('results', {}).get('songs', {}).get('data', [])

        if songs:
            print('Search results:')
            for song in songs:
                print(f'Track Name: {song.get("attributes", {}).get("name")}')
                print(f'Artist: {song.get("attributes", {}).get("artistName")}')
                print(f'Album: {song.get("attributes", {}).get("albumName")}')
                print(f'Preview URL: {song.get("attributes", {}).get("previewUrl")}')
                print('---')
        else:
            print('No songs found.')
    else:
        print('Failed to search for songs.')

# Usage
query = input('Enter a song name: ')
search_songs(query)

#Creating a playlist

import requests

# Constants for Apple Music API
BASE_URL = 'https://api.music.apple.com/v1'
PLAYLISTS_URL = f'{BASE_URL}/me/library/playlists'
HEADERS = {
    'Authorization': 'Bearer YOUR_ACCESS_TOKEN',
    'Music-User-Token': 'YOUR_USER_TOKEN',
    'Content-Type': 'application/json',
}

# Function to create a playlist in Apple Music
def create_playlist(playlist_name, track_ids):
    data = {
        'attributes': {
            'name': playlist_name,
        },
        'relationships': {
            'tracks': {
                'data': [{'id': track_id, 'type': 'songs'} for track_id in track_ids],
            },
        },
    }

    response = requests.post(PLAYLISTS_URL, headers=HEADERS, json=data)

    if response.status_code == 201:
        print('Playlist created successfully.')
    else:
        print('Failed to create playlist.')
        print(response.json())

# Usage
playlist_name = input('Enter playlist name: ')
track_ids = input('Enter track IDs (comma-separated): ').split(',')
create_playlist(playlist_name, track_ids)
