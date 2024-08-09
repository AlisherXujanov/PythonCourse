# 1. Yes
# 2. No
# ======================================================================
# ======================================================================
# 1. I
# 2. D. .index()
# 3. C. .append()
# --------------
# 4. Write code to add ‘horseback riding’ to the third position (i.e., right before volleyball) in the list sports.
sports = ['cricket', 'football', 'volleyball', 'baseball',
          'softball', 'track and field', 'curling', 'ping pong', 'hockey']

sports.insert(2, "horseback riding")
# --------------
# 5. Write code to take ‘London’ out of the list trav_dest.
trav_dest = ['Beirut', 'Milan', 'Pittsburgh', 'Buenos Aires',
             'Nairobi', 'Kathmandu', 'Osaka', 'London', 'Melbourne']

trav_dest.remove("London")
# --------------
# 6. Write code to add ‘Guadalajara’ to the end of the list trav_dest using a list method.
trav_dest = ['Beirut', 'Milan', 'Pittsburgh', 'Buenos Aires',
             'Nairobi', 'Kathmandu', 'Osaka', 'Melbourne']

trav_dest.append("Guadalajara")
# --------------
# 7. D. IV.
# --------------
# 8. A. I.
# --------------

# ======================================================================
# ======================================================================
# 1. D. c
# 2. A. cawdra
# 3. A. item
# 4. phrase
# --------------
# 5. Currently there is a string called str1. Write code to create a list called chars which should contain the characters from str1. Each character in str1 should be its own element in the list chars.
str1 = "I love python"
# HINT: what's the accumulator? That should go here.
chars = []
for i in str1:
    chars.append(i)
# ======================================================================
# ======================================================================
# 1. ["holiday", "celebrate!", "company"]
# 2. C. III.
# 3. D. 4.
# ----------
# 4. 
#   - C. total
#   - D. accum
# ----------
# 5. 
#   - A. item
#   - C. elem
#   - D. char
# ----------
# 6. 
#   - A. num_lst
#   - C. sentence
#   - D. names
# ----------
# 7. D. accumulator variable: total | iterator variable: sentence |sequence variable: sentence_lst
# ----------
# 8. For each character in the string saved in ael, append that character to a list that should be saved in a variable app.
ael = "python!"

app = []
for i in ael:
    app.append(i)
# -----------
# 9. For each string in wrds, add ‘ed’ to the end of the word (to make the word past tense). Save these past tense words to a list called past_wrds.
wrds = ["end", 'work', "play", "start", "walk",
        "look", "open", "rain", "learn", "clean"]

past_wrds = []
for i in wrds:
    past_wrds.append(i + "ed")
# ======================================================================
# ======================================================================

# 1. Below are a set of scores that students have received in the past semester. Write code to determine how many are 90 or above and assign that result to the value a_scores.
scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"

scores = scores.split()
a_scores = 0
for i in scores:
    if int(i) >= 90:
        a_scores += 1
# -------------- -------------- -------------- --------------
# 2. Write code that uses the string stored in org and creates an acronym which is assigned to the variable acro. Only the first letter of each word should be used, each letter in the acronym should be a capital letter, and there should be nothing to separate the letters of the acronym. Words that should not be included in the acronym are stored in the list stopwords. For example, if org was assigned the string “hello to world” then the resulting acronym should be “HW”.

stopwords = ['to', 'a', 'for', 'by', 'an',
             'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"
 
acro = ""
org = org.split()
for i in org:
    if i not in stopwords:
        acro += i[0].upper()
# -------------- -------------- -------------- --------------
# 3. Write code that uses the string stored in sent and creates an acronym which is assigned to the variable acro. The first two letters of each word should be used, each letter in the acronym should be a capital letter, and each element of the acronym should be separated by a “. “ (dot and space). Words that should not be included in the acronym are stored in the list stopwords. For example, if sent was assigned the string “height and ewok wonder” then the resulting acronym should be “HE. EW. WO”.
stopwords = ['to', 'a', 'for', 'by', 'an',
             'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"

acro = ""
sent = sent.split()
for i in sent:
    if i not in stopwords:
        acro += i[0].upper() + i[1].upper() + ". "
        
acro = acro[:-2]
# -------------- -------------- -------------- --------------
# 4. A palindrome is a phrase that, if reversed, would read the exact same. Write code that checks if p_phrase is a palindrome by reversing it and then checking if the reversed version is equal to the original. Assign the reversed version of p_phrase to the variable r_phrase so that we can check your work.

p_phrase = "was it a car or a cat I saw"

r_phrase = p_phrase[::-1]
# -------------- -------------- -------------- --------------
# 5. Provided is a list of data about a store’s inventory where each item in the list represents the name of an item, how much is in stock, and how much it costs. Print out each item in the list with the same formatting, using the .format method (not string concatenation). For example, the first print statment should read The store has 12 shoes, each for 29.99 USD.

inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99",
             "sweatpants, 25, 15.00", "scarves, 13, 7.75"]

for i in inventory:
    i = i.split(", ")
    print("The store has {} {}, each for {} USD.".format(i[1], i[0], i[2]))



