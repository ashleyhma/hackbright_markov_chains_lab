"""Generate Markov text from text files."""

# from random import choice


def open_and_read_file(input_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here

    text_string = open(input_path).read()


    return text_string


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """
    

    chains = {}
    words = input_text.split() 

    for i in range(len(words) - 1):
        # print(words[i], words[i +1])
        tuple_key = (words[i], words[i +1])
        # list_values = []

        if tuple_key not in chains:
        #     # print("first", words[i])
        #     # print("second", words[i+1])
        #     # print("third", words[i+2])  
        #     # print("fourth", words[-len(words)])

            if words[i] in (words[-2], words[-1]):
                continue
            elif words[i] not in (words[-2], words[-1]):
                chains[tuple_key] = [words[i+2]]
                
        else:
            chains[tuple_key] = chains.get(tuple_key, []) + [words[i+2]]
                # print(chains[tuple_key])



    

    return chains


def make_text(chains):
    """Return text from chains."""

    import random

    words = []
    # print(chains)

    
    for tuple_key, choices in chains.items():
        # print(tuple_key)
        next_word = random.choice(choices)
        # print(next_word)
 
        tuple_key_list = [tuple_key[0]] + [tuple_key[1]]
        
        # print(tuple_key_list)
        our_new_list = (tuple_key_list) + [next_word]
        # print(our_new_list)
        words.append(our_new_list)

        next_key_words = our_new_list[1:]
        # print(next_key_words)

        


        


    
        # print(phrase_list)


        # words.append(our_new_phrase)
        # print(words)

        # for new_key,value in chains:
        #     new_next_word = random.choice(value)
        #     new_new_phrase = new_key + new_next_word

        # print(key, "strings")
        # print(next_word, "next")
        # print(our_new_phrase, "new")

    # your code goes here

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)
print(chains)

# # Produce random text
# random_text = make_text(chains)

# print(random_text)
