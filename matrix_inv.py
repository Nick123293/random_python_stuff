#!/usr/bin/python3
"""
Finds the inverse of an NxN matrix (given it has one)
Mathparse automatically resolves expressions, allowing for the input of arbitrary expressions into python elements.
  """

import numpy as np
from mathparse import mathparse
import re

def sanitize_input(input: str):
  return re.sub(r'(?<!\d)\.(\d+)', r'0.\1', input) #add a 0 to the beginning of the string it it starts with a . (or has letters before the .)

def get_matrix():
  m = int(input(f"How many rows/cols in matrix "))
  arr=np.zeros((m, m))
  for x in range(m):
    for y in range(m):
      arr[x,y]=mathparse.parse(sanitize_input(input(f"Input val {x},{y} "))) #Take input, sanitize it, then parse with mathparse
  return arr


def main():
  matrix = (get_matrix())
  inv=np.linalg.inv(matrix)
  print(inv)
  print("Verify: M*inv(M)=I")
  print(np.round(matrix @ inv))
  return 0

if __name__ == "__main__":
  main()