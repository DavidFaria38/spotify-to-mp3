import requests


class GetSpotify:
    def __init__(self, spotifyBaseUrl, spotifyToken):
        print("class init")
        self.spotifyBaseUrl = spotifyBaseUrl
        self.spotifyToken = spotifyToken

    def getPlaylist(self, playlistId):
        url = self.spotifyBaseUrl + f'/v1/playlists/{playlistId}/tracks'
        headers = {'Content-Type': 'application/json',
                   'Authorization': "Bearer " + spotifyToken}

        response = requests.get(url, headers=headers).json()

        # print(response)

        return response

### END CLASSES ###


### INIT MAIN ###
spotifyBaseUrl = "https://api.spotify.com"
spotifyToken = "####"
# spotifyClientId = "####"

playlistId = "2JcuiV3pxwG9kF7KlaysXc"

spotify = GetSpotify(spotifyBaseUrl, spotifyToken)
playlist = spotify.getPlaylist(playlistId)


for song in playlist['items']:
    songName = song['track']['name']
    albumName = song['track']['album']['name']
    artistName = song['track']['album']['artists'][0]['name']
    
    print('{} | {} by {}'.format(songName, albumName, artistName))
