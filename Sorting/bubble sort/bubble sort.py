#author- Diwakar Sharma [Github- diwakarsharma4]
#-----------------------------------------------

#In bubble sort we start the iteration from the first two elements and compare them.
#If arr[i] > arr[i+1] then we swap those elements.
#We keep reapeating this process until we reach second last element.
#Then for the next pass we again repeat whole process from first two elements.
#Total n-1 passes need to be performed, where n is the number of elements in the array.

#Time complexity - O(n^2)
#Space complexity - O(1)
#It is an in-place sorting algorithm.
#It is a stable sorting algorithm.

def bubble_sort(arr, n):
    for pass_ in range(n-1):
        for indx in range(n-pass_-1):
            if arr[indx] > arr[indx+1]:
                arr[indx], arr[indx+1] = arr[indx+1], arr[indx]

arr = [4, 1, 5, 2, 6, 8]
bubble_sort(arr, len(arr))
print(arr)
#output -> [1, 2, 4, 5, 6, 8]
#--------------------------------------------------------------------------------------------------------

#In case the array got sorted before n-1 passes, we can avoid unnecessary comparisions by using flag.
def bubble_sort(arr, n):
    for pass_ in range(n-1):
        flag = False
        for indx in range(n-pass_-1):
            if arr[indx] > arr[indx+1]:
                arr[indx], arr[indx+1] = arr[indx+1], arr[indx]
                flag = True
        if flag == False:
            break

arr = [4, 1, 5, 2, 6, 8]
bubble_sort(arr, len(arr))
print(arr)
#output -> [1, 2, 4, 5, 6, 8]
#--------------------------------------------------------------------------------------------------------

#recursive method
def bubble_sort(arr, n):
    if n == 0 or n == 1:
        return 
    for indx in range(n-1):
        if arr[indx] > arr[indx+1]:
            arr[indx], arr[indx+1] = arr[indx+1], arr[indx]
    bubble_sort(arr, n-1)
    
arr = [4, 1, 5, 2, 6, 8]
bubble_sort(arr, len(arr))
print(arr)
#output -> [1, 2, 4, 5, 6, 8]
#--------------------------------------------------------------------------------------------------------

