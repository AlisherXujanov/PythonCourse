# The textfile, assets/travel_plans.txt, contains the summer travel plans for someone with some commentary. Find the total number of characters in the file and save to the variable num.
num = None
# YOUR CODE HERE
with open("assets/travel_plans.txt") as file:
    num = len(file.read())
    
print(num)
# ========================================================================================================
# ========================================================================================================
# We have provided a file called `assets/emotion_words.txt` that contains lines of words that describe emotions. Find the total number of words in the file and assign this value to the variable `num_words`.
num_words = None

# YOUR CODE HERE
with open("assets/emotion_words.txt") as file:
    num_words = len(file.read().split())
    
print(num_words)
# ========================================================================================================
# ========================================================================================================
# Assign to the variable `num_lines` the number of lines in the file `assets/school_prompt.txt`.
# **Note: different file than the previous question!**
num_lines = None

# YOUR CODE HERE
with open("assets/school_prompt.txt") as file:
    num_lines = len(file.readlines())
    
print(num_lines)
# ========================================================================================================
# ========================================================================================================
# Assign the first 30 characters of `assets/school_prompt.txt` as a string to the variable `beginning_chars`.
beginning_chars = None

# YOUR CODE HERE
with open("assets/school_prompt.txt") as file:
    beginning_chars = file.read()[:30]
# ========================================================================================================
# ========================================================================================================
# **Challenge:** Using the file `assets/school_prompt.txt`, assign the third word of every line to a list called `three`.
three = None

# YOUR CODE HERE
with open("assets/school_prompt.txt") as file:
    three = [line.split()[2] for line in file.readlines()]
    
# ========================================================================================================
# ========================================================================================================
# **Challenge: ** Create a list called `emotions` that contains the first word of every line in `assets/emotion_words.txt`.
emotions = None

# YOUR CODE HERE
with open("assets/emotion_words.txt") as file:
    emotions = [line.split()[0] for line in file.readlines()]

print(emotions)

# ========================================================================================================
# ========================================================================================================
# Assign the first 33 characters from the textfile, `assets/travel_plans.txt` to the variable `first_chars`.
first_chars = None

# YOUR CODE HERE
with open("assets/travel_plans.txt") as file:
    first_chars = file.read()[:33]
    
# ========================================================================================================
# ========================================================================================================
# **Challenge: ** Using the file `assets/school_prompt.txt`, if the character ‘p’ is in a word, then add the word to a list called `p_words`.

p_words = None

# YOUR CODE HERE
with open("assets/school_prompt.txt") as file:
    p_words = [word for line in file.readlines() for word in line.split() if "p" in word]
