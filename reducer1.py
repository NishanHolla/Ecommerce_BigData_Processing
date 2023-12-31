#!/usr/bin/env python3

import sys

for line in sys.stdin:

    product_id, record_type, customer_id, value = line.strip().split('\t')
    print(product_id,record_type,customer_id,value)

