#!/usr/bin/env python3

import sys

for line in sys.stdin:

    fields = line.strip().split('\t')

    if fields[0] == 'order':

        order_id, customer_id, product_id, quantity, price = fields[1:]

        print(f"{product_id}\torder\t{customer_id}\t{quantity}")

    elif fields[0] == 'review':

        review_id, product_id, customer_id, rating, _ = fields[1:]

        print(f"{product_id}\treview\t{customer_id}\t{rating}")



