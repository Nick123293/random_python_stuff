#!/usr/bin/python3
"""
Finds the inverse of an NxN matrix (given it has one)
Mathparse automatically resolves expressions, allowing for the input of arbitrary expressions into python elements.
  """

import numpy as np
import argparse
import sys
from mathparse import mathparse

def get_matrix():
  m = int(input(f"How many rows/cols in matrix "))
  arr=np.zeros((m, m))
  for x in range(m):
    for y in range(m):
      arr[x,y]=mathparse.parse(input(f"Input val {x},{y} "))
  return arr


def main():
  parser=argparse.ArgumentParser(description="Usage: python3 matrix_mult.py [--force_dims]: optional")
  parser.add_argument("--force-dims", action='store_true' ,help="If given, forces dimensions to allow matrix multiplication")
  args = parser.parse_args()
  matrix = (get_matrix())
  inv=np.linalg.inv(matrix)
  print(inv)
  print("Verify: M*inv(M)=I")
  print(np.round(matrix @ inv))
  return 0

if __name__ == "__main__":
  main()