#!/usr/bin/env python3
""" Solution for codeforces 'Watermalone' problem
    https://codeforces.com/problemset/problem/4/A
"""
w = int(input())
print('YES' if w % 2 == 0 and w > 2 else 'NO')
