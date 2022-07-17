#author- Diwakar Sharma [Github- diwakarsharma4]
#-----------------------------------------------

#The selection sort algorithm sorts an array by repeatedly finding the minimum element from unsorted part, and putting it at the beginningn of sorted part.

#Time complexity : O(n^2)
#Space complexity : O(1)
#It is an in-place sorting algorithm.
#It can be both stable and non-stable sorting.

#Non-stable selection sort :
def selection_sort(arr, n):
    for indx in range(n):
        min_indx = indx
        for curr in range(indx+1, n):
            if arr[curr] < arr[min_indx]:
                min_indx = curr
        arr[indx], arr[min_indx] = arr[min_indx], arr[indx]
        
arr = [12, 11, 13, 5, 6]
selection_sort(arr, len(arr))
print(arr)
#output -> [5, 6, 11, 12, 13]
#----------------------------------------------------------------------------------------------------

#Stable selection sort :
def selection_sort(arr, n):
    for indx in range(n):
        min_indx = indx
        for curr in range(indx+1, n):
            if arr[curr] < arr[min_indx]:
                min_indx = curr
    
        key = arr[min_indx]
        while min_indx > indx:
            arr[min_indx] = arr[min_indx-1]
            min_indx -= 1
        arr[indx] = key
        
arr = [12, 11, 13, 5, 6]
selection_sort(arr, len(arr))
print(arr)
#output -> [5, 6, 11, 12, 13]
#----------------------------------------------------------------------------------------------------
