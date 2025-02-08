#!/usr/bin/env python3

# Author: Suyash Mishra

# Author ID: 137285227

# Date Created: 2025/02/04

import sys

if len(sys.argv) != 2:

    print(f"Usage: {sys.argv[0]} <starting_number>")

    sys.exit(1)

timer = int(sys.argv[1])

while timer > 0:

    print(timer)

    timer -= 1

print("blast off!")
