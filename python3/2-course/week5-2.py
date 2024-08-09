# TASK-1

# We have provided some synthetic(fake, semi-randomly generated) twitter data in a csv file named project_twitter_data.csv which has the
# text of a tweet, the number of retweets of that tweet, and the number of replies to that tweet. We have also words that express positive
# sentiment and negative sentiment, in the files positive_words.txt and negative_words.txt.

# Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is . You will create a csv file,
# which contains columns for the Number of Retweets, Number of Replies, Positive Score(which is how many happy words are in the tweet),
# Negative Score(which is how many angry words are in the tweet), and the Net Score for each tweet. At the end, you upload the csv file to
# Excel or Google Sheets, and produce a graph of the Net Score vs Number of Retweets.

# To start, define a function called strip_punctuation which takes one parameter, a string which represents a word, and removes
# characters considered punctuation from everywhere in the word. (Hint: remember the .replace() method for strings.)

# SOLUTION:
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(string):
    for char in string:
        if char in punctuation_chars:
            string = string.replace(char, '')
    print(string)
    return (string)

# =================================================================================
# =================================================================================
# TASK-2
# Next, copy in your strip_punctuation function and define a function called get_pos which takes one parameter, a string which represents
# one or more sentences, and calculates how many words in the string are considered positive words. Use the list, positive_words to
# determine what words will count as positive. The function should return a positive integer - how many occurrences there are of positive
# words in the text. Note that all of the words in positive_words are lower cased, so you’ll need to convert all the words in the input
# string to lower case as well.


# SOLUTION:
positive_words = []
with open("assets/positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


def strip_punctuation(string):
    for char in string:
        if char in punctuation_chars:
            string = string.replace(char, '')
    return (string)


def get_pos(sentence):
    sentence = sentence.lower()
    sent_list = sentence.split(" ")
    count = 0
    for word in sent_list:
        word = strip_punctuation(word)
        if word in positive_words:
            count += 1
    return count

# =================================================================================
# =================================================================================
# TASK-3
# Next, copy in your strip_punctuation function and define a function called get_neg which takes one parameter, a string which represents
# one or more sentences, and calculates how many words in the string are considered negative words. Use the list, negative_words to
# determine what words will count as negative. The function should return a positive integer - how many occurrences there are of negative
# words in the text. Note that all of the words in negative_words are lower cased, so you’ll need to convert all the words in the input
# string to lower case as well.


# SOLUTION:
negative_words = []
with open("assets/negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


def strip_punctuation(string):
    for char in string:
        if char in punctuation_chars:
            string = string.replace(char, '')
    return (string)


def get_neg(sentence):
    sentence = sentence.lower()
    sent_list = sentence.split(" ")
    count = 0
    for word in sent_list:
        word = strip_punctuation(word)
        if word in negative_words:
            count += 1
    return count
# =================================================================================
# =================================================================================
# TASK-4
# Finally, copy in your previous functions and write code that opens the file project_twitter_data.csv which has the fake generated
# twitter data(the text of a tweet, the number of retweets of that tweet, and the number of replies to that tweet). Your task is to build
# a sentiment classifier, which will detect how positive or negative each tweet is . Copy the code from the code windows above, and put
# that in the top of this code window. Now, you will write code to create a csv file called resulting_data.csv, which contains the Number
# of Retweets, Number of Replies, Positive Score(which is how many happy words are in the tweet), Negative Score(which is how many angry
#                                                                                                                words are in the tweet), and the Net Score(how positive or negative the text is overall) for each tweet. The file should have those
# headers in that order. Remember that there is another component to this project. You will upload the csv file to Excel or Google Sheets
# and produce a graph of the Net Score vs Number of Retweets. Check Coursera for that portion of the assignment, if you’re accessing this
# textbook from Coursera.


# SOLUTION:
# lists of words to use
positive_words = []
with open("assets/positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("assets/negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


def strip_punctuation(string):
    for char in string:
        if char in punctuation_chars:
            string = string.replace(char, '')
    return (string)


def get_neg(sentence):
    sentence = sentence.lower()
    sent_list = sentence.split(" ")
    count = 0
    for word in sent_list:
        word = strip_punctuation(word)
        if word in negative_words:
            count += 1
    return count


def get_pos(sentence):
    sentence = sentence.lower()
    sent_list = sentence.split(" ")
    count = 0
    for word in sent_list:
        word = strip_punctuation(word)
        if word in positive_words:
            count += 1
    return count


tweet_file = open('project_twitter_data.csv', 'r')
final_li = []

for tw in tweet_file.readlines()[1:]:
    new_sen = [1, 1, 1, 1, 1]
    li = tw.split(',')
    # print(li)
    new_sen[0] = int(li[1])
    string = li[2]
    new_sen[1] = int(string[:-1])
    new_sen[2] = get_pos(li[0])
    new_sen[3] = get_neg(li[0])
    new_sen[4] = new_sen[2]-new_sen[3]
    final_li.append(new_sen)
tweet_file.close()

x = [ele[4] for ele in final_li]
y = [ele[0] for ele in final_li]
print(x)
print(y)
filename = 'resulting_data.csv'
outfile = open(filename, "w")
outfile.write(
    'Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
outfile.write('\n')
for result in final_li:
    row_string = '{},{},{},{},{}'.format(
        result[0], result[1], result[2], result[3], result[4])
    outfile.write(row_string + "\n")
