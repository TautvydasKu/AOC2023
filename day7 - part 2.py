# import the input data
with open('day7_input.txt') as f:
    input = [x.rstrip('\n').split() for x in f.readlines()]
    
    
# function to count repetitions of a card in hand
def countRep(hand):
    counts = dict()
    for card in set(hand):
        count_r = 0
        for val in hand:
            if val == card:
                count_r += 1
        counts[card] = count_r
    return counts


# counting hand type
def getType(hand):
    # removing jacks from hands
    hand.pop('J', None)
    
    if hand == {}:
        return 7
    
    sum_reps = sum([v for k,v in hand.items()])
    min_reps = min([v for k,v in hand.items()])
    max_reps = max([v for k,v in hand.items()])

    if len(hand) == 1:
        # five of the kind
        return 7
    if len(hand) == 2:
        if min_reps == 1:
            # four of the kind
            return 6
        else:
            # full house
            return 5
    if len(hand) == 3:
        if sum_reps == 5 and max_reps < 3:
            # two pair
            return 3
        else:
            # three of the kind
            return 4
    if len(hand) == 4:
        # one pair
        return 2
    else:    
        # high card
        return 1


# function to get 10 digit string strength of hand
def getValue(hand):
    to_return = ''
    for c in hand:
        if c == 'A':
            to_return += '14'
        elif c == 'K':
            to_return += '13'
        elif c == 'Q':
            to_return += '12'
        elif c == 'J':
            to_return += '01'
        elif c == 'T':
            to_return += '10'
        else:
            to_return += '0' + c
    return to_return


# function for sorting by 3rd column
def takeValue(elem):
    return elem[2]
        
# evaluate hand strengths and sort them
cards = [[x, y, str(getType(countRep(x))) + getValue(x)] for x, y in input]
cards.sort(key=takeValue)
answer1 = sum([x * int(y[1]) for x, y in list(enumerate(cards, 1))])

print(answer1)