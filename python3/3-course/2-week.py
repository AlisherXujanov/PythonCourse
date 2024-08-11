
nested = [['dog', 'cat', 'horse'], ['frog', 'turtle',
                                    'snake', 'gecko'], ['hamster', 'gerbil', 'rat', 'ferret']]
output = nested[1][2]
print(output)
# ==============================================================================================
# ==============================================================================================
# ==============================================================================================
# ==============================================================================================
lst = [['apple', 'orange', 'banana'], [5, 6, 7, 8, 9.9, 10],
       ['green', 'yellow', 'purple', 'red']]

# Test to see if 'yellow' is in the third list of lst. Save to variable ``yellow``
yellow = 'yellow' in lst[2]
print(yellow)

# Test to see if 4 is in the second list of lst. Save to variable ``four``
four = 4 in lst[1]
print(four)

# Test to see if 'orange' is in the first element of lst. Save to variable ``orange``
orange = 'orange' in lst[0]
print(orange)
# ==============================================================================================
# ==============================================================================================
# ==============================================================================================
# ==============================================================================================
L = [[5, 8, 7], ['hello', 'hi', 'hola'], [6.6, 1.54, 3.99], ['small', 'large']]

# Test if 'hola' is in the list L. Save to variable name test1
test1 = 'hola' in L
print(test1)
# Test if [5, 8, 7] is in the list L. Save to variable name test2
test2 = [5, 8, 7] in L
print(test2)
# Test if 6.6 is in the third element of list L. Save to variable name test3
test3 = 6.6 in L[2]
print(test3)
# ==============================================================================================
# ==============================================================================================
# ==============================================================================================
# ==============================================================================================
nested = {'data': ['finding', 23, ['exercises', 'hangout', 34]], 'window': ['part', 'whole', [], 'sum', ['math', 'calculus', 'algebra', 'geometry', 'statistics',
                                                                                                         ['physics', 'chemistry', 'biology']]]}

# Check to see if the string data is a key in nested, if it is, assign True to the variable data, otherwise assign False.
data = 'data' in nested

# Check to see if the integer 24 is in the value of the key data, if it is then assign to the variable twentyfour the value of True, otherwise False.
twentyfour = 24 in nested['data'] or 24 in nested['window']
print(twentyfour)

# Check to see that the string 'whole' is not in the value of the key window. If it's not, then assign to the variable whole the value of True, otherwise False.
li = nested['window']
whole = 'whole' not in li
print(whole)

# Check to see if the string 'physics' is a key in the dictionary nested. If it is, assign to the variable physics, the value of True, otherwise False.
physics = 'physics' in nested
print(physics)
# ==============================================================================================
# ==============================================================================================
# ==============================================================================================
# ==============================================================================================
nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19}, 'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22}, 'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}
london_gold=nested_d['London']['Great Britain']
print(london_gold)
# ==============================================================================================
# ==============================================================================================
# ==============================================================================================
# ==============================================================================================
sports = {'swimming': ['butterfly', 'breaststroke', 'backstroke', 'freestyle'], 'diving': ['springboard', 'platform', 'synchronized'],
          'track': ['sprint', 'distance', 'jumps', 'throws'], 'gymnastics': {'women': ['vault', 'floor', 'uneven bars', 'balance beam'],
                                                                             'men': ['vault', 'parallel bars', 'floor', 'rings']}}

# Assign the string 'backstroke' to the name v1
v1 = sports['swimming'][2]
print(v1)

# Assign the string 'platform' to the name v2
v2 = sports['diving'][1]
print(v2)

# Assign the list ['vault', 'floor', 'uneven bars', 'balance beam'] to the name v3
v3 = sports['gymnastics']['women']
print(v3)

# Assign the string 'rings' to the name v4
v4 = sports['gymnastics']['men'][3]
print(v4)
# ==============================================================================================
# ==============================================================================================
# ==============================================================================================
# ==============================================================================================
list__of_lists = [
    ['purple', 'mauve', 'blue'],
    ['red', 'maroon', 'blood orange', 'crimson'],
    ['sea green', 'cornflower', 'lavender', 'indigo'],
    ['yellow', 'amarillo', 'mac n cheese', 'golden rod']
]
thirds = []
for lists in list__of_lists:
    thirds.append(lists[2])
print(thirds)
# ==============================================================================================
# ==============================================================================================
# ==============================================================================================
# ==============================================================================================
athletes = [
    ['Phelps', 'Lochte', 'Schooling', 'Ledecky', 'Franklin'],
    ['Felix', 'Bolt', 'Gardner', 'Eaton'],
    ['Biles', 'Douglas', 'Hamm', 'Raisman', 'Mikulak', 'Dalton']]

t_athletes = []
others = []

# YOUR CODE HERE
for lists in athletes:
    for athlete in lists:
        if 't' in athlete:
            t_athletes.append(athlete)
        else:
            others.append(athlete)
print(t_athletes)
print(others)







