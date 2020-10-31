import threading
from twitchPlays import twitchPlaysOnline
playerChoice = None

def getVotes(obj):
	print("I am getting voteResults")
	threading.Timer(10.0, getVotes, args=[obj]).start()
	global playerChoice
	playerChoice = obj.voteResults()

def printit():
	threading.Timer(5.0, printit).start()
	print("this is the playerChoice: ", playerChoice)


temp = ["1","2","3","hi","bye"]
tPlays = twitchPlaysOnline("irc.twitch.tv", 6667, "oauth:342unb3xh4k4ui5vms06ckdbqyu22b", "TwitchBot", "fungster", "fungster", temp)

getVotes(tPlays)
printit()