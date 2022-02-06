import math

def main_algo(arr):
    def find_levels(length):
        val = length
        count = 0
        while val > 2:
            val = math.ceil(val / 2)
            count += 1
        return count

    def create_dic(lev):
        store = {}
        count = 1
        while lev  >= count:
            store[count] = []
            count += 1

        return store




    array = arr
    level = find_levels(len(array))
    store = create_dic(level)
    count_store = {"count":0}


    def update_dic(level,arr):
        subject_list = store.get(level)
        for i in arr:
            subject_list.append(i)
        store[level] = subject_list

    def update_count(co):
        sub = count_store.get("count")
        sub += co
        count_store["count"] = sub



    def mergeSort(array, lev):
        gain = 0
        if len(array) > 1:
            level = lev
            
            r = len(array) // 2
            L = array[:r]
            M = array[r:]


            mergeSort(L, level - 1)
            mergeSort(M, level - 1)

            if level != 0:
                update_dic(level,L)
                update_dic(level,M)

            i = j = k = 0



            while i < len(L) and j < len(M):
                if L[i] < M[j]:
                    array[k] = L[i]
                    i += 1
                else:
                    array[k] = M[j]
                    j += 1
                k += 1
                gain += 1

            update_count(gain)




            while i < len(L):
                array[k] = L[i]
                i += 1
                k += 1

            while j < len(M):
                array[k] = M[j]
                j += 1
                k += 1


    def printList(array):
        for i in range(len(array)):
            print(array[i], end=" ")
        print()

    def print_dic(dict):
        for value in dict.values():
            printList(value)

    print(f"The length of array is {len(array)}")
    printList(array)
    mergeSort(array,level)
    print("___________")
    print_dic(store)
    printList(array)
    print(f"total comparisons were {count_store.get('count')}")
    print("___________")
    print("___________")      



main_algo([5, 3, 1, 2, 8, 4, 7, 6])

str_list = []
for i in range(1,51):
    str_list.append(i)
main_algo(str_list)

rev = []
for i in range(50,0,-1):
    rev.append(i)
main_algo(rev)


from random import randint
random = []
for i in range(1,51):
    random.append(randint(1,100))
main_algo(random)
