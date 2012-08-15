import sys

def merge( list1, start, mid, end ):
    print( start, mid, end )
    swap_count = 0
    i = start
    j = mid + 1
    sorted_list = []
    while i <= mid and j <= end:
        if list1[i] > list1[j]:
            sorted_list.append(list1[j])
            swap_count += mid - i + 1
            j += 1
        else:
            sorted_list.append(list1[i])
            i += 1

    while i <= mid:
        sorted_list.append(list1[i])
        i += 1

    while j <= end:
        sorted_list.append(list1[j])
        j += 1

    i = start
    for num in sorted_list:
        list1[i] = num
        i += 1

    #print(list1)
    return swap_count

def insertion_sort_swap_count( array, start, end  ):
    #print( start, end )
    if start == end:
        return 0
    mid = ( start + end ) // 2
    swap_count = insertion_sort_swap_count( array, start, mid )
    #print( "Left: %d" % swap_count )
    swap_count += insertion_sort_swap_count( array, mid + 1, end )
    #print( "Right: %d" % swap_count )
    swap_count += merge( array, start, mid, end )
    #print( "Merge: %d" % swap_count )
    return swap_count

test_cases = input()

for i in range( 0, int(test_cases) ):
    array_size = input()
    array_line = input()
    array = [ int(x) for x in array_line.split() ]
    print(insertion_sort_swap_count( array, 0, len(array) - 1 ))
