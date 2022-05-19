

def print_upper_words(words, starts_with):
    """for a list of words, print only the words that begin with the letter
    indicated in the starts_with argument"""

    
    for word in words:
        for letter in starts_with:
            if word.startswith(letter):
             word = word.upper()
             print(word)