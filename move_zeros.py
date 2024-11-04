'''Write a function move_zeros(numbers) that moves all 0s 
to the end of the list while maintaining the order of the other elements'''
def move_zeros_method1(arr):
    i=0
    while i<len(arr):
        if arr[i]==0:
            j=i
            while j<len(arr)-1:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                j+=1
        else:
            i+=1
    return arr



