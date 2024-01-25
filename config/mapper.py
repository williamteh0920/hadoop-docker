#!/usr/bin/env python3

import sys
import concurrent.futures

def mapper(line):
    line = line.strip()
    words = line.split()
    result = []

    for word in words:
        result.append((word, 1))

    return result

# Input comes from STDIN (standard input)
with concurrent.futures.ThreadPoolExecutor() as executor:
    # Read input lines asynchronously
    input_lines = [line for line in sys.stdin]

    # Map function using threads
    results = list(executor.map(mapper, input_lines))

    # Flatten the results list
    flattened_results = [item for sublist in results for item in sublist]

    # Output to STDOUT (standard output)
    for word, count in flattened_results:
        print(f"{word}\t{count}")
