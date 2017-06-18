import random, timeit
# having a list keeping record of k smallest sorted list. loop the list once only

# (best scenario)if k is reasonable smaller than input list length n,  this performance will be O(n)
# The detail correct answer can be found here: http://www.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array-set-2-expected-linear-time/
def kthsmallest(inputlist, k):
    smalllist = [None for _ in range(k)]

    for i in inputlist:
        smalllist = process(i, smalllist)
        #print(smalllist)
    return smalllist[k-1]

def process (check, smalllist):

    for idx in range(len(smalllist)):
        if smalllist[idx] is None or check <= smalllist[idx]:
            smalllist.insert(idx, check)
            return smalllist[:-1]
    return smalllist

kthsmallest([1,23,4,5,6,4,3], 5)
numbers = [5,33,6,2,4,7,8,9,12,41,25,64,57,86,79,1]
print (kthsmallest(numbers, 5))

print ([random.randrange(1000) for _ in range(1000)])

print (kthsmallest([random.randrange(1000) for _ in range(1000)], 5))

for i in range(10000, 100001, 10000):
    t = timeit.Timer("kthsmallest([random.randrange(%d) for _ in range(%d)], %d)" %(i,i, i-1),
                     globals=globals())

    lst_time = t.timeit(number=1000)
    print (lst_time)
    # k = 5
    # 15.780868905635469
    # 31.382822092601337
    # 45.13059950368046
    # 63.282038593311526
    # 78.91681596974675

    # k = n - 1