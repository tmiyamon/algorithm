#!/usr/bin/python
# -*- coding: utf-8 -*-

class Heap:
  def left(self,i):
    return (i<<1) + 1 

  def right(self,i):
    return (i<<1) + 2

  def parent(self,i):
    return i>>1

  def max_heapify(self,A,i):
    l = self.left(i)
    r = self.right(i)

    largest = l if l < len(A) and A[l] > A[i] else i
    if r < len(A) and A[r] > A[largest]:
      largest = r
    
    if largest is not i:
      A[i],A[largest] = A[largest],A[i]
      self.max_heapify(A, largest)

  def build_max_heap(self,A):
    for i in xrange(len(A)/2-1, -1, -1):
      self.max_heapify(A, i)
    

  def min_heapify(self,A,i):
    l = self.left(i)
    r = self.right(i)

    smallest = l if l < len(A) and A[l] < A[i] else i
    if r < len(A) and A[r] < A[smallest]:
      smallest = r

    if smallest is not i:
      A[smallest], A[i] = A[i], A[smallest]
      self.min_heapify(A, smallest)

  def build_min_heap(self,A):
    for i in xrange(len(A)/2-1, -1, -1):
      self.min_heapify(A, i)

class MaxPriorityQueue(Heap):
  def extract_max(self,A):
    if len(A) < 1:
      raise Error("Heap under flow")
    
    max = A[0]

    A[0] = A.pop(len(A)-1)

    self.max_heapify(A,0)
    
    return max

  def increse_key(self,A,i,key):
    if key < A[i]:
      raise Error("New key is smaller than current one")

    A[i] = key
    while 0 < i and A[parent(i)] < A[i]:
      A[i],A[parnet(i)] = A[parnet(i)],A[i]
      i = parent(i)


import random 

q = MaxPriorityQueue()
#B = [4,1,3,2,16,9,10,14,8,7]
B = range(100)
random.shuffle(B)
print B
q.build_max_heap(B)
print B
while len(B) > 0:
  print q.extract_max(B)
  #print B
