def modified_merge(array):

    def mergeSort(array):
        if len(array) > 1:

            #  r is the point where the array is divided into two subarrays
            r = len(array)//2
            L = array[:r]
            M = array[r:]

            # Sort the two halves
            mergeSort(L)
            mergeSort(M)
            i = j = k = 0

            # Until we reach either end of either L or M, pick larger among
            # elements L and M and place them in the correct position at A[p..r]
            while i < len(L) and j < len(M):
                if L[i] < M[j]:
                    array[k] = L[i]
                    i += 1
                else:
                    array[k] = M[j]
                    j += 1
                k += 1

            # When we run out of elements in either L or M,
            # pick up the remaining elements and put in A[p..r]
            while i < len(L):
                array[k] = L[i]
                i += 1
                k += 1

            while j < len(M):
                array[k] = M[j]
                j += 1
                k += 1

            printList(array)


    # Print the array
    def printList(array):
        for i in range(len(array)):
            print(array[i], end=" ")
        print()

    print(f"The length of array is {len(array)}")
    printList(array)
    print("___________")
    print("___________")
    mergeSort(array)
    print("___________")
    print("___________")
    printList(array)
    # print(f"Total comparisons were {count}")


# Driver program
if __name__ == '__main__':
    array = [5,3,1,6,9]
    # 5, 3, 1, 2, 8, 4, 7, 8

    modified_merge(array)
