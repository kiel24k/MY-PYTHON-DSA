def binary_search(list, target):
    first = 0 # 5
    last = len(list) - 1 #9
    
    while first <= last: # 0 <= 9 : true || 5 <= 9 : true || 
        midpoint = (first + last)//2 # midpoint = 4 || 7
        
        if list[midpoint] == target:   #5 == 8 : false || 8 == 8 : true
            return midpoint
        elif list[midpoint] < target:  #5 < 8 : true 
            first = midpoint + 1 # first = 5
        else:
           last = midpoint - 1 
    return None

def verify(index):
    if index is not None:
        print("target found at index: ", index)
    else:
        print("Target not found in list")

        
# python variables
numbers = [1,2,3,4,5,6,7,8,9,10]

result = binary_search(numbers, 8)

verify(result)

# hahaha dasd
#dasdasdloolokoksassd
    
