# Accepting arguments from command line (DO NOT DIRECTLY RUN THIS FILE)
# To run, open terminal and type 'python arguments.py [arguments]' then hit enter

# Example - python arguments.py Lewis Hamilton

import sys
# print(sys.argv)

name = sys.argv[1]          # Indexing is from 1 itself
print(f"Hello {name}")

name = sys.argv[2]
print(f"Hello {name}")
