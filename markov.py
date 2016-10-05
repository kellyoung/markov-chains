from random import choice

import sys


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    with open(file_path) as file_text:
        contents = file_text.read()

    return contents


def make_chains(text_string, gram_length):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}

    # your code goes here
    words = text_string.split()

    for i in range(len(words) - gram_length):
        # first create a tuple as chains' key
        n_grams = tuple(words[i:i+gram_length])

        #then create the key's value
        chains[n_grams] = chains.get(n_grams, [])
        chains[n_grams].append(words[i+gram_length])

    return chains


def make_text(chains, gram_length):
    """Takes dictionary of markov chains; returns random text."""

    # create a sublist of tuples to choose 1
    capitalized_keys = [key for key in chains.keys() if key[0][0].isupper()]

    n_gram = choice(capitalized_keys)  # choosing randomly out of keys to begin chain process
    random_text = ''                # instantiates string

    for index in range(gram_length):  # adding each word in the tuple to start off
        random_text += n_gram[index] + ' '

    making_text = True
    while making_text:
        try:
            n_gram_choices = chains[n_gram]  # returns a list of values of bigram
            word_to_add = choice(n_gram_choices)  # choosing one of the values of bigram
            
            random_text += word_to_add + ' '  # adds a new word to the text
            n_gram_args = list(n_gram[1:gram_length]) + [word_to_add]  # creates next key values for chain
            n_gram = tuple(n_gram_args)  # converts the key values to tuple

        except KeyError:
            making_text = False  # reaches end of markov chain
    
    # slice random_text to when you find the last punctuation

    # find last punctuation
    punctuations = ['.', '?', '!', '"']

    index = len(random_text) - 1

    while index > -1:
        if random_text[index] in punctuations:
            return random_text[:index + 1]
        index -= 1


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
n = int(sys.argv[2])
chains = make_chains(input_text, n)

#Produce random text
random_text = make_text(chains, n)

print random_text
