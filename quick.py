#!/usr/bin/env python3
"""
cheating in my stupid fucking maths class with python fuck fuck fuck fuck you all
"""
from math import *

sfra=lambda x,y: [*(a/gcd(x,y) for a in (x,y))]

def srad(n, s):
  for i in range(2, n):
    d, m = divmod(n, i**s)
    if not m:
      p, q = srad(d, s)
      return (p*i, q)
  else:
    return (1, n)


