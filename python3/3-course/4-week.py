# This project will take you through the process of mashing up data from two different APIs.

# [The OMDb API](https: // www.omdbapi.com /) lets you provide a movie title as a query input and get back data about the movie, including scores from various review sites(Rotten Tomatoes, IMDb, etc.).

# [icanhazdadjokes.com](https: // icanhazdadjoke.com /) returns random dad jokes containing a search string that you specify in your query.

# The end result of this project will be a function that takes in a movie title as input and produces a formatted text string that includes a couple dad jokes related to a word from the movie's plot.

# For example, here are a couple of sample outputs:

# ---

# ```
# Baby Mama
# Rotten Tomatoes rating: 63%
# A successful, single businesswoman who dreams of having a baby discovers she is infertile and hires a **working** class woman to be her unlikely surrogate.
# Speaking of **working**, that reminds me of some jokes.
# Hope they're better than the movie!

# Want to hear a joke about construction? Nah, I'm still **working** on it.
# Why doesn't the Chimney-Sweep call out sick from work? Because he's used to **working** with a flue.
# ```

# ---

# ```
# Back to the Future
# Rotten Tomatoes rating: 93%
# Marty McFly, a 17-year-old high school student, is **accidentally** sent 30 years into the past in a time-traveling DeLorean invented by his close friend, the maverick scientist Doc Brown.
# Speaking of **accidentally**, that reminds me of some jokes.
# Hope they're as good as the movie!

# I **accidentally** drank a bottle of invisible ink. Now I’m in hospital, waiting to be seen.
# A butcher **accidentally** backed into his meat grinder and got a little behind in his work that day.
# ```
# ---


# To avoid problems with rate limits and site accessibility, we have provided a cache file with results for all the queries you need to make to both OMDb and icanhazdadjokes. Just use `requests_with_caching.get()` rather than `requests.get()`. If you're having trouble, you may not be formatting your queries properly, or you may not be asking for data that exists in our cache. We will try to provide as much information as we can to help guide you to form queries for which data exists in the cache.

import requests_with_caching


apikey = 'abcd1234'  # you may *optionally* replace this with your API key.
# Note: you do *not* need an API key to complete this assignment. Every request should be in the cache
requests_with_caching.clear_cache()
# print(list(requests_with_caching.perm_cache().keys()))

# Fetching movie info from OMDb
# Your first task will be to fetch data from OMDb. The documentation for the API is at[https://www.omdbapi.com/](https: // www.omdbapi.com/)

# Define a function called `get_movie_data`. It takes in one parameter which is a string that should represent the title of a movie you want to search. The function should return a dictionary with information about that movie.

# Again, use `requests_with_caching.get()`. If you were to use the live OMDP API, you would need to get an API key, as described in the documentation. However ** you do not need an API key ** to complete this assignment. For the queries on movies that are already in the permanent cache, you won’t need an API key.

# HINT: Be sure to include ** only ** keys `t` and `r` as query parameters in order to extract data from the cache. If any other parameters are included,  the function will not be able to recognize the data that you're attempting to pull from the cache.

# The following movie titles are in the cache:
# - Black Panther
# - Venom
# - Baby Mama
# - Sherlock Holmes
# - Return of the Jedi
# - Back to the Future

# NOTE: the OMDb API uses http:// instead of https://


def get_movie_data(name: str) -> dict:
    """Returns a dictionary of movie information from the OMDb API.
    
    Parameters
    ----------
    name : str
        The name of the movie to search for.
    
    Returns
    -------
    dict
        A dictionary of movie information.
    """
    baseurl = 'http://www.omdbapi.com/'
    params = {'t': name, 'r': 'json'}
    resp = requests_with_caching.get(baseurl, params=params)
    return resp.json()


results = get_movie_data("Black Panther")
assert type(results) == dict
assert results["Year"] == '2018'

# some other invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# print(get_movie_data("Venom"))
# print(get_movie_data("Baby Mama"))


## Extract the Rotten Tomatoes Rating for a Movie
# Next, you will write a function that extracts the Rotten Tomatoes rating for a movie from the results dictionary as an *integer*. If the movie does not have a Rotten Tomatoes rating, return `-1`.

# Fill in the template for the function below

