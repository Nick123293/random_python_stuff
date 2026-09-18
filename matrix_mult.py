
"""Mathparse automatically resolves expressions, allowing for the input of arbitrary expressions into python elements"""

import numpy as np
from mathparse import mathparse

def get_matrix(i: int):
  m = int(input(f"How many rows in matrix {i} "))
  n = int(input(f"How many columns in matrix {i} "))
  arr=np.zeros((m, n))
  for x in range(m):
    for y in range(n):
      arr[x,y]=mathparse.parse(input(f"Input val {x},{y} "))
  return arr


def main():
  n = int(input("How many matrices are you multiplying \n"))
  matrices=[]
  for i in range(n):
    matrices.append(get_matrix(i))
  init=np.dot(matrices[0], matrices[1])
  for mults in range(len(matrices)-2): #If multiplying only two matrices, this for loop does not do anything
    init=np.dot(init, matrices[mults])
  print(init)
  return 0

if __name__ == "__main__":
  main()