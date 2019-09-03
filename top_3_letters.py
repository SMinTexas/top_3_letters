#Given a histogram tally (one returned from either letter_histogram or word_summary), 
# print the top 3 words or letters.

# use supercalifragilisticexpialidocious as the test word

import string

def letter_count(str):
    counts = dict((letter,str.count(letter)) for letter in set(str))
    return counts

input_word = input("Enter a word ")

count_of_letters = letter_count(input_word)
print(count_of_letters)
sorted_letter_count = sorted(count_of_letters, key=count_of_letters.__getitem__, reverse=True)
print(sorted_letter_count)
sObject = slice(0, 3)
print(sorted_letter_count[sObject])