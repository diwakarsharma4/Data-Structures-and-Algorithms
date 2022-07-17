#author- Diwakar Sharma [Github- diwakarsharma4]
#-----------------------------------------------

#Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands.
#The array is virtually split into a sorted and an unsorted part.
#Values from the unsorted part are picked and placed at the correct position in the sorted part.

#Time complexity : O(n^2)
#Space complexity : O(1)
#It is an in-place sorting algorithm
#It is a stable sorting algorithm

def insertion_sort(arr, n):
    for indx in range(n):
        key = arr[indx]
        curr = indx - 1
        while curr >= 0 and key < arr[curr]:
            arr[curr+1] = arr[curr]
            curr -= 1
        arr[curr+1] = key
        
arr = [12, 11, 13, 5, 6]
insertion_sort(arr, len(arr))
print(arr)
#output -> [5, 6, 11, 12, 13]
