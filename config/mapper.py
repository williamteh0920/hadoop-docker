#!/usr/bin/env python3

import sys

# Input comes from STDIN (standard input)
for line in sys.stdin:
    # Remove leading and trailing whitespaces
    line = line.strip()

    # Split the line into words
    words = line.split()

    # Emit the word and count to the output
    for word in words:
        # Output to STDOUT (standard output)
        print(f"{word}\t1")
