import pandas as pd

# import the input data
with open('day1_input.txt') as f:
    input = [x.rstrip('\n') for x in f.readlines()]

# ---------- part 1 ----------
# keep and add together last and first digit
two_digits = [int(x[0] + x[-1]) for x in [''.join(i for i in x if i.isdigit()) for x in input]]
answer1 = sum(two_digits)
print("Answer to first part is {}".format(answer1))

# ---------- part 2 ----------
# adding number and word of a digit not to mess up other replacements
# this will change the initial string but we are only interested in last and first digit, not the particular text
# example replacement:
# sevenine -> seven7sevenine -> seven7sevenine9nine

replacement = {'one': 'one1one',
               'two': 'two2two',
               'three': 'three3three',
               'four': 'four4four',
               'five': 'five5five',
               'six': 'six6six',
               'seven': 'seven7seven',
               'eight': 'eight8eight',
               'nine': 'nine9nine'}
    
df = pd.DataFrame(input)
df.columns = ['line']
df['replaced'] = df['line'].replace(replacement, regex=True)
df['left_digit'] = df['replaced'].str.replace('\D+', '', regex=True).str[0]
df['right_digit'] = df['replaced'].str.replace('\D+', '', regex=True).str[-1]
df['final'] = df['left_digit'] + df['right_digit']

answer2 = sum([int(x) for x in df['final'].tolist()])
print("Answer to 2nd part is {}".format(answer2))