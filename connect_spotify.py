#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import spotipy, webbrowser 
from spotipy import util as su

def connectSpotify():

	cli_id = open('/Users/user/Documents/client_id_spotify.txt').read().strip()
	cli_sec = open('/Users/user/Documents/client_secret_spotify.txt').read().strip()
	redirect='http://localhost:8080'
	

	token = su.prompt_for_user_token(username='El AD',scope='streaming',client_id=cli_id,client_secret=cli_sec,redirect_uri=redirect)
	if token:
		service  = spotipy.Spotify(auth=token)
		print("Sucessfully authenticated to Spotify.\n")

	search_string = input("Please enter album,song,artist, etc to search.\n")
	results = service.search(search_string) 

	for i in range(len(results['tracks']['items'])):
		externalUrl = results['tracks']['items'][i]['album']['external_urls']['spotify']
		webbrowser.open(str(externalUrl))
		input("Press any key to continue to next track.\n")

if __name__ == "__main__":
	connectSpotify()
