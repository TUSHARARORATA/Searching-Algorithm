# Binary Search with Time Complexity of O(logN):
def Binary_Search(array,k):
    len_array=len(array)
    result=-1
    if array==[k]:
        return 0
    else:
        low=0
        high=len_array-1
        while(low<=high):
            middle=(low+high)//2
            if array[middle]>k:
                high=middle-1
            elif array[middle]<k:
                low=middle+1
            elif array[middle]==k:
                return middle
            if low>high:
                return result
    return result

            
    
        
    

if __name__=='__main__':
    array=input("Enter array").split(',')
    array=list(map(int,array))
    search_element=int(input("Enter element to be searched"))
    result=Binary_Search(array,search_element)
    if result==-1:
        print("Element not found")
    else:
        print("Element found at index ",result)