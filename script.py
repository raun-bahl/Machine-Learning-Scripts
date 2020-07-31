def sum_to_n(arr, n):
    list1 = []
    list2 = []
    for i in arr:
        for j in arr:
            if i+j == n and i not in list2 and j not in list2:
                list1.append(i)
                list1.append(j)
    list2.append(list1)
        
    print(list2)

    
                
