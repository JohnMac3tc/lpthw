def break_words(stuff):
    """this finction will break up words for us"""
    words = stuff.split(' ')
    return words
    
def sort_words(words):
    """sort the words"""
    return sortred(words)
    
def print_first_word(words):
    """prints the first word after popping off"""
    word = words.pop(0)
    
def print_last_word(words):
    """print the last word after popping off"""
    word = words.pop(-1)
    print word
    
def sort_sentence(sentence):
    """takes in a full sentence and returns sorted words"""
    words = break_words(sentence
    return sort_words(words)
    
def print_first_and_last(sentence):
    """prints the first and last sentence"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
    
def print_first_and_last_sorted(sentence):
    """sorts the words then prints the first and last one"""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)