#!/usr/bin/env python

# Google Code Jam 20XX - YY Round - Problem ZZ

def single(func):
    return func(raw_input())

def row(func):
    return map(func, raw_input().split())

def printcase(case, out, pattern='Case #%d: %s'):
    print pattern % (case, out)

def repeat(func, times):
    return [func() for _ in xrange(times)]


T = single(int)
for t in xrange(1, T + 1):
    # start here
