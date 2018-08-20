import sort_alg as sort
import random
import time
import numpy as np
import matplotlib.pyplot as plt

def average_time_test(iter_count, size):
    print("Average time test")
    tQS = [0] * iter_count
    tBubble = [0] * iter_count
    tMS = [0] * iter_count
    tIS = [0] * iter_count
    tSS = [0] * iter_count
    tHS = [0] * iter_count
    for i in range(0, iter_count):
        list1 = [random.randint(0,int(size)) for i in range(int(size))]
        list2 = list1.copy()
        list3 = list1.copy()
        list4 = list1.copy()
        list5 = list1.copy()
        list6 = list1.copy()

        t0 = time.clock()
        sort.quicksort(list1)
        t1 = time.clock()
        tQS[i] = t1 - t0 

        t0 = time.clock()
        sort.bubble_sort(list2)
        t1 = time.clock()
        tBubble[i] = t1 - t0

        t0 = time.clock()
        sort.merge_sort(list3)
        t1 = time.clock()
        tMS[i] = t1 - t0

        t0 = time.clock()
        sort.insertion_sort(list4)
        t1 = time.clock()
        tIS[i] = t1 - t0

        t0 = time.clock()
        sort.selection_sort(list5)
        t1 = time.clock()
        tSS[i] = t1 - t0
        
        t0 = time.clock()
        sort.heap_sort(list6)
        t1 = time.clock()
        tHS[i] = t1 - t0

        print(str(int(((i+1)/iter_count)*100)) +"% done")

    print ("Quicksort average = " + str(sum(tQS)/iter_count) + " s")
    print ("Bubble sort average = " + str(sum(tBubble)/iter_count)+ " s")
    print ("Merge sort average = " + str(sum(tMS)/iter_count)+ " s")
    print ("Insertion sort average = " + str(sum(tIS)/iter_count)+ " s")
    print("Selection sort average = " + str(sum(tSS)/iter_count)+ " s")
    print("Heap sort average = " + str(sum(tHS)/iter_count)+ " s")

def ascending_size_test(iter_count, min_size, max_size):
    tQS = [0] * iter_count
    tBubble = [0] * iter_count
    tMS = [0] * iter_count
    tIS = [0] * iter_count
    tSS = [0] * iter_count
    tHS = [0] * iter_count
    size = min_size
    step = (max_size - min_size)//iter_count 
    size_list =[0] * iter_count
    for i in range(0, iter_count):
        list1 = [random.randint(0,int(size)) for i in range(int(size))]
        list2 = list1.copy()
        list3 = list1.copy()
        list4 = list1.copy()
        list5 = list1.copy()
        list6 = list1.copy()

        t0 = time.clock()
        sort.quicksort(list1)
        t1 = time.clock()
        tQS[i] = t1 - t0 

        t0 = time.clock()
        sort.bubble_sort(list2)
        t1 = time.clock()
        tBubble[i] = t1 - t0

        t0 = time.clock()
        sort.merge_sort(list3)
        t1 = time.clock()
        tMS[i] = t1 - t0

        t0 = time.clock()
        sort.insertion_sort(list4)
        t1 = time.clock()
        tIS[i] = t1 - t0

        t0 = time.clock()
        sort.selection_sort(list5)
        t1 = time.clock()
        tSS[i] = t1 - t0
        
        t0 = time.clock()
        sort.heap_sort(list6)
        t1 = time.clock()
        tHS[i] = t1 - t0

        size_list[i] = size
        size += step
        print(str(int(((i+1)/iter_count)*100)) +"% done")

        

if __name__ == "__main__":
    average_time_test(100,2e3)
    