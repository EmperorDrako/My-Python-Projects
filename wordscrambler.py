# Simple Python Word Scrambler
# A nice mini project! 
import random 
print("Welcome to the Python word scrambler!")
def scramble_word(word):
    word_list = list(word)
    random.shuffle(word_list)
    return ''.join(word_list)
word = input("\nEnter your word you want to scramble: ")
scrambled = scramble_word(word)
print(f"Your scrambled word is: {scrambled}")
