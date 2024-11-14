fruits = ['apple', 'mango', 'cherry', 'banana', 'berry', 'pineapple']


vs = "aiuoe"
r = [f for f in fruits if f[0] in vs and f[-1] in vs]


r2 = [f for f in fruits if len([l for l in f if l in vs]) > 2]




