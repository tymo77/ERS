import random
import itertools
import csv
import datetime
import os
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