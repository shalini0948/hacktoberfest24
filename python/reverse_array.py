# Define function
def reverse_Array(arr,n):
    for i in range(n // 2):
        arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]  #reverse array logic
    return arr

arr = [1, 2, 3, 4, 5] #input
n = len(arr) # length of array
new_Array=reverse_Array(arr,n) # Storing reverse array 
print(new_Array)
