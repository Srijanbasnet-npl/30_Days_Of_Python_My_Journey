import itertools


A = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
B = {2, 4, 6, 8, 10, 12, 14}
C = {1, 3, 5, 7, 9}

print("--- Set Operations Results ---\n")

is_b_subset = B.issubset(A)
print(f"Is B a subset of A?: {is_b_subset}")

is_c_subset = C.issubset(A)
print(f"Is C a subset of A?: {is_c_subset}")

union_ab = A.union(B)
print(f"The union of A and B: {union_ab}")

intersect_ac = A.intersection(C)
print(f"The intersection of A and C: {intersect_ac}")

diff_ab = A.difference(B)
print(f"The difference A - B: {diff_ab}")

sym_diff_bc = B.symmetric_difference(C)
print(f"The symmetric difference of B and C: {sym_diff_bc}")

cartesian_product = set(itertools.product(A, B))
print(f"\nThe cartesian products A x B ({len(cartesian_product)} pairs):\n{cartesian_product}")