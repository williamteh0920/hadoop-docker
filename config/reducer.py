#!/usr/bin/env python3

from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None

# Input comes from STDIN
for line in sys.stdin:
    # Remove leading and trailing whitespaces
    line = line.strip()

    # Split the line into word and count
    word, count = line.split('\t', 1)

    # Convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # Ignore/discard this line if the count is not a valid integer
        continue

    # Process the same word
    if current_word == word:
        current_count += count
    else:
        # A new word encountered, print the count of the previous word
        if current_word:
            print(f"{current_word}\t{current_count}")
        current_count = count
        current_word = word

# Output the last word
if current_word == word:
    print(f"{current_word}\t{current_count}")
