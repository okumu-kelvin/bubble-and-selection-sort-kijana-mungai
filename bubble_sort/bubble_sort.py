def bubble_sort(unsorted_list):
    # TODO: Implement bubble sort
    x = len(unsorted_list)
    for i in range(x):
        for j in range(0,x-i-1):
            if unsorted_list[j] > unsorted_list[j+1]:
                unsorted_list[j],unsorted_list[j+1] = unsorted_list[j+1],unsorted_list[j]
    return unsorted_list            

           
data = [12,18,19,16,54]            
bubble_sort(data)
print("Sorted array:",data)               
                