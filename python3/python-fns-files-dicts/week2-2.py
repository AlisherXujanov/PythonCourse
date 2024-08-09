# Question: 1
# The dictionary Junior shows a schedule for a junior year semester. The key is the course name and the value is the number of credits.
# Find the total number of credits taken this semester and assign it to the variable credits. Do not hardcode this – use dictionary
# accumulation!
# Solution:

Junior = {'SI 206': 4, 'SI 310': 4, 'BL 300': 3,
          'TO 313': 3, 'BCOM 350': 1, 'MO 300': 3}
credits = 0
for key in Junior:
    credits += Junior[key]
print(credits) // 18

# Question: 2
# Create a dictionary, freq, that displays each character in string str1 as the key and its frequency as the value.
# Solution:

str1 = "peter piper picked a peck of pickled peppers"
freq = {}
for key in str1:
    if key not in freq:
        freq[key] = 0
    freq[key] += 1
print(freq) // {'p': 9, 'e': 8, 't': 1, 'r': 3, ' ': 7, 'i': 3,
                'c': 3, 'k': 3, 'd': 2, 'a': 1, 'o': 1, 'f': 1, 'l': 1, 's': 1}


# Question: 3
# Provided is a string saved to the variable name s1. Create a dictionary named counts that contains each letter in s1 and the number of
# times it occurs.
# Solution:

s1 = "hello"
counts = {}
for key in s1:
    if key not in counts:
        counts[key] = 0
    counts[key] += 1
print(counts) // {'e': 1, 'o': 1, 'l': 2, 'h': 1}


# Question: 4
# Create a dictionary, freq_words, that contains each word in string str1 as the key and its frequency as the value.
# Solution:

str1 = "I wish I wish with all my heart to fly with dragons in a land apart"
lst = str1.split()
freq_words = {}
for key in lst:
    if key not in freq_words:
        freq_words[key] = 0
    freq_words[key] += 1
print(freq_words) // {'I': 2, 'wish': 2, 'with': 2, 'all': 1, 'my': 1, 'heart': 1, 'to': 1, 'fly': 1, 'dragons': 1, 'in': 1, 'a': 1,
                      'land': 1, 'apart': 1}


# Question: 5
# Create a dictionary called wrd_d from the string sent, so that the key is a word and the value is how many times you have seen that word.
# Solution:

sent = "Singing in the rain and playing in the rain are two entirely different situations but both can be good"
lst = sent.split()
wrd_d = {}
for key in lst:
    if key not in wrd_d:
        wrd_d[key] = 0
    wrd_d[key] += 1
print(wrd_d) // {'in': 2, 'Singing': 1, 'the': 2, 'rain': 2, 'and': 1, 'playing': 1, 'are': 1, 'two': 1, 'entirely': 1, 'different': 1,
                 'situations': 1, 'but': 1, 'both': 1, 'can': 1, 'be': 1, 'good': 1}


# Question: 6
# Create the dictionary characters that shows each character from the string sally and its frequency. Then, find the most frequent letter
# based on the dictionary. Assign this letter to the variable best_char.
# Solution:

sally = "sally sells sea shells by the sea shore"
characters = {}
for key in sally:
    if key not in characters:
        characters[key] = 0
    characters[key] += 1
best_char = max(characters, key=lambda x: characters[x])
print(characters) // {'a': 3, 's': 8, 'l': 6, 'y': 2,
                      ' ': 7, 'e': 6, 'h': 3, 'b': 1, 't': 1, 'o': 1, 'r': 1}


# Question: 7
# Find the least frequent letter. Create the dictionary characters that shows each character from string sally and its frequency. Then,
# find the least frequent letter in the string and assign the letter to the variable worst_char.
# Solution:

sally = "sally sells sea shells by the sea shore and by the road"
characters = {}
for key in sally:
    if key not in characters:
        characters[key] = 0
    characters[key] += 1
worst_char = min(characters, key=lambda x: characters[x])
print(characters) // {'a': 5, 's': 8, 'l': 6, 'y': 3, ' ': 11,
                      'e': 7, 'h': 4, 'b': 2, 't': 2, 'o': 2, 'r': 2, 'n': 1, 'd': 2}


# Question: 8
# Create a dictionary named letter_counts that contains each letter and the number of times it occurs in string1. Challenge: Letters should
# not be counted separately as upper-case and lower-case. Intead, all of them should be counted as lower-case.
# Solution:

string1 = "There is a tide in the affairs of men, Which taken at the flood, leads on to fortune. Omitted, all the voyage of their life is bound in shallows and in miseries. On such a full sea are we now afloat. And we must take the current when it serves, or lose our ventures."
string1 = string1.lower()
letter_counts = {}
for key in string1:
    if key not in letter_counts:
        letter_counts[key] = 0
    letter_counts[key] += 1
print(letter_counts) // {'a': 17, 's': 15, 'l': 11, 'y': 1, ' ': 53, 'e': 29, 'h': 11, 'b': 1, 't': 19, 'o': 17, 'r': 12, 'n': 15,
                         'd': 7, 'i': 14, 'f': 9, 'm': 4, ',': 4, 'w': 6, 'c': 3, 'k': 2, 'u': 8, '.': 4, 'v': 3, 'g': 1}

# Question: 9
# Create a dictionary called low_d that keeps track of all the characters in the string p and notes how many times each character was seen.
# Make sure that there are no repeats of characters as keys, such that “T” and “t” are both seen as a “t” for example.
# Solution:

p = "Summer is a great time to go outside. You have to be careful of the sun though because of the heat."
p = p.lower()
low_d = {}
for key in p:
    if key not in low_d:
        low_d[key] = 0
    low_d[key] += 1
print(low_d) // {'a': 6, 's': 5, 'l': 1, 'y': 1, ' ': 20, 'e': 12, 'h': 6, 'b': 2, 't': 9, 'o': 8, 'r': 3, 'n': 1, 'd': 1, 'i': 3,
                 'f': 3, 'm': 3, 'c': 2, 'u': 7, '.': 2, 'v': 1, 'g': 3}