def rt_rating(movie_data: dict) -> int:
    """Returns the Rotten Tomatoes rating from a dictionary of movie information.
    
    Parameters
    ----------
    movie_data : dict
        A dictionary of movie information.
    
    Returns
    -------
    int
        The Rotten Tomatoes rating. For example, 75% would be returned as the integer 75.
    """
    ratings = movie_data['Ratings']
    for rating in ratings:
        if rating['Source'] == 'Rotten Tomatoes':
            return int(rating['Value'][:-1])
    return -1


# We suggest that you write an assert statement to check the output of your function for the movie Black Panther. The autograder will check results for some other movies.
results = get_movie_data("Black Panther")
assert rt_rating(results) == 96


# Fetching Jokes
# Now you will use another API to fetch a couple of dad jokes related to a movie's plot.

# You will do this in two stages. First you'll implement a helper function that calls the API to get jokes, asking for jokes related to a single word.

# Then you'll use that helper function, calling it with the longest words from the plot summary until it finds one that there are jokes for.

# Search for Jokes Containing a Word
# To search for dad jokes, you'll be using the API for icanhazdadjokes. The documentation for the API is at [https://icanhazdadjoke.com/api](https://icanhazdadjoke.com/api)

# Define a function called `get_joke_data`. It takes in one parameter which is a string. The function should return a dictionary with information about **up to two** jokes that contain that string.

# Again, use `requests_with_caching.get()`. All the query results you need are already in the permanent cache.

# - Note 1: Be sure to include **only** keys `term` and `limit` as query parameters in order to extract data from the cache. If any other parameters are included, the function will not be able to recognize the data that you're attempting to pull from the cache.
# - Note 2: Use the `limit` parameter in the icanhazdadjokes API to limit it to two results (instead of slicing)

def get_joke_data(term: str) -> dict:
    """Returns a dictionary of jokes from the icanhazdadjokes API.
    
    Parameters
    ----------
    term : str
        The search term to use to find jokes.
    
    Returns
    -------
    dict
        A dictionary of jokes.
    """
    baseurl = 'https://icanhazdadjoke.com/search'
    params = {'term': term, 'limit': 2}
    resp = requests_with_caching.get(baseurl, params=params)
    return resp.json()


assert len(get_joke_data("magic")[
           'results']) == 2, "The correct number of jokes for 'magic' should be 2"
assert get_joke_data("magic")[
    'results'][0]['joke'] == "What do you call a magician who has lost their magic? Ian."


# Get Jokes for a Long Word from the Plot Description

# Now you'll define a function called `get_jokes`. It will extract the longest word from the plot and try to find jokes for it. If there aren't any, it will proceed to the next longest word, and so on, until it finds a word for which there are jokes. If there is more than one word of the same length, try words that are earlier in the description first(which `sorted` does by default, since it's "stable" and will only move things around the minimum necessary).

# We provide code that removes punctuation from the words in `plot` and assigns the result to the variable `words`. Your code should extend this by sorting `words` from longest to shortest and use the sorted list (and the `get_joke_data` function that you defined above) to find the longest word with associated jokes. If there are no words with associated jokes, your function should return the tuple `(None, None)`. If there is a word with associated jokes, your function should return a tuple with (1) the longest word with a joke and (2) a list of jokes associated with that word (as a list of strings).

def get_jokes(plot: str, verbosity=0) -> tuple[str, list[str]]:
    """Returns a tuple containing the longest word for which jokes were found
    and the joke itself. Break ties for longest word using the order in `plot`.
    Make sure that you strip punctuation from the word before you search for a joke.

    Parameters
    ----------
    plot : str
        The plot of a movie.

    verbosity : int (optional)
        If 0, no output is printed. If 1, some output is printed about which words were tried.
        Defaults to 0.

    Returns
    -------
    tuple[str, list[str]]
        A tuple containing the word that was used to search for a joke and a list of two joke strings.
    """

    words = plot.split()  # split into separate words
    # remove punctuation for each word
    words = [w.strip(',.!;:') for w in words]

    # WRITE YOUR CODE HERE
    words = sorted(words, key=len, reverse=True)
    for word in words:
        jokes = get_joke_data(word)
        if jokes['total_jokes'] > 0:
            return word, [joke['joke'] for joke in jokes['results']]
    return None, None


# BONUS CHALLENGE(ungraded). If we had specified that ties should be broken by taking words in the alphabetic order rather than later, how could you have done that? Try writing a test and then implementing it!


# Put it All Together

