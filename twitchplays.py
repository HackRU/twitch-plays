import socket
import threading
import requests
from ahk import AHK

#Download Autohotkey at https://www.autohotkey.com/ and provide the address to
#AutoHotkey.exe below!
ahk = AHK(executable_path='C:/Program Files/AutoHotkey/AutoHotkey.exe')

SERVER = "irc.twitch.tv"
PORT = 6667

#Your OAUTH Code Here https://twitchapps.com/tmi/
PASS = "oauth:342unb3xh4k4ui5vms06ckdbqyu22b"

#What you'd like to name your bot
BOT = "TwitchBot"

#The channel you want to monitor
CHANNEL = "fungster"

#Your account
OWNER = "fungster"

message = ""
user = ""

irc = socket.socket()

irc.connect((SERVER, PORT))
irc.send((	"PASS " + PASS + "\n" +
			"NICK " + BOT + "\n" +
			"JOIN #" + CHANNEL + "\n").encode())

def gamecontrol():

	global message

	while True:

		if "play_1" == message.lower():
			x = requests.post('http://127.0.0.1:5000/1')
			message = ""

		if "play_2" == message.lower():
			x = requests.post('http://127.0.0.1:5000/2')
			message = ""

		if "play_3" == message.lower():
			x = requests.post('http://127.0.0.1:5000/3')
			message = ""

		if "play_4" == message.lower():
			x = requests.post('http://127.0.0.1:5000/4')
			message = ""

		if "play_5" == message.lower():
			x = requests.post('http://127.0.0.1:5000/5')
			message = ""

		if "play_6" == message.lower():
			x = requests.post('http://127.0.0.1:5000/6')
			message = ""

		if "play_7" == message.lower():
			x = requests.post('http://127.0.0.1:5000/7')
			message = ""

		if "play_8" == message.lower():
			x = requests.post('http://127.0.0.1:5000/8')
			message = ""

		if "play_9" == message.lower():
			x = requests.post('http://127.0.0.1:5000/9')
			message = ""

		if "reset" == message.lower():
			message = ""

def twitch():

	global user
	global message

	def joinchat():
		Loading = True
		while Loading:
			readbuffer_join = irc.recv(1024)
			readbuffer_join = readbuffer_join.decode()
			print(readbuffer_join)
			for line in readbuffer_join.split("\n")[0:-1]:
				print(line)
				Loading = loadingComplete(line)

	def loadingComplete(line):
		if("End of /NAMES list" in line):
			print("TwitchBot has joined " + CHANNEL + "'s Channel!")
			sendMessage(irc, "Hello World!")
			return False
		else:
			return True

	def sendMessage(irc, message):
		messageTemp = "PRIVMSG #" + CHANNEL + " :" + message
		irc.send((messageTemp + "\n").encode())

	def getUser(line):
		#global user
		colons = line.count(":")
		colonless = colons-1
		separate = line.split(":", colons)
		user = separate[colonless].split("!", 1)[0]
		return user

	def getMessage(line):
		#global message
		try:
			colons = line.count(":")
			message = (line.split(":", colons))[colons]
		except:
			message = ""
		return message

	def console(line):
		if "PRIVMSG" in line:
			return False
		else:
			return True

	joinchat()
	irc.send("CAP REQ :twitch.tv/tags\r\n".encode())
	while True:
		try:
			readbuffer = irc.recv(1024).decode()
		except:
			readbuffer = ""
		for line in readbuffer.split("\r\n"):
			if line == "":
				continue
			if "PING :tmi.twitch.tv" in line:
				print(line)
				msgg = "PONG :tmi.twitch.tv\r\n".encode()
				irc.send(msgg)
				print(msgg)
				continue
			else:
				try:
					user = getUser(line)
					message = getMessage(line)
					print(user + " : " + message)
				except Exception:
					pass

def main():
	if __name__ =='__main__':
		t1 = threading.Thread(target = twitch)
		t1.start()
		t2 = threading.Thread(target = gamecontrol)
		t2. start()
main()