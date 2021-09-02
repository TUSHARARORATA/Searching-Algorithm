# Linear Search with Time Complexity of O(N):
def Linear_Search(array,k):
    result=-1
    for i in range(len(array)):
        if array[i]==k:
            result=i
            break

    if result==-1:
        print("Element not found in given array")
    else:
        print("Element is at index ",i)
        
    

if __name__=='__main__':
    array=input("Enter array").split(',')
    array=list(map(int,array))
    search_element=int(input("Enter element to be searched"))
    Linear_Search(array,search_element)