# Now put it all together to make the full app. Define a function, `haha_me`. It takes a movie name as input and verbosity and returns a text string that is meant to entertain the reader.

# We have provided a helper function, `highlight`, that highlights a string inside a larger string by wrapping it in asterisks(`*`). Try invoking it a few times to make sure you understand what it does, then figure out how it should be used based on the sample outputs in the assert statements.

# If the movie is not found in the OMDb API(using `get_movie_data`), return `"No movie found: "` followed by the movie title.

# If the movie is found, but there are no jokes(`get_jokes` returned `(None, None)`), return `"I've got no jokes about this movie. It's too serious!"`.

# If the movie and jokes are found, your function should return a string with each of the following on separate lines:
# - The name of the movie
# - `"Rotten Tomatoes rating: XX%"` (replacing `"XX"` with the actual Rotten Tomatoes rating)
# - The plot of the movie with the joke keyword highlighted(using the provided `highlight` function)
# - `"Speaking of **YY**, that reminds me of some jokes."` (replacing `"YY"` with the joke keyword)
# - A different phrase about the jokes, depending on the Rotten Tomatoes rating:
#     - No Rotten Tomates Rating(meaning the rating is `-1`): `"Hope you like them!"`
#     - Rotten Tomatoes Rating below 70 %: `"Hope they're better than the movie!"`
#     - Rotten Tomates 70 % +: `"Hope they're as good as the movie!"`
# - *(an empty line)*
# - The list of jokes, separated by a newline(using `"\n".join(...)`)

# For example, for Venom:
# ```
# Venom
# Rotten Tomatoes rating: 30%
# A failed reporter is bonded to an alien entity, one of many symbiotes who have invaded ** Earth**. But the being takes a liking to ** Earth ** and decides to protect it.
# Speaking of ** Earth**, that reminds me of some jokes.
# Hope they're better than the movie!

# Astronomers got tired watching the moon go around the **Earth** for 24 hours. They decided to call it a day.
# The rotation of **Earth** really makes my day.
# ```

def highlight(word: str, sentence: str) -> str:
    """
    Highlights a specific word in a sentence by surrounding it with asterisks (**).
    The highlighting is case-insensitive.

    Args:
        word (str): The word to be highlighted.
        sentence (str): The sentence in which the word should be highlighted.

    Returns:
        str: The sentence with the specified word highlighted.
    """
    import re

    # Escape special characters in the word to treat it as a literal string
    # Use re.sub() to replace the word with the highlighted version
    # Use re.IGNORECASE flag to perform case-insensitive replacement
    return re.sub(re.escape(word), f"**{word}**", sentence, flags=re.IGNORECASE)


def haha_me(movie_title: str, verbosity=0) -> str:
    """Returns a string containing a movie title, the Rotten Tomatoes rating, a plot summary,
    and two jokes about the movie. If no jokes are found, a message is returned instead.

    Parameters
    ----------
    movie_title : str
        The title of a movie.
    
    verbosity : int (optional)
        If 0, no output is printed. If 1, some output is printed about which plot words were tried.
        Defaults to 0.
    """
    movie_data = get_movie_data(movie_title)
    if movie_data == {}:
        return f"No movie found: {movie_title}"
    rt = rt_rating(movie_data)
    plot = movie_data['Plot']
    keyword, jokes = get_jokes(plot, verbosity)
    if keyword is None:
        return "I've got no jokes about this movie. It's too serious!"
    if rt == -1:
        rating_phrase = "Hope you like them!"
    elif rt < 70:
        rating_phrase = "Hope they're better than the movie!"
    else:
        rating_phrase = "Hope they're as good as the movie!"
    return f"{movie_title}\nRotten Tomatoes rating: {rt}%\n{highlight(keyword, plot)}\nSpeaking of **{keyword}**, that reminds me of some jokes.\n{rating_phrase}\n\n{chr(10).join(jokes)}"


assert haha_me("Black Panther", verbosity=1) == """Black Panther
Rotten Tomatoes rating: 96%
T'Challa, heir to the hidden but advanced kingdom of Wakanda, must step **forward** to lead his people into a new future and must confront a challenger from his country's past.
Speaking of **forward**, that reminds me of some jokes.
Hope they're as good as the movie!

Sometimes I tuck my knees into my chest and lean **forward**.  That’s just how I roll.
Why do scuba divers fall backwards into the water? Because if they fell **forward**s they’d still be in the boat."""
