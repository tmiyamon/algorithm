def merge(left, right):
  result = []
  while len(left) is not 0 and len(right) is not 0:
    if left[0] < right[0]:
      result.append(left.pop(0))
    else:
      result.append(right.pop(0))

  result.extend(left)
  result.extend(right)

  return result


def msort(a):
  n = len(a)
  if n <= 1:
    return a

  return merge(msort(a[:n/2]),msort(a[n/2:]))


print msort([1,5,7,2,3,4,8,3,9])

