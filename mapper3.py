#!/usr/bin/env python3

import sys
from collections import defaultdict

quantity = defaultdict(int)

for line in sys.stdin:
    line = line.strip()
    line = line.split(" ")
    prod_id , cus_id, quant = line 
    quantity[prod_id] += int(quant)

quantity_final = sorted(quantity.items())

for key, value in quantity_final:
    print(key, value)   