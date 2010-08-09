class HeapSort:
  def __init__(self,elements):
    self.heap = elements
    self.heap_size = len(elements)-1

  def left(self,i):
    return 2*i+1

  def right(self,i):
    return 2*i+2
  
  def parent(self,i):
    return i/2-1

  def max_heapify(self,i):
    l = self.left(i)
    r = self.right(i)
    A = self.heap
    heap_size = self.heap_size

    largest = l if l <= heap_size and A[l] > A[i]  else i
    if r <= heap_size and A[r] > A[largest]:
      largest = r

    if largest is not i:
      A[i],A[largest] = A[largest],A[i]
      self.max_heapify(largest)

  def build_max_heap(self):
    for i in xrange(self.heap_size/2, -1, -1):
      self.max_heapify(i)

  def sort(self):
    A = self.heap
    self.build_max_heap()
    
    for i in xrange(self.heap_size, 0, -1):
      A[0], A[i] = A[i], A[0]
      self.heap_size -= 1
      self.max_heapify(0)

    self.heap_size = len(A)

  def heap_maximum():
    return self.heap[0]

  def heap_extract_max():
    if self.

if __name__=="__main__":
  A = [4,1,3,2,16,9,10,14,8,7]
  print A
  heap = HeapSort(A)
  #heap.build_max_heap()
  #print "build_max_heap():",A
  heap.sort()
  print "sort():",A
 

