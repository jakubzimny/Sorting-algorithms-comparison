import sort_alg as sort
import random
import time
import numpy as np
import matplotlib.pyplot as plt

def average_time_test(iter_count, size):
    print("Average time test")
    tQS = [0] * iter_count
    tBS = [0] * iter_count
    tMS = [0] * iter_count
    tIS = [0] * iter_count
    tSS = [0] * iter_count
    tHS = [0] * iter_count
    tShell = [0] * iter_count
    for i in range(0, iter_count):
        list1 = [random.randint(0,int(size)) for i in range(int(size))]
        list2 = list1.copy()
        list3 = list1.copy()
        list4 = list1.copy()
        list5 = list1.copy()
        list6 = list1.copy()
        list7 = list1.copy()

        t0 = time.clock()
        sort.quicksort(list1)
        t1 = time.clock()
        tQS[i] = t1 - t0 

        t0 = time.clock()
        sort.bubble_sort(list2)
        t1 = time.clock()
        tBS[i] = t1 - t0

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
        sort.heapsort(list6)
        t1 = time.clock()
        tHS[i] = t1 - t0

        t0 = time.clock()
        sort.shell_sort(list7)
        t1 = time.clock()
        tShell[i] = t1 - t0

        print(str(int(((i+1)/iter_count)*100)) +"% done")

    print ("Quicksort average = " + str(sum(tQS)/iter_count) + " s")
    print ("Bubble sort average = " + str(sum(tBS)/iter_count)+ " s")
    print ("Merge sort average = " + str(sum(tMS)/iter_count)+ " s")
    print ("Insertion sort average = " + str(sum(tIS)/iter_count)+ " s")
    print("Selection sort average = " + str(sum(tSS)/iter_count)+ " s")
    print("Heapsort average = " + str(sum(tHS)/iter_count)+ " s")
    print("Shellsort average = " + str(sum(tShell)/iter_count)+ " s")

def ascending_size_test(iter_count, min_size, max_size):
    tQS = [0] * iter_count
    tBS = [0] * iter_count
    tMS = [0] * iter_count
    tIS = [0] * iter_count
    tSS = [0] * iter_count
    tHS = [0] * iter_count
    tShell = [0] * iter_count
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
        list7 = list1.copy()

        t0 = time.clock()
        sort.quicksort(list1)
        t1 = time.clock()
        tQS[i] = t1 - t0 

        t0 = time.clock()
        sort.bubble_sort(list2)
        t1 = time.clock()
        tBS[i] = t1 - t0

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
        sort.heapsort(list6)
        t1 = time.clock()
        tHS[i] = t1 - t0

        t0 = time.clock()
        sort.shell_sort(list7)
        t1 = time.clock()
        tShell[i] = t1 - t0

        size_list[i] = size
        size += step
        print(str(int(((i+1)/iter_count)*100)) +"% done")
    
    plot_qs = np.array(tQS)
    plot_ms = np.array(tMS)
    plot_hs = np.array(tHS)
    plot_is = np.array(tIS)
    plot_ss = np.array(tSS)
    plot_bs = np.array(tBS)
    plot_shell = np.array(tShell)

    plt.figure()
    plt.semilogy(size_list, plot_bs, label="Bubble sort")
    plt.semilogy(size_list, plot_hs, label="Heapsort")
    plt.semilogy(size_list, plot_qs, label="Quicksort")
    plt.semilogy(size_list, plot_ms, label="Merge sort")
    plt.semilogy(size_list, plot_is, label="Insertion sort")
    plt.semilogy(size_list, plot_ss, label="Selection sort")
    plt.semilogy(size_list, plot_shell, label="Shellsort")
    plt.grid()
    plt.title("Sorting algorithms comparison")
    plt.ylabel("Computation time [s]")
    plt.xlabel("Size of sorted list")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    #average_time_test(100,5e3)
    ascending_size_test(500,10,5e3)
   
    