import re
import requests
import config
playlist = [ "Thriller; Michael Jackson",
             "Wake Me Up; The Weeknd",
            "90210; Travis Scott",
            "When Doves Cry; Prince",
             "Daydreaming; Radiohead"         
            ]
#for now hard-code a list, but eventually import playlists and liked album, songs from Spotify or something
def getPlaylistInfo(playlist):
    for song in playlist:
        song = song.strip()
        title = song.split(';')[0]
        artist= song.split(';')[1].lstrip()

    return 0

def test():
    data = requests.get("http://ws.audioscrobbler.com/2.0/?method=track.gettoptags&artist=Michael+Jackson&track=Thriller&api_key="+ config.API_key+"&format=json" )
    print(data.text)

if __name__ == '__main__':
    getPlaylistInfo(playlist)
    test()