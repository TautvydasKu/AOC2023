"""
Time:        59     79     65     75
Distance:   597   1234   1032   1328
"""
# define input data
input = [[59, 597], [79, 1234], [65, 1032], [75, 1328]]
input2 = [59796575, 597123410321328]

# calculate each race by bruteforcing
def race(time, distance):
    wins = 0
    for i in range(1, time + 1):
        if i * (time-i) > distance:
            wins += 1
    return wins

results = [race(x, y) for x, y in input]

print("Answer to part one is: {}". format(results[0] * results[1] * results[2] * results[3]))
print("Answer to part two is: {}". format(race(input2[0], input2[1])))


# ------------ revisit -------------
import math

# calculate race results by solving quadratic equation
# -x^2 + time * x - distance > 0
# x^2 - time * x + distance < 0
def race2(time, distance):
    x1 = (time - math.sqrt(time ** 2 - 4 * distance))/2
    x2 = (time + math.sqrt(time ** 2 - 4 * distance))/2
    return math.floor(x2) - math.floor(x1)

results = [race2(x, y) for x, y in input]

print("Answer to part one is: {}". format(results[0] * results[1] * results[2] * results[3]))
print("Answer to part two is: {}". format(race2(input2[0], input2[1])))
