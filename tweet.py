import tweepy
import imgen
import os
import time
global file

with os.scandir() as it:
    for entry in it:
        if entry.name.startswith('day') and entry.is_file():
            file = (entry.name)
            break
            
dot = file.index('.')
fileday = int(file[3:dot])


if fileday <= imgen.day-3:
    print("generando imagen...")
    imgen.crear_imagen()
    os.remove(file)
    # Authenticate to Twitter
    auth = tweepy.OAuthHandler("YOUR API KEY GOES HERE", "YOUR API KEY GOES HERE")
    auth.set_access_token("YOUR API KEY GOES HERE", "YOUR API KEY GOES HERE")

    # Create API object
    api = tweepy.API(auth, wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True)
    print("Subiendo foto a tw...")
    api.update_with_media("day"+str(imgen.day)+".png") 
    print("done")

else:
    print("No han pasado 3 días desde la última vez que fue generada")
    time.sleep(2)

