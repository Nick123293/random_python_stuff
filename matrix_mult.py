#!/usr/bin/python3
"""Mathparse automatically resolves expressions, allowing for the input of arbitrary expressions into python elements.

--force-dims manually checks the matrix dimensions to make sure the multiplication is valid. numpy also does this, but using --force-dims gives 
a cleaner error."""

import numpy as np
import argparse
import sys
from mathparse import mathparse

def get_matrix(i: int):
  m = int(input(f"How many rows in matrix {i} "))
  n = int(input(f"How many columns in matrix {i} "))
  arr=np.zeros((m, n))
  for x in range(m):
    for y in range(n):
      arr[x,y]=mathparse.parse(input(f"Input val {x},{y} "))
  return arr

def ensure_dims(matrices: list[np.ndarray], i: int):
  if(matrices[i-1].shape[1] != matrices[i].shape[0]):
    print("Dimension mismatch resulting in undefined matrix multiplication.\n")
    sys.exit(1)
  return 0


def main():
  parser=argparse.ArgumentParser(description="Usage: python3 matrix_mult.py [--force_dims]: optional")
  parser.add_argument("--force-dims", action='store_true' ,help="If given, forces dimensions to allow matrix multiplication")
  args = parser.parse_args()
  n = int(input("How many matrices are you multiplying \n"))
  matrices=[]
  for i in range(n):
    matrices.append(get_matrix(i))
    if(i!=0 and args.force_dims):
      ensure_dims(matrices, i)
  init=np.dot(matrices[0], matrices[1])
  for mults in range(len(matrices)-2): #If multiplying only two matrices, this for loop does not do anything
    init=np.dot(init, matrices[mults])
  print(init)
  return 0

if __name__ == "__main__":
  main()