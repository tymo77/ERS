def rank_card(card):
	if card[0]=="A":
		score=13
	elif card[0]=="K":
		score=12
	elif card[0]=="Q":
		score=11
	elif card[0]=="J":
		score=10
	elif card[0]=="T":
		score=9
	elif card[0]=="9":
		score=8
	elif card[0]=="8":
		score=7
	elif card[0]=="7":
		score=6
	elif card[0]=="6":
		score=5
	elif card[0]=="5":
		score=4
	elif card[0]=="4":
		score=3
	elif card[0]=="3":
		score=2
	elif card[0]=="2":
		score=1
	else:
		score=0
	return score

def rank_cards(cards_list):
	cards_rank_list=[]
	cards_list=list(cards_list)
	for card in cards_list:
		cards_rank_list.append(rank_card(card))
	return cards_rank_list

def max_card(cards_list):
	"""the cards_list is unordered. convert it to an array and run using array methods"""
	cards_array=[]
	for card in cards_list:
		cards_array.append(card)
	rank_list=rank_cards(cards_array)
	max_card=cards_array[rank_list.index(max(rank_list))]
	
	return max_card

def min_card(cards_list):
	"""the cards_list is unordered. convert it to an array and run using array methods"""
	cards_array=[]#initialize the array of cards
	for card in cards_list: #for each card in the cards dictionary values, append the card to the cards array, then rank the cards, then get the minimum
		cards_array.append(card)
	rank_list=rank_cards(cards_array)
	min_card=cards_array[rank_list.index(min(rank_list))]
	return min_card