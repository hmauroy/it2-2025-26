"""
Oppgave 1: Lag en funksjon random_string_list(length) som returnerer 
en liste med strenger med tilfeldig utvalgte bokstaver. 
Hver streng skal ha en lengde på 10 bokstaver. 
Parameteren length angir lengden på lista (antall strenger).

Henrik:
Bruker ASCII-alfabetet med små bokstaver med verdier 97-122.

Oppgave 2: Implementer algoritmen InsertionSort som funksjonen insertion_sort(unsorted_list). 
Algoritmen skal ta en usortert liste som input-argument og returnere en sortert versjon av samme liste.

Oppgave 3: Implementer algoritmen MergeSort som funksjonen merge_sort(unsorted_list). 
Algoritmen skal returnere en sortert liste, på samme måte som insertion_sort(). 
Som del av algoritmen skal du også implementere funksjonen merge(list1,list2) som setter sammen 
to ferdig sorterte lister og returnerer en "merged" sortert liste. 


Oppgave 4: Bruk random_string_list() og generer lister med 100, 1000 og 10000 strenger. 
Sorter disse listene med de to algoritmene du har implementert, og mål kjøretiden. 
Prøv så å sortere de samme listene med Pythons «innebygde» metode sorted() og sammenlign 
kjøretiden med dine egne algoritmer.
Svar:
Min mergeSort(list) er rask ved få elementer.
Ved 10000 elementer er insertionSort(list) raskere.
python innebygde sorted(list) er lynrask! Bruker timsort() som er en smart algoritme ingen i Python-verden 
klarer å gjøre bedre. Derfor er den benyttet som hovedsorteringsalgoritme.
"""

from random import randint
import random
random.seed(9001)
import time

def mergeSort_recursively(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        mergeSort_recursively(L)
        mergeSort_recursively(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def merge_sort(unsorted_list):
    if len(unsorted_list) > 1:
        if len(unsorted_list) % 2 == 0:
            half = len(unsorted_list) // 2
        else:
            half = len(unsorted_list) // 2 + 1
        first_half = unsorted_list[:half]
        second_half = unsorted_list[half:]
        # divide first half
        first_half = merge_sort(first_half)
        # divide second half
        second_half = merge_sort(second_half)
        # Do some recursive merging!
        return merge(first_half,second_half)
    else: # Base case
        return unsorted_list

def merge(a,b):
    # a and b MUST be sorted lists:
    # Run through b and check where each element should be placed in a.
    sorted_list = [x for x in a]
    for i in range(len(b)):
        match = False
        current = b[i]
        for j in range(len(sorted_list)):
            no2 = sorted_list[j]
            if b[i] < sorted_list[j]:
                sorted_list.insert(j,b[i])
                match = True
                break
        if match is not True:
            sorted_list.append(b[i])
    return sorted_list
                

def insertion_sort(unsorted_list):
    sorted_list = [unsorted_list[0]]
    for i in range(1,len(unsorted_list)):
        match = False
        for j in range(len(sorted_list)):
            if unsorted_list[i] < sorted_list[j]:
                sorted_list.insert(j,unsorted_list[i])
                match = True
                break
        if match is not True:
            sorted_list.append(unsorted_list[i])
    return sorted_list

def random_string_list(length):
    list_1 = []
    for i in range(length):
        list_1.append(random_chars(10))
    return list_1

def random_chars(n):
    s = ""
    for i in range(n):
        s += chr( randint(97,122) )
    return s

from heapq import merge

def merge_sort_rosetta(m):
    if len(m) <= 1:
        return m

    middle = len(m) // 2
    left = m[:middle]
    right = m[middle:]

    left = merge_sort_rosetta(left)
    right = merge_sort_rosetta(right)
    return list(merge(left, right))


def main():
    #print(f'lengde 3: {random_string_list(3)}')
    #arr = [15,4,23,7,9,11,3]
    #print(f'usortert: {arr}')
    #print(f'sortert: {insertion_sort(random_string_list(10))}')
    #print(f'merge([4,15] , [7,23]): {merge([4,15] , [7,23])}')
    #print(f'merge([4, 7, 15, 23] , [7,23]): {merge([4, 7, 15, 23] , [7,23])}')
    #print(f'merge_sort([15,4,23,7,9,11,3]): {merge_sort([15,4,23,7,9,11,3])}')

    # Performance testing of InsertionSort og MergeSort, and Python sorted() using timsort()
    # Results
    # n = 10000
    # t_insertionSort = [1.52s, 1.52s, 1.50s, 1.50s]
    # t_MergeSort = [1.52s, 1.49s, 1.49s, 1.50s]
    # n = 20000
    # t_insertionSort = [6.17, 6.08, 6.14] sec
    # t_MergeSort = [6.21, 6.22, 6.46] sec
    # n = 30000
    # t_insertionSort = [14.16, 14.41] sec
    # t_MergeSort = [14.91, 14.81] sec
    # n = 60000
    # t_insertionSort = [59.2, ] sec
    # t_MergeSort = [57.4, ] sec
    # t_PythonSort = [0.17, ] sec

    import copy
    n = 10000
    list_1 = random_string_list(n)
    # Henrik endrer på koden pga. jeg tror InsertionSort og TimSort har en sorterte lister.
    list_2 = copy.deepcopy(list_1)
    list_3 = copy.deepcopy(list_1)
    list_4 = copy.deepcopy(list_1)
    list_5 = copy.deepcopy(list_1)

    # MergeSort
    start_time = time.time()
    #print(start_time)
    list_2_sorted = merge_sort(list_2)
    #print(list_1_sorted[:10])
    duration = time.time() - start_time
    print(f"MergeSort sorted {n} lists in {duration*1000:.1f} ms.")

    # InsertionSort
    #print(list_1[:10])
    start_time = time.time()
    #print(start_time)
    list_1_sorted = insertion_sort(list_1)
    #print(list_1_sorted[:10])
    duration = time.time() - start_time
    print(f"InsertionSort sorted {n} lists in {duration*1000:.1f} ms.")

    # Python sort()
    start_time = time.time()
    #print(start_time)
    list_3_sorted = sorted(list_3)
    #print(list_1_sorted[:10])
    duration = time.time() - start_time
    print(f"Python sort sorted {n} lists in {duration*1000:.1f} ms.")

    # MergeSort Recursively
    #print(list_1[:10])
    start_time = time.time()
    #print(start_time)
    list_4_sorted = mergeSort_recursively(list_4)
    #print(list_1_sorted[:10])
    duration = time.time() - start_time
    print(f"MergeSort Recursively sorted {n} lists in {duration*1000:.1f} ms.")

    # MergeSort Rosettacode
    #print(list_1[:10])
    start_time = time.time()
    #print(start_time)
    list_5_sorted = merge_sort_rosetta(list_5)
    #print(list_1_sorted[:10])
    duration = time.time() - start_time
    print(f"MergeSort Rosettacode sorted {n} lists in {duration*1000:.1f} ms.")

    print(f'Diff: insertionSort == MergeSort {list_1_sorted == list_2_sorted}')
    print(f'Diff: insertionSort == PythonSort {list_1_sorted == list_3_sorted}')
    print(f'Diff: MergeSort == MergeSort Recursively {list_2_sorted == list_4_sorted}')
    print(f'Diff: MergeSort Rosetta == PythonSort {list_5_sorted == list_3_sorted}')
    print(f'Diff: MergeSort Rosetta == MergeSort {list_5_sorted == list_2_sorted}')
    
    



if __name__ == "__main__":
    main()