def bsearch(A, v):
  if len(A) is 0:
    return

  middle = len(A)/2
  if v is A[middle]:
    return middle
  elif v < A[middle]:
    return bsearch(A[:middle],v)
  else:
    return middle + bsearch(A[middle:], v)

B = [10,20,30,40,50,60,70,80,90]
print bsearch(B, 5)

