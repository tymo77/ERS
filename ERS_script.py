import random
import itertools
import csv
import datetime
import os
import rank
"""
player_no is like a players' name
player_index of the player order gives the player in that position. it is a position indicator.
"""

def set_order(number_of_players):
	player_order=list(range(number_of_players))
	random.shuffle(player_order)
	return(player_order)
	
def deal(player_order,number_of_decks):
	number_of_players=len(player_order)
	suits = 'cdhs' #initilaize suits
	ranks = '23456789TJQKA'#initialize card ranks
	dealer_cards=[]

	for deck_no in range(number_of_decks): #for each hand in the array of how many cards are dealt at each turn
		deck=list(''.join(card) for card in itertools.product(ranks, suits))
		random.shuffle(deck)
		dealer_cards=dealer_cards+deck

	#players start empty handed
	player_hands=[]
	for player in range(number_of_players):
		player_hands.append([])

	#deal hands to each player
	player_index=0
	for card in dealer_cards:
		player_index=player_index%number_of_players
		player_hands[player_order[player_index]].append(card)
		player_index+=1
	return (player_hands)

def count_players(player_hands):
	num_ingame=0
	for hand in player_hands:
		if len(hand)>0:
			num_ingame+=1
	return(num_ingame)

def test_face(card):
	if card[0]=="A" or card[0]=="K" or card[0]=="Q" or card[0]=="J":
		if card[0]=="A":
			return(4)
		if card[0]=="K":
			return(3)
		if card[0]=="Q":
			return(2)
		if card[0]=="J":
			return(1)
	else:
		return(0)
		
def play_game(number_of_players,number_of_decks):
	#set the order and deal cards
	order=set_order(number_of_players)
	hands=deal(order,number_of_decks)
	
	players_left=number_of_players
	turn=0
	player_turn=0
	stack=[]
	challenge=False
	
	while players_left>1:
		#run the game until we have one person left
		
		#PLAY CARD
		while len(hands[order[player_turn]])==0:
			#if there are no cards in the players' hand, skip to the next player
			player_turn+=1
			player_turn=player_turn%number_of_players
		stack.insert(0,hands[order[player_turn]].pop(0))
		
		#TEST FACE
		if test_face(stack[0])>0:
			challenge=True
			countdown=test_face(stack[0])
			player_turn+=1
			player_turn=player_turn%number_of_players
		else:
			#TEST CHALLENGE
			if challenge:
				#TEST LOST CHALLENGE
				if countdown>0:
					player_turn+=0
					player_turn=player_turn%number_of_players
					countdown-=1
				else:
					challenge=False
					player_turn-=1
					player_turn=player_turn%number_of_players
					stack.reverse()
					hands[order[player_turn]].extend(stack)
					stack.clear()
			else:
				player_turn+=1
				player_turn=player_turn%number_of_players
		
		#CALC PLAYERS LEFT and INCREMENT TURN
		players_left=count_players(hands)#check players left
		turn+=1#update loop variable	
		
		#END OF LOOP
		if turn>10000:
			print("TOO MANY TURNS")
			break#combat infinte loop
	return([hands,stack])