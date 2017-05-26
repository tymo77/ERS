def rank_card(card):
	if card[0]=="A":
		rank=13
	if card[0]=="K":
		rank=12
	if card[0]=="Q":
		rank=11
	if card[0]=="J":
		rank=10
	if card[0]=="T":
		rank=9
	if card[0]=="9":
		rank=8
	if card[0]=="8":
		rank=7
	if card[0]=="7":
		rank=6
	if card[0]=="6":
		rank=5
	if card[0]=="5":
		rank=4
	if card[0]=="4":
		rank=3
	if card[0]=="3":
		rank=2
	if card[0]=="2":
		rank=1
return rank

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