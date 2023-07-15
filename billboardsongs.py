from datetime import date, timedelta
import billboard
import sys
import json
import spotipy

AUTH_FILE = 'authorization.json'


def makePlaylist(year):
    songs = makeList(year)
    print('Collected songs from chart.')

    auth = loadAuth()
    sp = spotipy.Spotify(auth_manager=spotipy.oauth2.SpotifyPKCE(
        client_id=auth['client_id'],
        scope=auth['scope'],
        redirect_uri=auth['redirect_uri']))

    uris = findURIs(sp, songs, year)
    print('Found Spotify URIs.')

    user_id = sp.me()['id']
    playlist = sp.user_playlist_create(user_id, str(year))

    for n in range(0, len(uris), 100):
        sp.playlist_add_items(playlist_id=playlist['id'], items=uris[n:n + 100])
    print(f'Made playlist {year} for {sp.me()["display_name"]}.')


def findURIs(sp, songs, year):
    uris = []
    for song in songs:
        try:
            uris.append(
                sp.search(q=song, type='track')['tracks']['items'][0]['uri'])
        except IndexError:
            print(f"Couldn't fetch {song} for {year}.")
    return uris


def makeList(year):
    tracks = set()
    for date in allSaturdays(year):
        chart = billboard.ChartData('hot-100', date)
        tracks.update(
            {str(song) for song in chart.entries if str(song) not in tracks})
    return tracks


def loadAuth():
    with open(AUTH_FILE) as jsonFile:
        auth = json.load(jsonFile)
    return auth


def allSaturdays(year):
    # taken from https://stackoverflow.com/questions/2003870/how-can-i-select-all-of-the-sundays-for-a-year-using-python
    d = date(year, 1, 1)
    d += timedelta(days=(5 - d.weekday() + 7) % 7)
    while d.year == year:
        yield str(d)
        d += timedelta(days=7)


if __name__ == '__main__':
    if sys.argv[1] == 'all':
        for year in range(1958, date.today().year):
            makePlaylist(year)
    else:
        year = int(sys.argv[1])
        makePlaylist(year)