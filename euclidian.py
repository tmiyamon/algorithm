def gcd(m, n):
  m -= 1
  n -= 1
  while m % n is not 0:
    tmp = n
    n = m % n
    m = tmp

  return n

print gcd(15439,3511)
