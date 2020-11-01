import threading
from twitch_plays import TwitchPlaysOnline, TwitchPlaysOffline

playerChoice = None

# Replaces the value of playerChoice to be the majority vote from the TwitchPlays API every 10 seconds
def get_votes(obj):
	print("I am getting voteResults")
	threading.Timer(10.0, get_votes, args=[obj]).start()
	global playerChoice
	playerChoice = obj.vote_results()


# Prints the value of playerChoice every 5 seconds
def printit():
	threading.Timer(5.0, printit).start()
	print("this is the playerChoice: ", playerChoice)


# List of voting options that the TwitchPlays API will detect for.
voteingOptions = ["1","2","3","hi","bye"]

# Initalize the TwitchPlays bot.
tPlays = TwitchPlaysOffline("irc.twitch.tv", 6667, "oauth:YOUR_OATH_CODE_HERE", "TwitchBot", "YOUR_CHANNEL_NAME_HERE", "YOUR_CHANNEL_NAME_HERE", voteingOptions)

get_votes(tPlays) 
printit()