import numpy

# function that picks a either h or tails given their probability.
# USES NUMPY!
def pickPenny(h,t):
	number = numpy.random.uniform(0,1)
	pp = ""

	if number > h:
		pp = "t"
	else:
		pp = "h"
	return pp


# Class player to build a player
class Player:
	def __init__(self, h,t):
		self.h = h
		self.t = t
		self.move_list = []

	# picks a penny and appends the result to result list
	def pick_penny(self):
		penny = pickPenny(self.h,self.t)
		self.move_list.append(penny)
		return penny

	# update parameters of player 1 given the list of past moves of player 2
	def ht_update1(self, moves_list_other):
		count_h = 0
		count_t = 0
		for move in moves_list_other:
			if(move == "h"):
				count_h +=1
			else:
				count_t +=1
		self.h = float(count_h) / len(moves_list_other)
		self.t = float(count_t) / len(moves_list_other)

	# update parameters of player 2 given the list of past moves of player 1
	def ht_update2(self, moves_list_other):
		count_h = 0
		count_t = 0
		for move in moves_list_other:
			if(move == "h"):
				count_h +=1
			else:
				count_t +=1
		self.h = float(count_t) / len(moves_list_other)
		self.t = float(count_h) / len(moves_list_other)


# class game, 

class Game:
	def __init__(self,p1_h,p2_h):
		self.player1 = Player(p1_h,1-p1_h)
		self.player2 = Player(p2_h,1-p2_h)
		self.payoff1 = 0
		self.payoff2 = 0
		self.payoff1_list = []
		self.payoff2_list = []

		# plays a single round
	def play_round(self):
		penny1 = self.player1.pick_penny()
		penny2 = self.player2.pick_penny()
		print penny1
		print penny2

		if (penny1 == penny2):
			self.payoff1 += 1
			self.payoff2 -= 1
			self.payoff1_list.append(1)
			self.payoff2_list.append(-1)
		else:
			self.payoff2 += 1
			self.payoff1 -= 1
			self.payoff1_list.append(-1)
			self.payoff2_list.append(1)	

		self.player1.ht_update1(self.player2.move_list)
		self.player2.ht_update2(self.player1.move_list)

		return self.payoff1, self.payoff2		

	# plays game with n_rounds
	def play_game(self,n_rounds):
		for i in xrange(1,n_rounds+1):
			print "Round %i" % i
			po1, po2 = self.play_round()
			print "payoff 1 after %i rounds: %i" % (i,po1)
			print "payoff 2 after %i rounds: %i" % (i,po2)
			new_h1,new_t1 = self.player1.h,self.player1.t 
			new_h2,new_t2 = self.player2.h,self.player2.t
			print "Player 1 h,t prob: %f, %f" % (new_h1, new_t1)
			print "Player 2 h,t prob: %f, %f" % (new_h2, new_t2)

			self.player1.h = new_h1
			self.player1.t = new_t1
			self.player2.h = new_h2
			self.player2.t = new_t2


if __name__ == '__main__':
	#initial parameters for probability and number of rounds
	p1h = 0.5
	p2h = 0.5
	n_rounds = 20000
	game = Game(p1h,p2h)
	game.play_game(n_rounds)

