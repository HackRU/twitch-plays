import time
from twitch_plays_hackru import TwitchPlaysOnline, TwitchPlaysOffline


base_options = {
    # List of voting options that the TwitchPlays API will detect for.
    "OPTIONS": ["1","2","3","hi","bye"],
    # how long to count votes
    "VOTE_INTERVAL": 5
}

twitch_options = {
    "PASS": "oauth:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "BOT": "TwitchPlaysBot",
    "CHANNEL": "<YOUR CHANNEL>",
    "OWNER": "<YOUR CHANNEL>",
    "OPTIONS": base_options["OPTIONS"],
    "VOTE_INTERVAL": base_options["VOTE_INTERVAL"]
}

# Initalize the TwitchPlays bot.
tPlays = TwitchPlaysOffline(**base_options)
#tPlays = TwitchPlaysOnline(**twitch_options)

while True:
    time.sleep(1)
    result = tPlays.vote_result()
    if result:
        print("players choose : ", result)
