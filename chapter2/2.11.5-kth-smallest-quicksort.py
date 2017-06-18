#partition : put privot to the correct position
import timeit
import random

def partition(arr, low, high):
    #print ("before",arr, low, high, arr[high])
    pivot = arr[high]
    lowerightboundry = low

    # travel all element in arr, arrange by pivot,
    # lowerightboundry is holding the right most boundry idx for elements smaller than pivot
    for idx in range(low, high):
        if arr[idx] <= pivot:
            arr[idx], arr[lowerightboundry] = arr[lowerightboundry], arr[idx]
            lowerightboundry = lowerightboundry + 1

    arr[lowerightboundry], arr[high] = arr[high], arr[lowerightboundry]
    #print("after", arr)
    return lowerightboundry

def quickSort(arr, low, high):
    if low < high:
        pivot_idx = partition(arr,low,high)
        quickSort(arr, low, pivot_idx-1)
        quickSort(arr, pivot_idx+1, high)


#
# n = len(arr)
# quickSort(arr,0,n-1)
# pi = partition(arr,low,high)
numbers = [5,33,6,2,4,7,8,9,12,41,25,64,57,86,79,17]
# print (partition(numbers,0,len(numbers)-1))
# quickSort(numbers,0, len(numbers)-1)
# print (numbers)
#
# numbers = [5, 6, 2, 4, 7, 8, 9, 12]
# print (partition(numbers,0,len(numbers)-1))
#
# numbers = [5, 6, 2, 4, 7, 8, 13, 12]
# print (partition(numbers,0,len(numbers)-1))

quickSort(numbers,0, len(numbers)-1)
print (numbers)


for i in range(1000, 10001, 1000):
    t = timeit.Timer("quickSort([random.randrange(%d) for _ in range(%d)], 0, %d)" %(i,i, i-1),
                     globals=globals())

    lst_time = t.timeit(number=1000)
    print (lst_time)