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
    max_reps = max([v for k,v in hand.items()])

    if len(hand) == 1:
        # five of a kind
        return 7
    if len(hand) == 2:
        if max_reps == 4:
            # four of a kind
            return 6
        else:
            # full house
            return 5
    if len(hand) == 3:
        if max_reps == 3:
            # three of a kind
            return 4
        else:
            # two pair
            return 3
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
            to_return += '11'
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