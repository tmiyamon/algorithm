def next_permutation(n):
  for i in xrange(len(n)-1,-1,-1):
    for j in xrange(i-1, -1, -1):
      if n[j] < n[i]: 
        n[j],n[i] = n[i],n[j]
        return n[:j+1] + sorted(n[j+1:])

a = [1,2,3,4,5]
print a
while True:
  b = next_permutation(a)
  if not b:
    break

  print b
  a = b
