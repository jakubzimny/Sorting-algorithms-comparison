import time
import random

### QUICKSORT ###

def partition(arr, begin, end):
    pivot = begin
    for i in range(begin + 1,end + 1):
        if arr[i] <= arr[begin]:
            pivot += 1
            arr[i], arr[pivot] = arr[pivot], arr[i]

    arr[begin], arr[pivot] = arr[pivot], arr[begin]
    return pivot

def quicksort(arr, begin = 0, end = None):
    if end is None:
        end = len(arr) - 1
    if begin >= end:
        return
    pivot = partition(arr, begin, end)
    quicksort(arr, begin, pivot - 1)
    quicksort(arr, pivot + 1, end)


### MERGE SORT ###

def merge(arr, begin, end, mid):
    
    n = mid - begin + 1
    m = end - mid
    L = [0] * n
    R = [0] * m
    for i in range(0, n):
        L[i] = arr[begin + i]
    for j in range(0,m):
        R[j] = arr[mid + j + 1]   
    i = 0
    j = 0  

    for k in range(begin,end+1):
        if i >= n:
            arr[k] = R[j]
            j += 1
        elif j >= m:
            arr[k] = L[i]
            i += 1
        else:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else: 
                arr[k] = R[j]
                j += 1
    
        
def merge_sort(arr, begin = 0, end = None):
    if end is None:
        end = len(arr) - 1
    if begin >= end:
        return
    
    mid = begin + (end - begin)//2
    merge_sort(arr, begin, mid)
    merge_sort(arr, mid + 1, end)
    return merge(arr, begin, end, mid)


### INSERTION SORT ###

def insertion_sort(arr):
    sorted_arr = []
    sorted_arr.append(arr[0])
    inserted = False
    for i in range(1,len(arr)):
        for j in range(0,len(sorted_arr)):
            if arr[i] <= sorted_arr[j]:
                sorted_arr.insert(j,arr[i])
                inserted = True
                break
        if inserted == False:
            sorted_arr.append(arr[i])
        inserted = False
    return sorted_arr

### SELECTION SORT ###

def selection_sort(arr):
    for i in range(0,len(arr)):
        min_el_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_el_index]:
                min_el_index = j
        if min_el_index != i:
            arr[i], arr[min_el_index] = arr[min_el_index], arr[i]


### HEAP SORT ### 

def max_child(index, size, heap):
    if index * 2 + 1 > size:
        return index * 2
    else: 
         return index * 2 if heap[index * 2] > heap[index * 2 + 1] else index * 2 + 1

def shift_down(index, size, heap):
    while index * 2 <= size:
        mc = max_child(index, size, heap)
        if heap[index] > heap[mc]:
            return
        heap[index], heap[mc] = heap[mc], heap[index]
        index = mc

def build_heap(arr):
    size = len(arr)
    arr = [0] + arr
    index = size // 2
    while index > 0:
        shift_down(index, size, arr)
        index -= 1
    

def heap_sort(arr):
    build_heap(arr)
    size = len(arr) - 1
    for i in range(size, 1, -1):
        arr[1], arr[i] = arr[i], arr[1]
        size -= 1
        shift_down(1,size,arr) 
    arr = arr[1:]

### SHELL SORT ###



### BUBBLE SORT ###

def bubble_sort(arr):
    for i in range(0,len(arr)):
        swapped = False
        for j in range(0,len(arr)):
            if arr[i] <= arr[j] and arr[i] is not arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                swapped = True
        if swapped == False:
            return
