#!/usr/bin/python3
"""
Calculates single head attention given an input query, key vectors, and scalar values for all previous tokens (or tokens in context window)
Values must be input manually. Including the query vector, key matrix, and value vector.
Requires numpy
"""
import math
import numpy as np
q_favorite=np.array([1,2])
key_matrix=np.array([[1,0],[0,1],[1,1],[2,0],[0,2]])
key_matrix_t=key_matrix[:, :, np.newaxis]
print("q_favorite:")
print(q_favorite)
print("\n")

print("key matrix transposed:")
print(key_matrix_t)
print("\n")

d_k=math.sqrt(2)
print("sqrt(d_k):")
print(d_k)
print("\n")

scaled_scores=np.dot(q_favorite, key_matrix_t)/d_k
print("scaled_scores:")
print(scaled_scores)
print("\n")
scaled_scores=scaled_scores.transpose()
print("scaled_scores transposed (s):")
print(scaled_scores)
print("\n")

x = [1/math.sqrt(2), math.sqrt(2), 3/math.sqrt(2), math.sqrt(2), 2*math.sqrt(2)]
y = np.exp(scaled_scores)
print("e^{s}:")
print(y)
print("\n")

z=np.sum(y)
print("sum_{i=1}^{5}e^{s}")
print(z)
print("\n")

fin = y/z
print("alpha:")
print(fin)
print("\n")

round = np.round(fin, decimals=4)
print("alpha rounded (to sum to 1):")
print(round)
print("\n")

print("Ensure sum of alpha is 1:")
print(round.sum())
print("\n")

v=[2, 5, 1, 6, 3]
v_np = np.array(v)
print("value vector (v):")
print(v_np)
print("\n")

intermediate=round*v_np
print("element-wise multiplication of v and rounded alpha:")
print(intermediate)
print("\n")

scalar_attention=intermediate.sum()
print("sum of intermediate: final scalar attention")
print(scalar_attention)
print("\n")
