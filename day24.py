from sympy import var, Eq, solve

with open('day24_input.txt') as f:
    input = [[int(a) for a in x.replace(' @',',').split(', ')] for x in f.read().split('\n')]


# -------------------- part 1 --------------------
# solving linear equation system on paper and writing formulas for t1 and t2
# { px1 + vx1*t1 = px2 + vx2*t2 
# { py1 + vy1*t1 = py2 + vy2*t2 

good_range = (200000000000000, 400000000000000)
# good_range = (7, 27)
cnt = 0
for i in range(len(input)):
    for ii in range(i+1, len(input)):
        px1, py1, pz1, vx1, vy1, vz1 = input[i]
        px2, py2, pz2, vx2, vy2, vz2 = input[ii]      
        try:
            t2 = ( (py1-py2)/vy2 + vy1/vy2*( (px2-px1)/vx1 ) ) / (1 - (vy1*vx2)/(vy2*vx1))
            t1 = (px2-px1)/vx1 + vx2*t2/vx1
        except:
            continue
        x = px2 + vx2 * t2
        y = py2 + vy2 * t2
        if t2 >= 0 and t1 >= 0 and x >= good_range[0] and x <= good_range[1] and y >= good_range[0] and y <= good_range[1]:
            cnt += 1
print('Answer to part one is:',cnt)


# -------------------- part 2 --------------------
# we have 6 unknows for starting positon: px, py, pz, vx, vy, vz
# to draw line in 3d plain we need 3 points, this suggest that we will use 3 input lines
# each line introduce 3 equations and 1 additional unknown, we will end up with 6+3 = 3+3+3 unknowns and equations

for v in ['px','py','pz','vx','vy','vz','t1','t2','t3']:
    exec(f'{v}=var("{v}")')
equations = []

equations.append(Eq(eval("px + vx * t1"), eval("input[0][0] + input[0][3] * t1")))
equations.append(Eq(eval("py + vy * t1"), eval("input[0][1] + input[0][4] * t1")))
equations.append(Eq(eval("pz + vz * t1"), eval("input[0][2] + input[0][5] * t1")))

equations.append(Eq(eval("px + vx * t2"), eval("input[1][0] + input[1][3] * t2")))
equations.append(Eq(eval("py + vy * t2"), eval("input[1][1] + input[1][4] * t2")))
equations.append(Eq(eval("pz + vz * t2"), eval("input[1][2] + input[1][5] * t2")))

equations.append(Eq(eval("px + vx * t3"), eval("input[2][0] + input[2][3] * t3")))
equations.append(Eq(eval("py + vy * t3"), eval("input[2][1] + input[2][4] * t3")))
equations.append(Eq(eval("pz + vz * t3"), eval("input[2][2] + input[2][5] * t3")))

answer = solve(equations)[0]
print('Answer to part two is:',answer[px] + answer[py] + answer[pz])