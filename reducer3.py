#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip()
    line = line.split(" ")
    prod_id, value = line
    print(f"{prod_id}\t{value}")

