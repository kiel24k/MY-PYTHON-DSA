def linear_search(list, target):
    """
    Returns the index position of the target if found, else returns None
    """

    for i in range(0, len(list)):
        if list[i] == target:
            return i
      
    return None
   

def verify(index):
    if index is not None:
        print("target found at index: ", index)
    else:
        print("Target not found in list")

        
# python variables
numbers = [1,2,3,4,5,6,7,8,9,10]

# cinallout ng result variable ang function ni linear_search() para tawagin ito mula kay verify 

result = linear_search(numbers, 8)
verify(result)