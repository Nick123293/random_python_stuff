#!/usr/bin/python3
"""
Finds the inverse of an NxN matrix (given it has one)
Mathparse automatically resolves expressions, allowing for the input of arbitrary expressions into python elements.
  """

import numpy as np
from mathparse import mathparse

def get_matrix():
  m = int(input(f"How many rows/cols in matrix "))
  arr=np.zeros((m, m))
  for x in range(m):
    for y in range(m):
      arr[x,y]=mathparse.parse(input(f"Input val {x},{y} "))
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