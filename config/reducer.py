#!/usr/bin/env python3

from operator import itemgetter
import sys
from collections import defaultdict
import concurrent.futures

def reducer(lines):
    current_word = None
    current_count = 0
    result = []

    for line in lines:
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
            # A new word encountered, append the count of the previous word to the result
            if current_word:
                result.append((current_word, current_count))
            current_count = count
            current_word = word

    # Append the last word to the result
    if current_word == word:
        result.append((current_word, current_count))

    return result

# Input comes from STDIN
with concurrent.futures.ThreadPoolExecutor() as executor:
    # Read input lines asynchronously
    input_lines = [line for line in sys.stdin]

    # Group input lines by word using defaultdict
    word_lines_dict = defaultdict(list)
    for line in input_lines:
        word, _ = line.split('\t', 1)
        word_lines_dict[word].append(line)

    # Reduce function using threads
    results = list(executor.map(reducer, word_lines_dict.values()))

    # Flatten the results list
    flattened_results = [item for sublist in results for item in sublist]

    # Sort the result by word
    sorted_results = sorted(flattened_results, key=itemgetter(0))

    # Output to STDOUT (standard output)
    for word, count in sorted_results:
        print(f"{word}\t{count}")
