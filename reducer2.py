#!/usr/bin/env python3

import sys
from collections import defaultdict

rev_dict = defaultdict(int)
ord_dict = defaultdict(int)

for line in sys.stdin:

    line = line.strip().split(" ")

    prod_id, record_type, cus_id, value = line
    key = (prod_id, cus_id)
    if record_type == 'review':
        rev_dict[key] = value
    else:
        ord_dict[key] = value

for key, value in rev_dict.items():
    print(key[0],key[1],ord_dict[key])