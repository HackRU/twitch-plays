from flask import Flask, request, jsonify
import threading
import time

#dictonary of votes
votes = {
	"null": 0,
	"1": 0,
	"2": 0,
	"3": 0,
	"4": 0,
	"5": 0,
	"6": 0,
	"7": 0,
	"8": 0,
	"9": 0
	}

app = Flask(__name__)

@app.route('/')
def index():
	return "hello world"

@app.route('/test')
def test():
	return "test"

@app.route('/votes')
def checkVotes():
	majority = "1";


	#find most votes
	global votes
	for key in votes:
		if votes[key] > votes[majority]:
			majority = key

	#reset vote
	votes = {
		"null":0,
		"1": 0,
		"2": 0,
		"3": 0,
		"4": 0,
		"5": 0,
		"6": 0,
		"7": 0,
		"8": 0,
		"9": 0
		}
	return majority

#recieve game commands
@app.route('/1', methods=['POST'])
def vote_for_one():
	votes["1"] += 1
	return "voted for one"

@app.route('/2', methods=['POST'])
def vote_for_two():
	votes["2"] += 1
	return "voted for two"

@app.route('/3', methods=['POST'])
def vote_for_three():
	votes["3"] += 1
	return "voted for three"

@app.route('/4', methods=['POST'])
def vote_for_four():
	votes["4"] += 1
	return "voted for four"

@app.route('/5', methods=['POST'])
def vote_for_five():
	votes["5"] += 1
	return "voted for five"

@app.route('/6', methods=['POST'])
def vote_for_six():
	votes["6"] += 1
	return "voted for six"

@app.route('/7', methods=['POST'])
def vote_for_seven():
	votes["7"] += 1
	return "voted for seven"

@app.route('/8', methods=['POST'])
def vote_for_eight():
	votes["8"] += 1
	return "voted for eight"

@app.route('/9', methods=['POST'])
def vote_for_nine():
	votes["9"] += 1
	return "voted for nine"


if __name__ == "__main__":
    app.run()
    
