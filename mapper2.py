#!/usr/bin/env python3
import sys

for line in sys.stdin:
    fields = line.strip().split(" ")
    prod_id, record_type, cus_id, value = fields
    if record_type == 'review' and int(value)<3:
        print(prod_id,record_type,cus_id,value)
    else:
        if record_type == 'order':
            print(prod_id,record_type,cus_id,value)
