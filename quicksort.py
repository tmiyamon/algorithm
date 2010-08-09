
def qsort(A):
  if len(A) <= 1: return A
  return qsort([lt for lt in A[1:] if lt < A[0]]) + A[0:1] + qsort([ge for ge in A[1:] if ge >= A[0]])

B = [2,3,4,6,6,7,2,1,4,5]
print qsort(B)
