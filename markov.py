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


def make_chains(text_string):
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

    for i in range(len(words) - 2):
        bigram = (words[i], words[i + 1])
        chains[bigram] = chains.get(bigram, [])
        chains[bigram].append(words[i+2])

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""
    
    bigram = choice(chains.keys())
    random_text = bigram[0].title() + ' ' + bigram[1] + ' '

    while True:
        try:
            bigram_choices = chains[bigram] #returns a list of values of bigram
            word_to_add = choice(bigram_choices) #choosing one of the values of bigram
            random_text += word_to_add + ' '
            bigram = (bigram[1], word_to_add)

        except KeyError:
            break
    
    return random_text


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
