# Sorting algorithms comparison
## Overview
This little project was made mostly because i wanted to catch up with sorting algorithms. Implementations are probably far from optimal so take it for what it's worth.

I tested 7 different algorithms:
1. Quicksort (not randomized)
2. Merge sort
3. Heapsort
4. Selection sort
5. Insertion sort
6. Shellsort (using Marcin Ciura's sequence)
7. Bubble sort

with 2 tests, first was taking an average of 100 sorts of randomized arrays with 5000 elements, second was mapping sorting time to size of an array to reveal differences in their complexity.

*Important note: Both tests used time.clock() function which returns real time instead of cpu time on windows, so they're just an aproximation.*

## Results
First test on my machine produced those results (rounded up to 4th decimal place):

**1. Quicksort average = 0.0105 s
2. Heapsort average = 0.0141 s
3. Shellsort average = 0.0148 s
4. Merge sort average = 0.0216 s
5. Selection sort average = 0.6874 s
6. Insertion sort average = 1.522 s
7. Bubble sort average = 2.0728 s**

Second test produced following graph:
