import socket
import threading
import requests

votes = {"null": 0}

class twitchPlaysOffline:
	def __init__(self, SERVER, PORT, PASS, BOT, CHANNEL, OWNER, OPTIONS = []):
		self.SERVER = SERVER
		self.PORT = PORT
		self.PASS = PASS
		self.BOT = BOT
		self.CHANNEL = CHANNEL
		self.OWNER = OWNER

		self.message = ""
		user = ""

		for key in OPTIONS:
			if key not in votes.keys():
				votes[key] = 0
				print(key + " : " + str(votes[key]))

		def gamecontrol():

			self.message

			while True:

				for key in votes:
					if ("play_" + key) == self.message.lower():
						votes[key] += 1
						print("voted for " + key)
						self.message = ""

					if "check" == self.message.lower():
						print(self.voteResults())
						self.message = ""

		def twitch():
			while True:
				self.message = input()

		def start():
			t1 = threading.Thread(target = twitch)
			t1.start()
			t2 = threading.Thread(target = gamecontrol)
			t2. start()	

		start()

	def voteResults(self):
		majority = "null"

		for key in votes:
			if votes[key] > votes[majority]:
				majority = key
			votes[key] = 0

		if majority == "null":
			return None

		return majority	