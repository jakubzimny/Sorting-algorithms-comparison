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

class BinaryHeap:
    def __init__(self):
        self.heap_list = [0]
        self.size = 0
    
    def percolate_up(self, index):
        while index // 2 > 0:
            if self.heap_list[index] > self.heap_list[index // 2]:
                self.heap_list[index], self.heap_list[index // 2] = self.heap_list[index // 2], self.heap_list[index]
            index = index // 2

    def insert(self, element):
        self.heap_list.append(element)
        self.size = self.size + 1
        self.percolate_up(self.size)
    
    def min_child(self, index):
        if index * 2 + 1 > self.size:
            return i * 2
        else: 
            return index * 2 if self.heap_list[index*2] <= self.heap_list[index*2 + 1] else index * 2 + 1

    def percolate_down(self, index):
        while index * 2 <= self.size:
            mc = self.min_child(index)
            if self.heap_list[index] <= self.heap_list[mc]:
                return
            self.heap_list[index], self.heap_list[mc] = self.heap_list[mc], self.heap_list[index]
            index = mc

    def delete_min(self):
        root_value = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.size]
        self.heap_list.pop()
        self.size = self.size - 1
        self.percolate_down(1)
        return root_value


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

# Driver program

if __name__ == "__main__":
    # list1 = [5,1,2,4,5,8,8,9,0,0,12,47,3]
    # list2 = [1,2,3,4,5,6,7]
    # list3 = [7,6,5,4,3,2,1]
    # bubble_sort(list1)
    # print(list1)

    it = 100
    tQS = [0] * it
    tBubble = [0] * it
    tMS = [0] * it
    tIS = [0] * it
    tSS = [0] * it
    for i in range(0,it):
        list1 = [random.randint(0,1000) for i in range(1000)]
        list2 = list1.copy()
        list3 = list1.copy()
        list4 = list1.copy()
        list5 = list1.copy()

        t0 = time.clock()
        quicksort(list1)
        t1 = time.clock()
        tQS[i] = t1 - t0 

        t0 = time.clock()
        bubble_sort(list2)
        t1 = time.clock()
        tBubble[i] = t1 - t0

        t0 = time.clock()
        merge_sort(list3)
        t1 = time.clock()
        tMS[i] = t1 - t0

        t0 = time.clock()
        insertion_sort(list4)
        t1 = time.clock()
        tIS[i] = t1 - t0

        t0 = time.clock()
        selection_sort(list5)
        t1 = time.clock()
        tSS[i] = t1 - t0

        print(i)

    print ("Quicksort average = " + str(sum(tQS)/it))
    print ("Bubble sort average = " + str(sum(tBubble)/it))
    print ("Merge sort average = " + str(sum(tMS)/it))
    print ("Insertion sort average = " + str(sum(tIS)/it))
    print("Selection sort average = " + str(sum(tSS)/it))