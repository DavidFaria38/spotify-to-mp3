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
spotifyToken = "BQCLs6M45C_V90tCpDTwR6UyYgys9Nqur7fcStVNDuM9P2Ogw-SFbVc36YuHtc6zvPYI68LrFp5h2pyu4IAen_3JgUb77bVCgemwBxdf6pv2DwpL4eTCpycpyuu8l6NJIXqXJe3fTQoecBQrjajb25T8l2K-t9cl1bupSF6gPijQtsIKfdezJVV5HnBqgMhb17YY-Qvb-l6mGLtvKNSVyZAGm0sqKRfwDMQJIBWsn4g"
# spotifyClientId = "674f3dc4619b4bfd9648cab56622b673"

playlistId = "2JcuiV3pxwG9kF7KlaysXc"

spotify = GetSpotify(spotifyBaseUrl, spotifyToken)
playlist = spotify.getPlaylist(playlistId)


for song in playlist['items']:
    songName = song['track']['name']
    albumName = song['track']['album']['name']
    artistName = song['track']['album']['artists'][0]['name']
    
    print('{} | {} by {}'.format(songName, albumName, artistName))
