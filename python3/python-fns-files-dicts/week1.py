# Files and CSV

# The textfile, assets/travel_plans.txt, contains the summer travel plans for someone with some commentary. Find the total number of characters in the file and save to the variable num.

num = 0
with open('assets/travel_plans.txt') as file:
    for line in file:
        num += len(line)
print(num)

# Sometimes, as in the next cell, we will show you one or more test cases, in the form of assert statements. Make sure your code pass those tests before you click the "Submit Assignment" button.

# When you click the "Submit Assignment" button, there may be additional, hidden tests that are run. If you fail one of those tests, you will get feedback and can resubmit, as many times as you want, until you get them all right.

# But it takes a little while for the auto grader to run. You will find it is faster, less frustrating, and more educational if you create additional tests of your own, either with assert statements or just print statements. That will give you a faster feedback-and -fix cycle; and formulating those tests will help you really understand what's going on.

assert num == 316, 'num is not assigned the correct value'

# We have provided a file called `assets/emotion_words.txt` that contains lines of words that describe emotions. Find the total number of words in the file and assign this value to the variable `num_words`.


num_words = 0
with open('assets/emotion_words.txt') as file:
    for line in file:
        num_words += len(line.split())
print(num_words)

assert num_words == 48, 'num_words is not assigned the correct value'

# Assign to the variable `num_lines` the number of lines in the file `assets/school_prompt.txt`.

# **Note: different file than the previous question!**
num_lines = 0
with open('assets/school_prompt.txt') as file:
    for line in file:
        num_lines += 1
print(num_lines)

assert num_lines == 10, 'num_lines is not assigned the correct value'

# Assign the first 30 characters of `assets/school_prompt.txt` as a string to the variable `beginning_chars`.

beginning_chars = None

with open('assets/school_prompt.txt') as file:
    beginning_chars = file.read()[:30]
print(beginning_chars)

assert type(beginning_chars) == str, 'beginning_chars is not a string'
assert len(
    beginning_chars) == 30, 'beginning_chars is not assigned the correct length'

school = open("assets/school_prompt.txt", "r")
lines = school.readlines()
three = []
for line in lines[0:]:
    val = line.split(" ")
    three.append(val[2])
print(three)

three = []

with open('assets/school_prompt.txt') as file:
    for line in file:
        three.append(line.strip())

print(three)



assert type(three) == list, 'three is not a list'
assert len(three) == 10, 'three is not assigned the correct length'

# **Challenge: ** Create a list called `emotions` that contains the first word of every line in `assets/emotion_words.txt`.

emotions = None

with open('assets/emotion_words.txt') as file:
    emotions = [line.split()[0] for line in file]
print(emotions)


assert type(emotions) == list, 'emotions is not a list'
assert len(emotions) == 7, 'emotions is not assigned the correct length'

# Assign the first 33 characters from the textfile, `assets/travel_plans.txt` to the variable `first_chars`.

first_chars = None

with open('assets/travel_plans.txt') as file:
    first_chars = file.read()[:33]
print(first_chars)


assert type(first_chars) == str, 'first_chars is not a string'
assert len(first_chars) == 33, 'first_chars is not assigned the correct length'

# **Challenge: ** Using the file `assets/school_prompt.txt`, if the character ‘p’ is in a word, then add the word to a list called `p_words`.


p_words = None

with open('assets/school_prompt.txt') as file:
    p_words = [word for line in file for word in line.split() if 'p' in word]
print(p_words)

assert type(p_words) == list, 'p_words is not a list'
assert len(p_words) == 5, 'p_words is not assigned the correct length'
